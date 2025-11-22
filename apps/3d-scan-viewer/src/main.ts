import './style.css'
import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js'
import { TransformControls } from 'three/examples/jsm/controls/TransformControls.js'
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js'
import { FBXLoader } from 'three/examples/jsm/loaders/FBXLoader.js'
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader.js'
import { PLYLoader } from 'three/examples/jsm/loaders/PLYLoader.js'
import { USDZLoader } from 'three/examples/jsm/loaders/USDZLoader.js'
import { GLTFExporter } from 'three/examples/jsm/exporters/GLTFExporter.js'

// Types
type ObjectType = 'wall' | 'floor' | 'furniture' | 'virtual-furniture' | 'unknown'

interface ClassifiedObject {
  object: THREE.Object3D
  type: ObjectType
  name: string
  originalMaterial?: THREE.Material | THREE.Material[]
}

// State
let scene: THREE.Scene
let camera: THREE.PerspectiveCamera
let renderer: THREE.WebGLRenderer
let orbitControls: OrbitControls
let transformControls: TransformControls
let raycaster: THREE.Raycaster
let mouse: THREE.Vector2

let currentModel: THREE.Object3D | null = null
let classifiedObjects: ClassifiedObject[] = []
let selectedObject: ClassifiedObject | null = null
let gridHelper: THREE.GridHelper

let isEditMode = false
let virtualFurniture: THREE.Mesh[] = []

// UI Elements
const canvas = document.getElementById('canvas') as HTMLCanvasElement
const fileInput = document.getElementById('fileInput') as HTMLInputElement
const uploadArea = document.querySelector('.file-upload-area') as HTMLDivElement
const loadingIndicator = document.getElementById('loadingIndicator') as HTMLDivElement
const formatInfo = document.getElementById('formatInfo') as HTMLSpanElement
const objectsInfo = document.getElementById('objectsInfo') as HTMLSpanElement
const selectedInfo = document.getElementById('selectedInfo') as HTMLSpanElement

// Mode buttons
const viewModeBtn = document.getElementById('viewMode') as HTMLButtonElement
const editModeBtn = document.getElementById('editMode') as HTMLButtonElement
const editToolsPanel = document.getElementById('editToolsPanel') as HTMLDivElement

// Control buttons
const resetCameraBtn = document.getElementById('resetCamera') as HTMLButtonElement
const toggleGridBtn = document.getElementById('toggleGrid') as HTMLButtonElement

// Edit tool buttons
const deleteObjectBtn = document.getElementById('deleteObject') as HTMLButtonElement
const hideObjectBtn = document.getElementById('hideObject') as HTMLButtonElement
const paintWallBtn = document.getElementById('paintWall') as HTMLButtonElement
const wallColorInput = document.getElementById('wallColor') as HTMLInputElement
const addFurnitureBtn = document.getElementById('addFurniture') as HTMLButtonElement
const exportUSDZBtn = document.getElementById('exportUSDZ') as HTMLButtonElement

// Furniture dimension inputs
const furnitureWidthInput = document.getElementById('furnitureWidth') as HTMLInputElement
const furnitureDepthInput = document.getElementById('furnitureDepth') as HTMLInputElement
const furnitureHeightInput = document.getElementById('furnitureHeight') as HTMLInputElement

// Selection indicator
const selectionIndicator = document.getElementById('selectionIndicator') as HTMLDivElement
const selectionName = document.getElementById('selectionName') as HTMLElement
const selectionType = document.getElementById('selectionType') as HTMLElement

// Initialize Three.js scene
function initScene() {
  // Scene
  scene = new THREE.Scene()
  scene.background = new THREE.Color(0x0f0f0f)
  scene.fog = new THREE.Fog(0x0f0f0f, 50, 200)

  // Camera
  camera = new THREE.PerspectiveCamera(
    50,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
  )
  camera.position.set(5, 5, 5)

  // Renderer
  renderer = new THREE.WebGLRenderer({
    canvas,
    antialias: true,
    alpha: true
  })
  renderer.setSize(window.innerWidth, window.innerHeight)
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
  renderer.shadowMap.enabled = true
  renderer.shadowMap.type = THREE.PCFSoftShadowMap
  renderer.toneMapping = THREE.ACESFilmicToneMapping
  renderer.toneMappingExposure = 1.0

  // Orbit Controls
  orbitControls = new OrbitControls(camera, renderer.domElement)
  orbitControls.enableDamping = true
  orbitControls.dampingFactor = 0.05
  orbitControls.screenSpacePanning = false
  orbitControls.minDistance = 1
  orbitControls.maxDistance = 100
  orbitControls.maxPolarAngle = Math.PI

  // Transform Controls (for furniture manipulation)
  transformControls = new TransformControls(camera, renderer.domElement)
  transformControls.addEventListener('dragging-changed', (event) => {
    orbitControls.enabled = !event.value
  })
  scene.add(transformControls as any) // TransformControls extends Object3D

  // Raycaster for selection
  raycaster = new THREE.Raycaster()
  mouse = new THREE.Vector2()

  // Lights
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.6)
  scene.add(ambientLight)

  const directionalLight = new THREE.DirectionalLight(0xffffff, 1.0)
  directionalLight.position.set(5, 10, 7.5)
  directionalLight.castShadow = true
  directionalLight.shadow.camera.near = 0.5
  directionalLight.shadow.camera.far = 50
  directionalLight.shadow.camera.left = -10
  directionalLight.shadow.camera.right = 10
  directionalLight.shadow.camera.top = 10
  directionalLight.shadow.camera.bottom = -10
  directionalLight.shadow.mapSize.width = 2048
  directionalLight.shadow.mapSize.height = 2048
  scene.add(directionalLight)

  const hemisphereLight = new THREE.HemisphereLight(0xffffff, 0x444444, 0.5)
  hemisphereLight.position.set(0, 20, 0)
  scene.add(hemisphereLight)

  // Grid
  gridHelper = new THREE.GridHelper(20, 20, 0x444444, 0x222222)
  scene.add(gridHelper)

  // Event listeners
  window.addEventListener('resize', onWindowResize)
  canvas.addEventListener('click', onCanvasClick)
  window.addEventListener('keydown', onKeyDown)

  // Start animation loop
  animate()
}

// Animation loop
function animate() {
  requestAnimationFrame(animate)
  orbitControls.update()
  renderer.render(scene, camera)
}

// Handle window resize
function onWindowResize() {
  const container = document.getElementById('canvasContainer')
  if (!container) return

  const width = container.clientWidth
  const height = container.clientHeight

  camera.aspect = width / height
  camera.updateProjectionMatrix()
  renderer.setSize(width, height)
}

// Handle canvas click for object selection
function onCanvasClick(event: MouseEvent) {
  if (!isEditMode || !currentModel) return

  const container = document.getElementById('canvasContainer')
  if (!container) return

  const rect = container.getBoundingClientRect()
  mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1
  mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1

  raycaster.setFromCamera(mouse, camera)

  // Create array of selectable objects
  const selectableObjects: THREE.Object3D[] = []
  classifiedObjects.forEach(co => selectableObjects.push(co.object))
  virtualFurniture.forEach(vf => selectableObjects.push(vf))

  const intersects = raycaster.intersectObjects(selectableObjects, true)

  if (intersects.length > 0) {
    // Find the classified object or virtual furniture
    let foundObject = intersects[0].object

    // Traverse up to find the root object
    while (foundObject.parent && foundObject.parent !== scene && foundObject.parent !== currentModel) {
      foundObject = foundObject.parent
    }

    // Find in classified objects
    const classified = classifiedObjects.find(co =>
      co.object === foundObject || co.object.children.includes(foundObject as any)
    )

    if (classified) {
      selectObject(classified)
    } else if (virtualFurniture.includes(foundObject as THREE.Mesh)) {
      // Virtual furniture selected
      selectVirtualFurniture(foundObject as THREE.Mesh)
    }
  } else {
    deselectObject()
  }
}

// Handle keyboard shortcuts
function onKeyDown(event: KeyboardEvent) {
  if (event.key === 'Escape') {
    deselectObject()
  } else if (event.key === 'Delete' || event.key === 'Backspace') {
    if (selectedObject && isEditMode) {
      event.preventDefault()
      deleteSelectedObject()
    }
  } else if (isEditMode && selectedObject && selectedObject.type === 'virtual-furniture') {
    // Transform controls shortcuts
    if (event.key.toLowerCase() === 't') {
      transformControls.setMode('translate')
    } else if (event.key.toLowerCase() === 'r') {
      transformControls.setMode('rotate')
    } else if (event.key.toLowerCase() === 's') {
      transformControls.setMode('scale')
    }
  }
}

// Load file
async function loadFile(file: File) {
  showLoading(true)

  // Clear previous model
  if (currentModel) {
    scene.remove(currentModel)
    currentModel = null
  }
  classifiedObjects = []
  virtualFurniture = []
  deselectObject()

  const extension = file.name.split('.').pop()?.toLowerCase()
  const url = URL.createObjectURL(file)

  try {
    let object: THREE.Object3D | null = null

    switch (extension) {
      case 'glb':
      case 'gltf':
        object = await loadGLTF(url)
        break
      case 'fbx':
        object = await loadFBX(url)
        break
      case 'obj':
        object = await loadOBJ(url)
        break
      case 'ply':
        object = await loadPLY(url)
        break
      case 'usdz':
        object = await loadUSDZ(url)
        break
      default:
        throw new Error(`Unsupported file format: ${extension}`)
    }

    if (object) {
      currentModel = object
      scene.add(object)

      // Classify objects (especially for USDZ from RoomPlanner)
      classifyObjects(object)

      // Center and scale the model
      centerAndScaleModel(object)

      // Update info
      formatInfo.textContent = extension?.toUpperCase() || 'UNKNOWN'
      objectsInfo.textContent = classifiedObjects.length.toString()
      selectedInfo.textContent = 'None'

      // Enable export if we have a model
      exportUSDZBtn.disabled = false

      // Reset camera
      resetCamera()
    }
  } catch (error) {
    console.error('Error loading file:', error)
    alert(`Error loading file: ${error instanceof Error ? error.message : 'Unknown error'}`)
  } finally {
    URL.revokeObjectURL(url)
    showLoading(false)
  }
}

// GLTF/GLB Loader
function loadGLTF(url: string): Promise<THREE.Object3D> {
  return new Promise((resolve, reject) => {
    const loader = new GLTFLoader()
    loader.load(
      url,
      (gltf) => resolve(gltf.scene),
      undefined,
      reject
    )
  })
}

// FBX Loader
function loadFBX(url: string): Promise<THREE.Object3D> {
  return new Promise((resolve, reject) => {
    const loader = new FBXLoader()
    loader.load(url, resolve, undefined, reject)
  })
}

// OBJ Loader
function loadOBJ(url: string): Promise<THREE.Object3D> {
  return new Promise((resolve, reject) => {
    const loader = new OBJLoader()
    loader.load(url, resolve, undefined, reject)
  })
}

// PLY Loader (Point Cloud)
function loadPLY(url: string): Promise<THREE.Object3D> {
  return new Promise((resolve, reject) => {
    const loader = new PLYLoader()
    loader.load(
      url,
      (geometry) => {
        geometry.computeVertexNormals()

        const hasColors = geometry.attributes.color !== undefined

        const material = new THREE.PointsMaterial({
          size: 0.02,
          vertexColors: hasColors,
          color: hasColors ? undefined : 0x888888,
          sizeAttenuation: true
        })

        const mesh = new THREE.Points(geometry, material)
        resolve(mesh)
      },
      undefined,
      reject
    )
  })
}

// USDZ Loader
function loadUSDZ(url: string): Promise<THREE.Object3D> {
  return new Promise((resolve, reject) => {
    const loader = new USDZLoader()
    loader.load(url, resolve, undefined, reject)
  })
}

// Classify objects based on metadata/name
function classifyObjects(root: THREE.Object3D) {
  classifiedObjects = []

  root.traverse((child) => {
    if ((child as THREE.Mesh).isMesh) {
      const mesh = child as THREE.Mesh
      const name = mesh.name.toLowerCase()

      let type: ObjectType = 'unknown'

      // Classify based on name/metadata
      // RoomPlanner typically names objects as "wall", "floor", "furniture", etc.
      if (name.includes('wall')) {
        type = 'wall'
      } else if (name.includes('floor') || name.includes('ground')) {
        type = 'floor'
      } else if (name.includes('furniture') || name.includes('chair') ||
                 name.includes('table') || name.includes('sofa') ||
                 name.includes('bed') || name.includes('cabinet')) {
        type = 'furniture'
      } else {
        // Try to infer from geometry
        const geometry = mesh.geometry
        if (geometry) {
          geometry.computeBoundingBox()
          const bbox = geometry.boundingBox
          if (bbox) {
            const size = new THREE.Vector3()
            bbox.getSize(size)

            // Flat horizontal objects are likely floors
            if (size.y < 0.1 && size.x > 1 && size.z > 1) {
              type = 'floor'
            }
            // Tall thin objects are likely walls
            else if (size.y > 1 && (size.x < 0.3 || size.z < 0.3)) {
              type = 'wall'
            }
          }
        }
      }

      classifiedObjects.push({
        object: mesh,
        type,
        name: mesh.name || `Object ${classifiedObjects.length + 1}`,
        originalMaterial: mesh.material
      })
    }
  })

  console.log('Classified objects:', classifiedObjects)
}

// Center and scale model
function centerAndScaleModel(object: THREE.Object3D) {
  const box = new THREE.Box3().setFromObject(object)
  const center = box.getCenter(new THREE.Vector3())
  const size = box.getSize(new THREE.Vector3())

  // Center the model
  object.position.sub(center)

  // Scale to fit in view
  const maxDim = Math.max(size.x, size.y, size.z)
  const scale = 5 / maxDim
  object.scale.setScalar(scale)
}

// Select object
function selectObject(classified: ClassifiedObject) {
  // Deselect previous
  if (selectedObject) {
    unhighlightObject(selectedObject)
  }

  selectedObject = classified
  highlightObject(classified)

  // Update UI
  selectionName.textContent = classified.name
  selectionType.textContent = classified.type
  selectionType.className = `type-badge ${classified.type}`
  selectionIndicator.style.display = 'block'
  selectedInfo.textContent = classified.name

  // Enable/disable buttons based on selection
  deleteObjectBtn.disabled = classified.type === 'floor' // Don't allow deleting floor
  hideObjectBtn.disabled = classified.type === 'floor'
  paintWallBtn.disabled = classified.type !== 'wall'

  // Attach transform controls if it's virtual furniture
  if (classified.type === 'virtual-furniture') {
    transformControls.attach(classified.object)
    transformControls.setMode('translate')
  }
}

// Select virtual furniture
function selectVirtualFurniture(mesh: THREE.Mesh) {
  const classified: ClassifiedObject = {
    object: mesh,
    type: 'virtual-furniture',
    name: mesh.name || 'Virtual Furniture',
    originalMaterial: mesh.material
  }

  selectObject(classified)
}

// Deselect object
function deselectObject() {
  if (selectedObject) {
    unhighlightObject(selectedObject)
  }

  selectedObject = null
  selectionIndicator.style.display = 'none'
  selectedInfo.textContent = 'None'

  // Disable edit buttons
  deleteObjectBtn.disabled = true
  hideObjectBtn.disabled = true
  paintWallBtn.disabled = true

  // Detach transform controls
  transformControls.detach()
}

// Highlight object
function highlightObject(classified: ClassifiedObject) {
  const mesh = classified.object as THREE.Mesh

  if (mesh.material) {
    // Add emission for highlight effect
    if (Array.isArray(mesh.material)) {
      mesh.material.forEach(mat => {
        if (mat instanceof THREE.MeshStandardMaterial) {
          mat.emissive = new THREE.Color(0x646cff)
          mat.emissiveIntensity = 0.3
        }
      })
    } else if (mesh.material instanceof THREE.MeshStandardMaterial) {
      mesh.material.emissive = new THREE.Color(0x646cff)
      mesh.material.emissiveIntensity = 0.3
    }
  }
}

// Unhighlight object
function unhighlightObject(classified: ClassifiedObject) {
  const mesh = classified.object as THREE.Mesh

  if (mesh.material) {
    if (Array.isArray(mesh.material)) {
      mesh.material.forEach(mat => {
        if (mat instanceof THREE.MeshStandardMaterial) {
          mat.emissive = new THREE.Color(0x000000)
          mat.emissiveIntensity = 0
        }
      })
    } else if (mesh.material instanceof THREE.MeshStandardMaterial) {
      mesh.material.emissive = new THREE.Color(0x000000)
      mesh.material.emissiveIntensity = 0
    }
  }
}

// Delete selected object
function deleteSelectedObject() {
  if (!selectedObject || !currentModel) return

  // Remove from scene
  selectedObject.object.removeFromParent()

  // Remove from classified objects
  classifiedObjects = classifiedObjects.filter(co => co !== selectedObject)

  // Remove from virtual furniture if applicable
  if (selectedObject.type === 'virtual-furniture') {
    virtualFurniture = virtualFurniture.filter(vf => vf !== selectedObject!.object)
  }

  // Update UI
  objectsInfo.textContent = (classifiedObjects.length + virtualFurniture.length).toString()

  deselectObject()
}

// Hide selected object
function hideSelectedObject() {
  if (!selectedObject) return

  selectedObject.object.visible = false
  deselectObject()
}

// Paint selected wall
function paintSelectedWall() {
  if (!selectedObject || selectedObject.type !== 'wall') return

  const mesh = selectedObject.object as THREE.Mesh
  const color = wallColorInput.value

  // Create new material with the selected color
  const newMaterial = new THREE.MeshStandardMaterial({
    color: new THREE.Color(color),
    roughness: 0.8,
    metalness: 0.1
  })

  mesh.material = newMaterial
}

// Add virtual furniture
function addVirtualFurniture() {
  const width = parseFloat(furnitureWidthInput.value)
  const depth = parseFloat(furnitureDepthInput.value)
  const height = parseFloat(furnitureHeightInput.value)

  // Create a box geometry with the specified dimensions
  const geometry = new THREE.BoxGeometry(width, height, depth)
  const material = new THREE.MeshStandardMaterial({
    color: 0x888888,
    roughness: 0.7,
    metalness: 0.3,
    transparent: true,
    opacity: 0.8
  })

  const mesh = new THREE.Mesh(geometry, material)
  mesh.name = `Furniture ${virtualFurniture.length + 1} (${width}×${depth}×${height}m)`

  // Position at center, slightly above ground
  mesh.position.set(0, height / 2, 0)
  mesh.castShadow = true
  mesh.receiveShadow = true

  scene.add(mesh)
  virtualFurniture.push(mesh)

  // Add to classified objects
  const classified: ClassifiedObject = {
    object: mesh,
    type: 'virtual-furniture',
    name: mesh.name,
    originalMaterial: material
  }
  classifiedObjects.push(classified)

  // Update UI
  objectsInfo.textContent = (classifiedObjects.length).toString()

  // Select the new furniture
  selectObject(classified)
}

// Export to USDZ/GLB
async function exportScene() {
  if (!currentModel) return

  try {
    // Use GLTF exporter (more reliable than USDZ export)
    const exporter = new GLTFExporter()

    exporter.parse(
      scene,
      (result) => {
        const output = JSON.stringify(result, null, 2)
        const blob = new Blob([output], { type: 'application/json' })
        const url = URL.createObjectURL(blob)

        const link = document.createElement('a')
        link.href = url
        link.download = 'room-plan-modified.gltf'
        link.click()

        URL.revokeObjectURL(url)
      },
      (error) => {
        console.error('Export error:', error)
        alert('Error exporting scene')
      },
      { binary: false }
    )
  } catch (error) {
    console.error('Export error:', error)
    alert('Error exporting scene')
  }
}

// Toggle between view and edit mode
function setMode(editMode: boolean) {
  isEditMode = editMode

  // Update UI
  if (editMode) {
    viewModeBtn.classList.remove('active')
    editModeBtn.classList.add('active')
    editToolsPanel.style.display = 'flex'
    orbitControls.enabled = true // Will be disabled when dragging transforms
  } else {
    viewModeBtn.classList.add('active')
    editModeBtn.classList.remove('active')
    editToolsPanel.style.display = 'none'
    orbitControls.enabled = true
    deselectObject()
  }
}

// Reset camera
function resetCamera() {
  if (!currentModel) return

  const box = new THREE.Box3().setFromObject(currentModel)
  const size = box.getSize(new THREE.Vector3())
  const maxDim = Math.max(size.x, size.y, size.z)

  const distance = maxDim * 1.5
  camera.position.set(distance, distance, distance)
  camera.lookAt(0, 0, 0)

  orbitControls.target.set(0, 0, 0)
  orbitControls.update()
}

// Toggle grid
function toggleGrid() {
  gridHelper.visible = !gridHelper.visible
  toggleGridBtn.classList.toggle('active', gridHelper.visible)
}

// Show/hide loading indicator
function showLoading(show: boolean) {
  if (show) {
    loadingIndicator.classList.add('active')
  } else {
    loadingIndicator.classList.remove('active')
  }
}

// Event Listeners

// File input
fileInput.addEventListener('change', (e) => {
  const file = (e.target as HTMLInputElement).files?.[0]
  if (file) {
    loadFile(file)
  }
})

// Drag and drop
uploadArea.addEventListener('dragover', (e) => {
  e.preventDefault()
  uploadArea.classList.add('drag-over')
})

uploadArea.addEventListener('dragleave', () => {
  uploadArea.classList.remove('drag-over')
})

uploadArea.addEventListener('drop', (e) => {
  e.preventDefault()
  uploadArea.classList.remove('drag-over')

  const file = e.dataTransfer?.files[0]
  if (file) {
    loadFile(file)
  }
})

// Mode toggle
viewModeBtn.addEventListener('click', () => setMode(false))
editModeBtn.addEventListener('click', () => setMode(true))

// Control buttons
resetCameraBtn.addEventListener('click', resetCamera)
toggleGridBtn.addEventListener('click', toggleGrid)

// Edit tool buttons
deleteObjectBtn.addEventListener('click', deleteSelectedObject)
hideObjectBtn.addEventListener('click', hideSelectedObject)
paintWallBtn.addEventListener('click', paintSelectedWall)
addFurnitureBtn.addEventListener('click', addVirtualFurniture)
exportUSDZBtn.addEventListener('click', exportScene)

// Furniture presets
document.querySelectorAll('.preset-btn').forEach(btn => {
  btn.addEventListener('click', (e) => {
    const target = e.target as HTMLButtonElement
    const width = parseFloat(target.dataset.w || '1')
    const depth = parseFloat(target.dataset.d || '1')
    const height = parseFloat(target.dataset.h || '1')

    furnitureWidthInput.value = width.toString()
    furnitureDepthInput.value = depth.toString()
    furnitureHeightInput.value = height.toString()
  })
})

// Initialize
initScene()
onWindowResize()

console.log('3D Room Planner initialized!')
