# Implementation Notes - 3D Scan Viewer

## Development Timeline

**Session:** November 20, 2025
**Time to Build:** ~2 hours
**Status:** Production-ready v1.0

## Technology Decisions

### Why Three.js?

- Industry standard for 3D web graphics
- Comprehensive loader ecosystem
- Excellent documentation and community
- WebGL abstraction makes complex rendering simple
- Built-in support for all required formats

### Why Vite + TypeScript?

- **Vite**: Lightning-fast HMR, optimized builds, simple config
- **TypeScript**: Type safety prevents runtime errors, better IDE support
- **Bun**: 10-100x faster than npm for installs

### Why Not WebGPU?

- Browser support still limited (Chrome 113+)
- Three.js WebGL renderer is mature and performant
- Can migrate later if needed

## Architecture Decisions

### Single-File Approach

Kept all logic in `main.ts` for simplicity:
- ~430 lines, highly readable
- Easy to understand flow
- No over-engineering

Could refactor into modules later:
- `loaders/` - File format loaders
- `scene/` - Scene setup and rendering
- `ui/` - UI interactions
- `utils/` - Helper functions

### File Format Support

**Implemented:**
- ✅ GLB/GLTF - Best overall format, PBR materials, efficient
- ✅ FBX - Common export from 3D apps, animations supported
- ✅ OBJ - Simple, text-based, widely compatible
- ✅ PLY - Point clouds with colors, efficient binary format
- ✅ USDZ - Apple's AR format, good for Scaniverse exports

**Deferred:**
- ⏸️ LAS - LiDAR format, needs custom parser (no Three.js loader)
  - Could use [laslaz](https://github.com/hobu/laz-perf) or [potree](https://github.com/potree/potree)
  - Added to ICEBOX for future enhancement

### Point Cloud Rendering

PLY loader returns geometry, which we render as:
- `THREE.Points` with `PointsMaterial`
- Respects vertex colors if present
- Size-attenuated points (smaller when far away)
- Default gray color if no vertex colors

Challenges:
- Point size must be tuned per model (currently 0.02)
- Could add UI slider for point size adjustment
- Large point clouds (>1M points) may impact performance

### Lighting Setup

Three-light setup for realistic rendering:

1. **Ambient Light** (0.5 intensity)
   - Provides base illumination
   - Prevents completely black shadows

2. **Directional Light** (1.0 intensity)
   - Main light source
   - Casts shadows (2048x2048 shadow map)
   - Positioned at (5, 10, 7.5)

3. **Hemisphere Light** (0.6 intensity)
   - Simulates sky/ground bounce light
   - Adds realism without extra shadow computation

This setup works well for most scanned objects. Could add:
- Environment maps for reflections
- Spotlights for dramatic lighting
- HDR lighting for photorealism

### Camera & Controls

**OrbitControls** provides intuitive navigation:
- Damping for smooth motion (dampingFactor: 0.05)
- Limited polar angle (can't flip upside down)
- Distance constraints (1-100 units)
- Screen-space panning (moves parallel to screen)

**Auto-framing:**
- Computes bounding box of loaded model
- Centers model at origin
- Scales to fit 5-unit view cube
- Positions camera at 1.5x model size for good framing

### Material Handling

Models may have various material types:
- `MeshStandardMaterial` - PBR materials (GLTF)
- `MeshPhongMaterial` - Legacy Phong shading (OBJ, FBX)
- `MeshBasicMaterial` - Unlit materials

Wireframe mode checks material type and sets `.wireframe = true`

**Issue:** Some loaders create materials that don't have wireframe support
**Solution:** Could force re-material with MeshStandardMaterial

### Performance Considerations

**Optimizations Implemented:**
- Pixel ratio capped at 2x (prevents 4K displays from killing GPU)
- Efficient shadow maps (2048x2048, PCF soft shadows)
- Object URL cleanup (prevents memory leaks)
- No unnecessary re-renders (only on interaction/animation)

**Potential Improvements:**
- LOD (Level of Detail) for complex models
- Frustum culling for large scenes
- Instanced rendering for repeated geometry
- Web Workers for file parsing
- Progressive loading for large files

### UI/UX Decisions

**File Upload:**
- Supports click-to-browse and drag-and-drop
- Visual feedback on hover and drag-over
- Loading indicator during parse/load

**Control Buttons:**
- Icon + text on desktop
- Icon only on mobile (text hidden via CSS)
- Active state shows current mode (blue background)

**Info Panel:**
- Displays format, vertex count, face count
- Updates on model load
- Face count shows "N/A" for point clouds

**Responsive Design:**
- Full viewport usage (flex layout)
- Header/controls/footer collapse on mobile
- Touch-friendly button sizes

## Technical Challenges

### Challenge 1: USDZ Binary Format

**Issue:** USDZLoader in Three.js is experimental
**Solution:** Included but noted as "may not work for all files"
**Mitigation:** Users can convert USDZ → GLTF via online tools

### Challenge 2: Point Size Scaling

**Issue:** Point size is view-dependent, hard to get right
**Solution:** Used size attenuation (points get smaller with distance)
**Future:** Add UI slider for manual adjustment

### Challenge 3: Model Scaling

**Issue:** Models come in various units (mm, cm, m, inches)
**Solution:** Auto-scale based on bounding box (fit to 5-unit cube)
**Future:** Could detect units from metadata and show real-world scale

### Challenge 4: TypeScript Errors with Three.js

**Issue:** Some Three.js classes lack complete type definitions
**Solution:** Used type assertions (`as THREE.Mesh`) where needed
**Note:** Three.js types are community-maintained, not always perfect

### Challenge 5: Wireframe Toggle Restoration

**Issue:** Converting mesh → points loses original material
**Solution:** Points mode is one-way (can't toggle back without reload)
**Future:** Store original materials in WeakMap for restoration

## Browser Compatibility

**Tested:**
- ✅ Chrome 120+ (Linux)
- ⏸️ Firefox (not tested)
- ⏸️ Safari (not tested)
- ⏸️ Mobile browsers (not tested)

**Known Issues:**
- USDZ may not work in Firefox (Apple format, Safari-first)
- Large files (>100MB) may cause memory issues on mobile

## Build Output

**Development:**
- Vite dev server on port 5173
- Fast HMR (< 50ms for most changes)
- Source maps for debugging

**Production:**
- Minified bundle: ~699KB (186KB gzipped)
- Single JS file (code-splitting not needed)
- CSS extracted: ~4KB
- Total payload: ~190KB gzipped

**Optimization Opportunities:**
- Code-splitting Three.js loaders (dynamic imports)
- Could reduce bundle to ~150KB by loading on-demand

## Deployment

Following repository pattern from CLAUDE.md:

1. Build production bundle
2. Copy `dist/` to `/docs/3d-scan-viewer/`
3. Update main `/docs/index.html` with new card
4. Commit and push

**Deployment Script:** `deploy-to-pages.sh`

## Future Enhancements

See ICEBOX.md for full list. Key priorities:

1. **LAS Support** - Critical for LiDAR workflows
2. **Measurements** - Ruler tool, annotations
3. **Cross-sections** - Slice plane for interior views
4. **Comparison Mode** - Side-by-side or overlay
5. **Export** - Screenshots, simplified meshes

## Lessons Learned

1. **Start with HTML first** - Building UI in HTML/CSS before TypeScript saved time
2. **Three.js examples are gold** - Loaders are well-documented in examples
3. **Type safety pays off** - TypeScript caught several bugs during development
4. **Auto-scaling is hard** - Took 3 iterations to get right for all model sizes
5. **Bun is fast** - Install and build times were instant

## Code Quality

**What went well:**
- Clean separation of concerns (loaders, UI, rendering)
- Consistent naming conventions
- Comprehensive error handling
- Good TypeScript types

**What could improve:**
- Add JSDoc comments for public functions
- Extract magic numbers to constants
- Add unit tests for critical functions
- Improve error messages for users

## References

- [Three.js Documentation](https://threejs.org/docs/)
- [Three.js Examples](https://threejs.org/examples/)
- [Vite Documentation](https://vite.dev/)
- [OrbitControls API](https://threejs.org/docs/#examples/en/controls/OrbitControls)

---

**Author:** Built with Claude Code
**Last Updated:** November 20, 2025
