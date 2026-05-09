import AppKit
import AVFoundation

final class AppDelegate: NSObject, NSApplicationDelegate {
    private var statusItem: NSStatusItem?
    private var enabled = true
    private var wakeSoundName: String = ""
    private var sleepSoundName: String = ""
    private var sounds: [Sound] = []
    private var player: AVAudioPlayer?

    private let defaults = UserDefaults.standard
    private let enabledKey = "WSS.enabled"
    private let wakeKey = "WSS.wakeSound"
    private let sleepKey = "WSS.sleepSound"

    private let defaultWake = "8bit-fanfare"
    private let defaultSleep = "steel-breeze"

    struct Sound {
        let name: String
        let url: URL
    }

    func applicationDidFinishLaunching(_ notification: Notification) {
        sounds = discoverBundledSounds()
        loadPreferences()
        setUpStatusItem()
        registerSleepWakeObservers()
    }

    private func discoverBundledSounds() -> [Sound] {
        let exts: Set<String> = ["wav", "aiff", "aif", "mp3", "m4a", "caf"]
        let bundle = Bundle.main
        let candidateRoots: [URL?] = [
            bundle.url(forResource: "Sounds", withExtension: nil),
            bundle.resourceURL?.appendingPathComponent("Sounds"),
            bundle.resourceURL,
            bundle.bundleURL.appendingPathComponent("Contents/Resources/Sounds")
        ]

        for case let root? in candidateRoots {
            guard FileManager.default.fileExists(atPath: root.path) else { continue }
            if let items = try? FileManager.default.contentsOfDirectory(at: root, includingPropertiesForKeys: nil) {
                let audio = items
                    .filter { exts.contains($0.pathExtension.lowercased()) }
                    .sorted { $0.lastPathComponent.lowercased() < $1.lastPathComponent.lowercased() }
                if !audio.isEmpty {
                    return audio.map {
                        Sound(name: $0.deletingPathExtension().lastPathComponent, url: $0)
                    }
                }
            }
        }
        return []
    }

    private func loadPreferences() {
        if defaults.object(forKey: enabledKey) != nil {
            enabled = defaults.bool(forKey: enabledKey)
        }
        wakeSoundName = pickInitialSound(saved: defaults.string(forKey: wakeKey), preferred: defaultWake)
        sleepSoundName = pickInitialSound(saved: defaults.string(forKey: sleepKey), preferred: defaultSleep)
    }

    private func pickInitialSound(saved: String?, preferred: String) -> String {
        if let saved = saved, sounds.contains(where: { $0.name == saved }) {
            return saved
        }
        if sounds.contains(where: { $0.name == preferred }) {
            return preferred
        }
        return sounds.first?.name ?? ""
    }

    private func setUpStatusItem() {
        let item = NSStatusBar.system.statusItem(withLength: NSStatusItem.variableLength)
        if let button = item.button {
            let image = NSImage(systemSymbolName: "moon.zzz", accessibilityDescription: "Wake/Sleep Sounds")
            image?.isTemplate = true
            button.image = image
        }
        item.menu = buildMenu()
        statusItem = item
    }

    private func buildMenu() -> NSMenu {
        let menu = NSMenu()

        let enabledItem = NSMenuItem(title: "Enabled", action: #selector(toggleEnabled), keyEquivalent: "")
        enabledItem.target = self
        enabledItem.state = enabled ? .on : .off
        menu.addItem(enabledItem)

        menu.addItem(.separator())

        if sounds.isEmpty {
            let missing = NSMenuItem(title: "No sounds found in bundle", action: nil, keyEquivalent: "")
            missing.isEnabled = false
            menu.addItem(missing)
        } else {
            menu.addItem(soundMenu(title: "Wake sound", current: wakeSoundName, action: #selector(selectWakeSound(_:))))
            menu.addItem(soundMenu(title: "Sleep sound", current: sleepSoundName, action: #selector(selectSleepSound(_:))))
        }

        menu.addItem(.separator())

        let testWake = NSMenuItem(title: "Test wake sound", action: #selector(playTestWake), keyEquivalent: "w")
        testWake.target = self
        testWake.isEnabled = !sounds.isEmpty
        menu.addItem(testWake)

        let testSleep = NSMenuItem(title: "Test sleep sound", action: #selector(playTestSleep), keyEquivalent: "s")
        testSleep.target = self
        testSleep.isEnabled = !sounds.isEmpty
        menu.addItem(testSleep)

        menu.addItem(.separator())

        let about = NSMenuItem(title: "About Wake/Sleep Sounds", action: #selector(showAbout), keyEquivalent: "")
        about.target = self
        menu.addItem(about)

        let quit = NSMenuItem(title: "Quit", action: #selector(NSApplication.terminate(_:)), keyEquivalent: "q")
        menu.addItem(quit)

        return menu
    }

    private func soundMenu(title: String, current: String, action: Selector) -> NSMenuItem {
        let parent = NSMenuItem(title: title, action: nil, keyEquivalent: "")
        let submenu = NSMenu(title: title)
        for sound in sounds {
            let item = NSMenuItem(title: sound.name, action: action, keyEquivalent: "")
            item.target = self
            item.representedObject = sound.name
            item.state = (sound.name == current) ? .on : .off
            submenu.addItem(item)
        }
        parent.submenu = submenu
        return parent
    }

    private func rebuildMenu() {
        statusItem?.menu = buildMenu()
    }

    @objc private func toggleEnabled() {
        enabled.toggle()
        defaults.set(enabled, forKey: enabledKey)
        rebuildMenu()
    }

    @objc private func selectWakeSound(_ sender: NSMenuItem) {
        guard let name = sender.representedObject as? String else { return }
        wakeSoundName = name
        defaults.set(name, forKey: wakeKey)
        rebuildMenu()
        play(named: name)
    }

    @objc private func selectSleepSound(_ sender: NSMenuItem) {
        guard let name = sender.representedObject as? String else { return }
        sleepSoundName = name
        defaults.set(name, forKey: sleepKey)
        rebuildMenu()
        play(named: name)
    }

    @objc private func playTestWake() { play(named: wakeSoundName) }
    @objc private func playTestSleep() { play(named: sleepSoundName) }

    @objc private func showAbout() {
        let alert = NSAlert()
        alert.messageText = "Wake/Sleep Sounds"
        alert.informativeText = """
        Plays a cheerful jingle when your Mac wakes up,
        and a gentler one just before it drifts to sleep.

        Sounds are from Kenney's Music Jingles (CC0).
        """
        alert.runModal()
    }

    private func registerSleepWakeObservers() {
        let center = NSWorkspace.shared.notificationCenter
        center.addObserver(self,
                           selector: #selector(handleWillSleep),
                           name: NSWorkspace.willSleepNotification,
                           object: nil)
        center.addObserver(self,
                           selector: #selector(handleDidWake),
                           name: NSWorkspace.didWakeNotification,
                           object: nil)
    }

    @objc private func handleWillSleep(_ notification: Notification) {
        guard enabled else { return }
        playSync(named: sleepSoundName, maxWait: 2.0)
    }

    @objc private func handleDidWake(_ notification: Notification) {
        guard enabled else { return }
        play(named: wakeSoundName)
    }

    private func play(named name: String) {
        guard let url = sounds.first(where: { $0.name == name })?.url else { return }
        do {
            let p = try AVAudioPlayer(contentsOf: url)
            p.prepareToPlay()
            p.play()
            player = p
        } catch {
            NSSound.beep()
        }
    }

    private func playSync(named name: String, maxWait: TimeInterval) {
        guard let url = sounds.first(where: { $0.name == name })?.url else { return }
        do {
            let p = try AVAudioPlayer(contentsOf: url)
            p.prepareToPlay()
            p.play()
            player = p
            let deadline = Date().addingTimeInterval(maxWait)
            while p.isPlaying && Date() < deadline {
                RunLoop.current.run(mode: .default, before: Date().addingTimeInterval(0.05))
            }
        } catch {
            // Silent failure; sleep is imminent.
        }
    }
}
