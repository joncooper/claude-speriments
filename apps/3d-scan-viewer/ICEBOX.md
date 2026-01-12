# ICEBOX - Future Enhancements

Ideas and features for future versions of the 3D Scan Viewer.

## High Priority

### 1. LAS Point Cloud Support
**Priority:** High
**Effort:** Medium
**Value:** High for LiDAR workflows

Full support for LAS/LAZ files (LiDAR point cloud format):
- Use [laz-perf](https://github.com/hobu/laz-perf) or similar parser
- Efficient rendering of large point clouds (>10M points)
- Octree-based LOD for performance
- Classification coloring (ground, vegetation, buildings)

**Technical approach:**
- Web Worker for parsing (don't block main thread)
- Progressive loading for large files
- GPU-based point rendering via shaders

### 2. Measurement Tools
**Priority:** High
**Effort:** Medium
**Value:** Critical for practical use

Interactive measurement capabilities:
- **Distance tool** - Click two points, show distance
- **Area tool** - Draw polygon, calculate area
- **Volume tool** - Measure enclosed volume
- **Angle tool** - Measure angles between surfaces

**UI Mockup:**
```
[Ruler icon] Measure
  └─ Distance
  └─ Area
  └─ Volume
  └─ Angle
```

### 3. Annotations
**Priority:** Medium
**Effort:** Medium
**Value:** High for collaboration

Add notes and markers to 3D models:
- Click to place annotation pin
- Add text, photos, links
- Export annotations as JSON
- Share annotated views via URL

**Use cases:**
- Construction site documentation
- Quality control notes
- Collaborative review

### 4. Cross-Section View
**Priority:** Medium
**Effort:** High
**Value:** High for analysis

Slice through models to view internals:
- Draggable clipping plane
- Rotate plane in X/Y/Z
- Show measurement at slice
- Export cross-section as 2D image

**Implementation:**
- Use Three.js clipping planes
- Fragment shader for cut edges
- 2D overlay showing measurements

### 5. Advanced Point Cloud Features
**Priority:** Medium
**Effort:** High
**Value:** Medium (specialized use)

Enhanced point cloud visualization:
- **Point size slider** - Adjust size in UI
- **Color by elevation** - Height-based gradient
- **Color by intensity** - For LiDAR data
- **Decimation** - Reduce points for performance
- **Density visualization** - Show coverage gaps

## Medium Priority

### 6. Model Comparison
**Priority:** Medium
**Effort:** High
**Value:** Medium

Compare two versions of a model:
- Side-by-side view
- Overlay mode with transparency
- Difference heatmap (show changes)
- Alignment tools

**Use cases:**
- Before/after comparisons
- Quality control (scan vs CAD)
- Progress tracking

### 7. Export Capabilities
**Priority:** Medium
**Effort:** Low-Medium
**Value:** Medium

Export processed models and views:
- **Screenshot** - High-res PNG/JPG of current view
- **Turntable video** - 360° rotation MP4
- **Simplified mesh** - Decimate and export
- **Point cloud subset** - Crop and export region

### 8. Lighting Presets
**Priority:** Low
**Effort:** Low
**Value:** Medium

Predefined lighting setups:
- Studio lighting (3-point)
- Outdoor (HDR environment)
- Dramatic (spotlight)
- Flat (no shadows)
- Custom (user-adjustable)

**Implementation:**
- Preset JSON configs
- UI dropdown selector
- Save custom presets to localStorage

### 9. Material Editor
**Priority:** Low
**Effort:** Medium
**Value:** Low (specialized)

Adjust material properties:
- Color picker
- Roughness/metalness sliders
- Opacity control
- Texture replacement
- Save material overrides

### 10. File Format Conversion
**Priority:** Low
**Effort:** High
**Value:** Medium

Convert between formats in-browser:
- USDZ → GLB
- OBJ → GLB
- PLY → OBJ
- Export with textures

**Challenge:** Complex conversions need server-side processing

## Low Priority (Nice to Have)

### 11. VR/AR Support
**Priority:** Low
**Effort:** High
**Value:** Low (niche use case)

View models in VR/AR:
- WebXR support
- VR controller navigation
- AR placement on real surfaces (iOS/Android)

**Requires:**
- WebXR device API
- Separate camera/control setup
- Testing on VR/AR devices

### 12. Collaboration Features
**Priority:** Low
**Effort:** Very High
**Value:** Low (needs backend)

Real-time multi-user viewing:
- Share session via link
- Synchronized camera views
- Voice chat overlay
- Shared annotations

**Requires:**
- WebSocket/WebRTC backend
- User authentication
- Persistent storage

### 13. Automatic Defect Detection
**Priority:** Low
**Effort:** Very High
**Value:** High (specialized)

AI-powered analysis:
- Detect holes/gaps in mesh
- Identify scan artifacts
- Suggest cleanup operations
- Quality scoring

**Requires:**
- ML model training
- Server-side processing
- Large dataset of examples

### 14. Animation Playback
**Priority:** Low
**Effort:** Medium
**Value:** Low (rare in scans)

Play embedded animations:
- Timeline scrubber
- Play/pause controls
- Speed adjustment
- Loop toggle

**Note:** Most 3D scans don't have animations, but FBX/GLTF may include them

### 15. Mesh Analysis Tools
**Priority:** Low
**Effort:** High
**Value:** Medium (specialized)

Advanced geometry analysis:
- Non-manifold edge detection
- Normal consistency check
- UV unwrapping visualization
- Triangle count optimization

### 16. Batch Processing
**Priority:** Low
**Effort:** Medium
**Value:** Low

Load multiple files:
- Folder upload
- Switch between models
- Compare all in grid view
- Batch export

### 17. Texture Baking
**Priority:** Low
**Effort:** Very High
**Value:** Low (specialized)

Generate textures from lighting:
- Bake ambient occlusion
- Generate normal maps
- Export PBR texture set

**Requires:**
- Complex shader setup
- Server-side rendering for quality

### 18. Performance Profiler
**Priority:** Low
**Effort:** Low
**Value:** Low (dev tool)

Show performance stats:
- FPS counter
- Triangle count
- Draw calls
- Memory usage
- GPU utilization

### 19. Keyboard Shortcuts
**Priority:** Low
**Effort:** Low
**Value:** Medium

Power user features:
- `G` - Toggle grid
- `W` - Toggle wireframe
- `P` - Toggle points
- `R` - Reset camera
- `F` - Frame selected
- `1-5` - Lighting presets
- `H` - Show help overlay

### 20. Preset Camera Angles
**Priority:** Low
**Effort**: Low
**Value:** Medium

Quick camera positioning:
- Top view
- Front view
- Side view
- Bottom view
- Isometric view
- Save custom views

## Research Ideas

### Experimental Features (Needs Investigation)

1. **Neural Radiance Fields (NeRF)**
   - Import NeRF reconstructions
   - Real-time NeRF rendering via WebGL
   - Convert NeRF to mesh

2. **Gaussian Splatting**
   - New 3D representation format
   - Potentially better for photorealistic scans
   - WebGL implementation available

3. **AI Mesh Cleanup**
   - Automatic hole filling
   - Noise reduction
   - Mesh simplification while preserving detail

4. **Photogrammetry Processing**
   - Upload photos → generate 3D model
   - Client-side processing (very ambitious)
   - Or integration with cloud services

5. **Point Cloud Classification**
   - ML-based semantic segmentation
   - Separate ground, buildings, vegetation
   - Interactive class editing

## Community Requests

Track user-requested features here:
- (None yet)

## Rejected Ideas

Features we've considered but decided against:

1. **Built-in 3D Modeling Tools**
   - Reason: Scope creep, use Blender instead

2. **Cloud Storage Integration**
   - Reason: Privacy concerns, keep it local-first

3. **Social Features (Comments, Likes)**
   - Reason: Out of scope, not a platform

---

**How to prioritize:**
1. User requests
2. Feature impact vs. effort
3. Alignment with core mission (viewing scans)
4. Technical feasibility

**Last Updated:** November 20, 2025
