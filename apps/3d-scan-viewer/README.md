# 3D Scan Viewer

A high-quality web-based viewer for 3D scans from iPhone apps like Scaniverse and KIRI Engine. View and interact with various 3D file formats including meshes and point clouds.

## Overview

3D Scan Viewer is a modern, performant web application built with Three.js that allows you to visualize 3D scans directly in your browser. Perfect for viewing exports from popular iPhone 3D scanning apps.

**Live Demo:** [https://joncooper.github.io/claude-speriments/3d-scan-viewer/](https://joncooper.github.io/claude-speriments/3d-scan-viewer/)

## Features

### Supported File Formats

- **USDZ** - Apple's Universal Scene Description format
- **FBX** - Autodesk FilmBox format
- **OBJ** - Wavefront OBJ format
- **GLB/GLTF** - glTF binary and JSON formats
- **PLY** - Polygon/Point Cloud format with color support
- **LAS** - LiDAR point cloud format (coming soon)

### Viewer Features

- **Intuitive Controls**
  - Rotate: Left-click + drag
  - Zoom: Scroll wheel
  - Pan: Right-click + drag
  - Reset camera to default view

- **Display Modes**
  - Solid mesh rendering with realistic lighting
  - Wireframe mode for topology inspection
  - Point cloud visualization
  - Toggle grid for spatial reference

- **Model Information**
  - Automatic vertex count
  - Face/triangle count
  - File format detection
  - Auto-centering and scaling

- **Performance**
  - Hardware-accelerated rendering
  - Optimized for large models
  - Responsive design (mobile-friendly)
  - Smooth 60fps animations

## Quick Start

### Development

```bash
# Install dependencies
bun install

# Start development server
bun run dev

# Open http://localhost:5173 in your browser
```

### Build for Production

```bash
# Build the application
bun run build

# Preview the production build
bun run preview
```

### Deploy to GitHub Pages

```bash
# Deploy to /docs directory
./deploy-to-pages.sh

# Commit and push
git add docs/
git commit -m "Deploy 3D Scan Viewer"
git push
```

## Usage

1. **Load a File**
   - Click the upload area or drag & drop a 3D file
   - Supported formats: USDZ, FBX, OBJ, GLB, GLTF, PLY, LAS

2. **Navigate the Scene**
   - Rotate: Click and drag
   - Zoom: Scroll wheel
   - Pan: Right-click and drag

3. **Adjust Display**
   - Reset View: Return camera to default position
   - Wireframe: Toggle wireframe overlay
   - Grid: Show/hide ground grid
   - Points: Convert mesh to point cloud visualization

## Technical Details

### Built With

- **Three.js** - 3D graphics library
- **TypeScript** - Type-safe JavaScript
- **Vite** - Fast build tool and dev server
- **Bun** - Fast package manager and runtime

### Architecture

The viewer is organized into functional modules:

- **Scene Setup** - Camera, lighting, renderer configuration
- **File Loaders** - Format-specific loading logic (GLTFLoader, FBXLoader, etc.)
- **Model Processing** - Auto-centering, scaling, and optimization
- **UI Controls** - File input, buttons, display toggles
- **Rendering Loop** - Smooth 60fps animation with damped controls

### Performance Optimizations

- Progressive loading with loading indicators
- Automatic model scaling to fit viewport
- GPU-accelerated rendering
- Efficient memory management (object disposal)
- Optimized shadow maps (2048x2048)

## File Format Support

### Mesh Formats

| Format | Extension | Features |
|--------|-----------|----------|
| GLTF/GLB | .gltf, .glb | PBR materials, animations, efficient |
| FBX | .fbx | Industry standard, animations |
| OBJ | .obj | Simple, widely supported |
| USDZ | .usdz | Apple's format, AR-ready |

### Point Cloud Formats

| Format | Extension | Features |
|--------|-----------|----------|
| PLY | .ply | Color support, efficient |
| LAS | .las | LiDAR standard (coming soon) |

## Browser Compatibility

- Chrome/Edge 90+ (recommended)
- Firefox 88+
- Safari 14+
- Mobile browsers supported

**Requirements:**
- WebGL 2.0 support
- Modern JavaScript (ES2020+)

## Tips for Best Results

1. **File Size**: Keep files under 50MB for smooth performance
2. **Point Clouds**: PLY format works best for colored point clouds
3. **Meshes**: GLB is recommended for textured meshes
4. **Lighting**: The viewer uses realistic PBR lighting - works best with properly authored materials

## Common Issues

**Q: Model appears black/dark**
- Check that the model has proper normals
- Some formats may need external material files

**Q: Model is too small/large**
- The viewer auto-scales, but you can zoom in/out
- Use Reset View to recenter

**Q: File won't load**
- Ensure the file extension matches the format
- Check browser console for specific errors
- Try converting to GLB (widely supported)

## Roadmap

See [ICEBOX.md](./ICEBOX.md) for planned features.

## Development

### Project Structure

```
3d-scan-viewer/
├── src/
│   ├── main.ts          # Main application logic
│   └── style.css        # Styling
├── index.html           # HTML structure
├── package.json         # Dependencies
├── tsconfig.json        # TypeScript config
├── vite.config.ts       # Vite config (if needed)
└── deploy-to-pages.sh   # Deployment script
```

### Adding New File Formats

1. Import the loader from Three.js examples
2. Add file extension to accept attribute
3. Create loader function (see existing patterns)
4. Add case to switch statement in `loadFile()`

Example:
```typescript
import { STLLoader } from 'three/examples/jsm/loaders/STLLoader.js'

function loadSTL(url: string): Promise<THREE.Object3D> {
  return new Promise((resolve, reject) => {
    const loader = new STLLoader()
    loader.load(url, (geometry) => {
      const material = new THREE.MeshStandardMaterial()
      const mesh = new THREE.Mesh(geometry, material)
      resolve(mesh)
    }, undefined, reject)
  })
}
```

## Credits

- Built with [Three.js](https://threejs.org/)
- Designed for [Scaniverse](https://scaniverse.com/) and [KIRI Engine](https://www.kiriengine.com/) exports
- Icons from [Feather Icons](https://feathericons.com/)

## License

MIT License - see LICENSE file for details

---

**Status:** ✅ Complete (v1.0.0)

**Last updated:** November 2025
