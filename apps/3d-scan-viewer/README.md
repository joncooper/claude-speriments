# 3D Room Planner

An interactive room planning tool for iPhone RoomPlanner scans. Remove furniture, paint walls, and try virtual furniture arrangements with real dimensions.

## Overview

3D Room Planner is a web-based application that lets you edit and plan rooms scanned with iPhone's RoomPlanner API. Load USDZ files, classify objects (walls, floor, furniture), make changes, and export the modified scene.

**Live Demo:** [https://joncooper.github.io/claude-speriments/3d-scan-viewer/](https://joncooper.github.io/claude-speriments/3d-scan-viewer/)

## Features

### 🎯 Two Modes

**View Mode** (Default)
- Rotate, zoom, pan with orbit controls
- Inspect 3D room scans
- No editing capabilities

**Edit Mode**
- Click to select objects
- Remove or hide furniture
- Paint walls with custom colors
- Add virtual furniture with real dimensions
- Move, rotate, and scale furniture blocks

### 🏗️ Room Editing

**Object Classification**
- Automatically identifies walls, floor, and furniture from USDZ metadata
- Falls back to geometry analysis (shape/size) for unnamed objects
- Color-coded badges: Wall (blue), Floor (purple), Furniture (pink)

**Furniture Management**
- **Remove furniture**: Select and delete unwanted objects
- **Hide objects**: Temporarily hide objects from view
- **Protect floor**: Floor cannot be deleted (safety feature)

**Wall Painting**
- Select any wall object
- Choose color with color picker
- Click "Paint Selected Wall" to apply
- Creates new PBR material with selected color

**Virtual Furniture**
- Add furniture blocks with precise dimensions (meters)
- Quick presets: Sofa (2.0×0.9×0.45m), Table (1.5×1.5×0.75m), Chair (1.0×0.6×0.5m), Bed (2.0×1.6×0.6m)
- Custom dimensions via input fields
- Semi-transparent gray material for easy visualization

**Transform Controls**
- **Move** (T key): Drag furniture to new position
- **Rotate** (R key): Rotate furniture around axes
- **Scale** (S key): Resize furniture blocks
- Visual gizmo with axis-aligned handles

### 📁 Supported File Formats

- **USDZ** - Primary format, iPhone RoomPlanner with metadata
- **GLB/GLTF** - Industry-standard 3D format
- **FBX** - Autodesk format with animations
- **OBJ** - Simple mesh format
- **PLY** - Point cloud format (with colors)

### ⌨️ Keyboard Shortcuts

- **ESC** - Deselect current object
- **Delete/Backspace** - Delete selected object
- **T** - Switch to Translate mode (when furniture selected)
- **R** - Switch to Rotate mode (when furniture selected)
- **S** - Switch to Scale mode (when furniture selected)

### 💾 Export

Export modified scenes as GLTF JSON files:
- Includes all changes (removed furniture, painted walls, virtual furniture)
- Compatible with most 3D software
- Can be re-imported for further editing

## Quick Start

### Development

```bash
# Install dependencies
bun install

# Start development server
bun run dev

# Open http://localhost:5173
```

### Production Build

```bash
# Build optimized bundle
bun run build

# Preview production build
bun run preview
```

### Deploy to GitHub Pages

```bash
./deploy-to-pages.sh
```

## Usage Guide

### 1. Load a Room Scan

- Click the upload area or drag & drop a USDZ file
- Room will auto-center and scale to fit view
- Objects are automatically classified

### 2. Switch to Edit Mode

- Click the "Edit" button in controls panel
- Edit tools panel appears below controls
- Click objects to select them

### 3. Edit the Room

**Remove Furniture:**
1. Click a furniture object to select it
2. Click "Delete Selected" or press Delete key
3. Object is removed from scene

**Paint Walls:**
1. Click a wall to select it
2. Choose color from "Wall Color" picker
3. Click "Paint Selected Wall"
4. Wall updates with new color

**Add Virtual Furniture:**
1. Enter dimensions (width, depth, height in meters)
   - Or click a preset button (Sofa, Table, Chair, Bed)
2. Click "Add Furniture Block"
3. Furniture appears at center of room
4. Use transform controls to position it

**Transform Furniture:**
1. Select virtual furniture (click it)
2. Transform gizmo appears
3. Press T/R/S to switch modes or drag handles
4. Move, rotate, or scale as needed

### 4. Export Modified Scene

1. Click "Export Modified USDZ" button
2. GLTF file downloads automatically
3. Can be opened in Blender, Three.js, etc.

## Technical Details

### Built With

- **Three.js** - WebGL 3D rendering engine
- **TypeScript** - Type-safe JavaScript
- **Vite** - Fast build tool and dev server
- **Bun** - Ultra-fast package manager

### Architecture

**Object Classification System:**
```typescript
type ObjectType = 'wall' | 'floor' | 'furniture' | 'virtual-furniture' | 'unknown'

interface ClassifiedObject {
  object: THREE.Object3D
  type: ObjectType
  name: string
  originalMaterial?: THREE.Material | THREE.Material[]
}
```

**Classification Logic:**
1. Check object name for keywords (wall, floor, furniture, table, chair, etc.)
2. If no name match, analyze geometry:
   - Flat horizontal objects (y < 0.1m) → floor
   - Tall thin objects (y > 1m, x or z < 0.3m) → wall
   - Everything else → unknown

**Transform Controls:**
- Uses Three.js TransformControls
- Three modes: translate, rotate, scale
- Disables orbit controls while dragging
- Only active when virtual furniture is selected

**Material System:**
- Painted walls get new MeshStandardMaterial
- Virtual furniture uses semi-transparent material (opacity 0.8)
- Roughness/metalness tuned for realistic PBR rendering

### Performance

- 60fps rendering on modern hardware
- Handles rooms with 50+ objects smoothly
- Optimized raycasting for object selection
- Efficient shadow maps (2048x2048)

## Browser Compatibility

- Chrome/Edge 90+ (recommended)
- Firefox 88+
- Safari 14+
- Mobile browsers supported

**Requirements:**
- WebGL 2.0
- Modern JavaScript (ES2020+)
- File API support

## Tips for Best Results

1. **USDZ Files**: Use scans from iPhone RoomPlanner app for best metadata
2. **Object Names**: If objects aren't classified correctly, check names in the scan
3. **Dimensions**: Virtual furniture uses meters - typical room is 3-5m wide
4. **Transforms**: Press T/R/S to switch modes if gizmo isn't visible
5. **Export**: Exported GLTF includes the entire scene (lighting, grid, etc.)

## Known Limitations

1. **USDZ Export**: Currently exports as GLTF (more reliable than USDZ export)
2. **LAS Format**: Point cloud support planned, not yet implemented
3. **Texture Editing**: Can only change wall colors, not apply textures
4. **Undo/Redo**: Not implemented - reload file to start over
5. **Metadata**: USDZ metadata parsing is heuristic-based, may misclassify some objects

## Roadmap

See [ICEBOX.md](./ICEBOX.md) for future enhancements.

**High Priority:**
- LAS point cloud support
- Measurement tools (distance, area, volume)
- Annotations and notes
- Cross-section views
- Better USDZ metadata parsing

## Development

### Project Structure

```
3d-scan-viewer/
├── src/
│   ├── main.ts          # Main application (774 lines)
│   └── style.css        # Styling (558 lines)
├── index.html           # HTML structure
├── README.md            # This file
├── NOTES.md             # Implementation details
├── ICEBOX.md            # Future ideas
├── package.json         # Dependencies
└── deploy-to-pages.sh   # Deployment script
```

### Key Files

- **main.ts** - Core logic, scene setup, object management, UI handlers
- **style.css** - Modern dark theme with responsive design
- **index.html** - Semantic HTML with mode toggle and edit tools

### Adding Features

**New Object Type:**
1. Add to `ObjectType` union type
2. Update `classifyObjects()` logic
3. Add classification color to CSS (`.type-badge.yourtype`)

**New Tool:**
1. Add button to HTML in edit tools panel
2. Create handler function in main.ts
3. Wire up event listener
4. Update UI state as needed

## Credits

- Built with [Three.js](https://threejs.org/)
- Designed for [iPhone RoomPlanner API](https://developer.apple.com/documentation/roomplan)
- Icons from [Feather Icons](https://feathericons.com/)
- Inspired by 3D room planning tools like Floorplanner, RoomSketcher

## License

MIT License - see LICENSE file for details

---

**Status:** ✅ Complete (v2.0.0)

**Last updated:** November 2025
