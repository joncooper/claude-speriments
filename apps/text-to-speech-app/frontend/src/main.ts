import "./style.css";

// ===== DOM Elements =====
const tabs = document.querySelectorAll<HTMLButtonElement>(".tab");
const tabPanels = document.querySelectorAll<HTMLDivElement>(".tab-panel");
const textInput = document.getElementById("text-input") as HTMLTextAreaElement;
const urlInput = document.getElementById("url-input") as HTMLInputElement;
const pdfInput = document.getElementById("pdf-input") as HTMLInputElement;
const pdfDropZone = document.getElementById("pdf-drop-zone") as HTMLLabelElement;
const pdfFileName = document.getElementById("pdf-file-name") as HTMLDivElement;

const voiceCards = document.querySelectorAll<HTMLLabelElement>(".radio-card");
const cloneUpload = document.getElementById("clone-upload") as HTMLDivElement;
const refAudioInput = document.getElementById("ref-audio-input") as HTMLInputElement;
const audioDropZone = document.getElementById("audio-drop-zone") as HTMLLabelElement;
const refAudioFileName = document.getElementById("ref-audio-file-name") as HTMLDivElement;

const exaggerationSlider = document.getElementById("exaggeration") as HTMLInputElement;
const exaggerationValue = document.getElementById("exaggeration-value") as HTMLSpanElement;
const cfgWeightSlider = document.getElementById("cfg-weight") as HTMLInputElement;
const cfgWeightValue = document.getElementById("cfg-weight-value") as HTMLSpanElement;

const previewBtn = document.getElementById("preview-btn") as HTMLButtonElement;
const previewArea = document.getElementById("preview-area") as HTMLDivElement;
const previewText = document.getElementById("preview-text") as HTMLDivElement;
const wordCount = document.getElementById("word-count") as HTMLSpanElement;
const chunkCount = document.getElementById("chunk-count") as HTMLSpanElement;

const generateBtn = document.getElementById("generate-btn") as HTMLButtonElement;

const progressSection = document.getElementById("progress-section") as HTMLElement;
const progressBar = document.getElementById("progress-bar") as HTMLDivElement;
const progressStatus = document.getElementById("progress-status") as HTMLSpanElement;
const progressPercent = document.getElementById("progress-percent") as HTMLSpanElement;
const progressDetail = document.getElementById("progress-detail") as HTMLParagraphElement;

const playerSection = document.getElementById("player-section") as HTMLElement;
const audioPlayer = document.getElementById("audio-player") as HTMLAudioElement;
const downloadBtn = document.getElementById("download-btn") as HTMLAnchorElement;

const errorSection = document.getElementById("error-section") as HTMLElement;
const errorMessage = document.getElementById("error-message") as HTMLParagraphElement;

// ===== State =====
let activeTab = "text";
let selectedPdfFile: File | null = null;
let selectedRefAudio: File | null = null;

// ===== Tab Switching =====
tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    const target = tab.dataset.tab!;
    activeTab = target;

    tabs.forEach((t) => {
      t.classList.toggle("active", t.dataset.tab === target);
      t.setAttribute("aria-selected", String(t.dataset.tab === target));
    });
    tabPanels.forEach((p) => {
      p.classList.toggle("active", p.dataset.panel === target);
    });
  });
});

// ===== Voice Mode Toggle =====
voiceCards.forEach((card) => {
  card.addEventListener("click", () => {
    voiceCards.forEach((c) => c.classList.remove("active"));
    card.classList.add("active");

    const mode = card.dataset.voice;
    cloneUpload.hidden = mode !== "clone";
  });
});

// ===== File Uploads =====
function setupDropZone(
  dropZone: HTMLElement,
  fileInput: HTMLInputElement,
  fileNameEl: HTMLDivElement,
  onSelect: (file: File) => void,
) {
  dropZone.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropZone.classList.add("drag-over");
  });

  dropZone.addEventListener("dragleave", () => {
    dropZone.classList.remove("drag-over");
  });

  dropZone.addEventListener("drop", (e) => {
    e.preventDefault();
    dropZone.classList.remove("drag-over");
    const file = (e as DragEvent).dataTransfer?.files[0];
    if (file) {
      onSelect(file);
      showFileName(fileNameEl, file.name);
    }
  });

  fileInput.addEventListener("change", () => {
    const file = fileInput.files?.[0];
    if (file) {
      onSelect(file);
      showFileName(fileNameEl, file.name);
    }
  });
}

function showFileName(el: HTMLDivElement, name: string) {
  el.textContent = name;
  el.hidden = false;
}

setupDropZone(pdfDropZone, pdfInput, pdfFileName, (f) => {
  selectedPdfFile = f;
});
setupDropZone(audioDropZone, refAudioInput, refAudioFileName, (f) => {
  selectedRefAudio = f;
});

// ===== Sliders =====
exaggerationSlider.addEventListener("input", () => {
  exaggerationValue.textContent = parseFloat(exaggerationSlider.value).toFixed(2);
});
cfgWeightSlider.addEventListener("input", () => {
  cfgWeightValue.textContent = parseFloat(cfgWeightSlider.value).toFixed(2);
});

// ===== Build FormData =====
function buildFormData(): FormData {
  const fd = new FormData();

  if (activeTab === "text") {
    fd.append("text", textInput.value);
  } else if (activeTab === "url") {
    fd.append("url", urlInput.value);
  } else if (activeTab === "pdf" && selectedPdfFile) {
    fd.append("file", selectedPdfFile);
  }

  if (selectedRefAudio) {
    fd.append("reference_audio", selectedRefAudio);
  }

  fd.append("exaggeration", exaggerationSlider.value);
  fd.append("cfg_weight", cfgWeightSlider.value);

  return fd;
}

function hasInput(): boolean {
  if (activeTab === "text") return textInput.value.trim().length > 0;
  if (activeTab === "url") return urlInput.value.trim().length > 0;
  if (activeTab === "pdf") return selectedPdfFile !== null;
  return false;
}

// ===== Preview =====
previewBtn.addEventListener("click", async () => {
  if (!hasInput()) {
    showError("Please provide some content first.");
    return;
  }

  previewBtn.classList.add("btn-loading");
  previewBtn.disabled = true;
  hideError();

  try {
    const fd = buildFormData();
    const resp = await fetch("/api/extract-text", { method: "POST", body: fd });

    if (!resp.ok) {
      const data = await resp.json();
      throw new Error(data.detail || "Failed to extract text");
    }

    const data = await resp.json();
    previewText.textContent = data.text;
    wordCount.textContent = `${data.word_count.toLocaleString()} words`;
    chunkCount.textContent = `${data.chunk_count} chunks`;
    previewArea.hidden = false;
  } catch (e) {
    showError((e as Error).message);
  } finally {
    previewBtn.classList.remove("btn-loading");
    previewBtn.disabled = false;
  }
});

// ===== Generate =====
generateBtn.addEventListener("click", async () => {
  if (!hasInput()) {
    showError("Please provide some content first.");
    return;
  }

  generateBtn.classList.add("btn-loading");
  generateBtn.disabled = true;
  hideError();
  hidePlayer();
  showProgress();

  try {
    const fd = buildFormData();
    const resp = await fetch("/api/generate", { method: "POST", body: fd });

    if (!resp.ok) {
      const data = await resp.json();
      throw new Error(data.detail || "Failed to start generation");
    }

    const data = await resp.json();
    const jobId: string = data.job_id;
    const totalChunks: number = data.total_chunks;

    updateProgress(0, 0, totalChunks, "Starting synthesis...");

    // Connect to SSE
    const evtSource = new EventSource(`/api/progress/${jobId}`);

    evtSource.addEventListener("progress", (e: MessageEvent) => {
      const info = JSON.parse(e.data);
      updateProgress(
        info.progress,
        info.current_chunk,
        info.total_chunks,
        `Synthesizing chunk ${info.current_chunk} of ${info.total_chunks}...`,
      );
    });

    evtSource.addEventListener("complete", (e: MessageEvent) => {
      evtSource.close();
      const info = JSON.parse(e.data);
      updateProgress(100, totalChunks, totalChunks, "Complete!");

      // Show audio player
      const audioUrl = info.audio_url;
      audioPlayer.src = audioUrl;
      downloadBtn.href = audioUrl;
      playerSection.hidden = false;

      // Scroll to player
      setTimeout(() => {
        playerSection.scrollIntoView({ behavior: "smooth", block: "center" });
      }, 300);

      generateBtn.classList.remove("btn-loading");
      generateBtn.disabled = false;

      // Hide progress after a moment
      setTimeout(() => {
        progressSection.hidden = true;
      }, 1000);
    });

    evtSource.addEventListener("error", (e: Event) => {
      // Check if it's an SSE error event with data
      const msgEvent = e as MessageEvent;
      if (msgEvent.data) {
        const info = JSON.parse(msgEvent.data);
        showError(info.error || "Generation failed");
      } else {
        showError("Connection lost. Please try again.");
      }
      evtSource.close();
      progressSection.hidden = true;
      generateBtn.classList.remove("btn-loading");
      generateBtn.disabled = false;
    });
  } catch (e) {
    showError((e as Error).message);
    progressSection.hidden = true;
    generateBtn.classList.remove("btn-loading");
    generateBtn.disabled = false;
  }
});

// ===== UI Helpers =====
function showProgress() {
  progressSection.hidden = false;
  progressBar.style.width = "0%";
  progressStatus.textContent = "Preparing...";
  progressPercent.textContent = "0%";
  progressDetail.textContent = "Starting synthesis...";
}

function updateProgress(
  percent: number,
  current: number,
  total: number,
  detail: string,
) {
  progressBar.style.width = `${percent}%`;
  progressPercent.textContent = `${percent}%`;
  progressStatus.textContent =
    percent >= 100 ? "Complete!" : `Processing (${current}/${total})`;
  progressDetail.textContent = detail;
}

function hidePlayer() {
  playerSection.hidden = true;
  audioPlayer.pause();
  audioPlayer.src = "";
}

function showError(msg: string) {
  errorMessage.textContent = msg;
  errorSection.hidden = false;
  errorSection.scrollIntoView({ behavior: "smooth", block: "center" });
}

function hideError() {
  errorSection.hidden = true;
}
