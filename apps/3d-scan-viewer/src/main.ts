import './style.css'
import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js'
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js'
import { FBXLoader } from 'three/examples/jsm/loaders/FBXLoader.js'
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader.js'
import { PLYLoader } from 'three/examples/jsm/loaders/PLYLoader.js'
import { USDZLoader } from 'three/examples/jsm/loaders/USDZLoader.js'

// State
let scene: THREE.Scene
let camera: THREE.PerspectiveCamera
let renderer: THREE.WebGLRenderer
let controls: OrbitControls
let currentModel: THREE.Object3D | null = null
let gridHelper: THREE.GridHelper
let isWireframe = false
let isPointsMode = false

// UI Elements
const canvas = document.getElementById('canvas') as HTMLCanvasElement
const fileInput = document.getElementById('fileInput') as HTMLInputElement
const uploadArea = document.querySelector('.file-upload-area') as HTMLDivElement
const loadingIndicator = document.getElementById('loadingIndicator') as HTMLDivElement
const formatInfo = document.getElementById('formatInfo') as HTMLSpanElement
const verticesInfo = document.getElementById('verticesInfo') as HTMLSpanElement
const facesInfo = document.getElementById('facesInfo') as HTMLSpanElement

// Control buttons
const resetCameraBtn = document.getElementById('resetCamera') as HTMLButtonElement
const toggleWireframeBtn = document.getElementById('toggleWireframe') as HTMLButtonElement
const toggleGridBtn = document.getElementById('toggleGrid') as HTMLButtonElement
const togglePointsBtn = document.getElementById('togglePoints') as HTMLButtonElement

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

  // Controls
  controls = new OrbitControls(camera, renderer.domElement)
  controls.enableDamping = true
  controls.dampingFactor = 0.05
  controls.screenSpacePanning = false
  controls.minDistance = 1
  controls.maxDistance = 100
  controls.maxPolarAngle = Math.PI

  // Lights
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.5)
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

  const hemisphereLight = new THREE.HemisphereLight(0xffffff, 0x444444, 0.6)
  hemisphereLight.position.set(0, 20, 0)
  scene.add(hemisphereLight)

  // Grid
  gridHelper = new THREE.GridHelper(20, 20, 0x444444, 0x222222)
  scene.add(gridHelper)

  // Handle window resize
  window.addEventListener('resize', onWindowResize)

  // Start animation loop
  animate()
}

// Animation loop
function animate() {
  requestAnimationFrame(animate)
  controls.update()
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

// Load file
async function loadFile(file: File) {
  showLoading(true)

  // Remove previous model
  if (currentModel) {
    scene.remove(currentModel)
    currentModel = null
  }

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
      case 'las':
        alert('LAS format support coming soon! Use PLY format for point clouds.')
        break
      default:
        throw new Error(`Unsupported file format: ${extension}`)
    }

    if (object) {
      currentModel = object
      scene.add(object)

      // Center and scale the model
      centerAndScaleModel(object)

      // Update info
      updateModelInfo(object, extension || 'unknown')

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

        // Check if it has colors
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

// Update model info
function updateModelInfo(object: THREE.Object3D, format: string) {
  let totalVertices = 0
  let totalFaces = 0

  object.traverse((child) => {
    if ((child as THREE.Mesh).isMesh || (child as THREE.Points).isPoints) {
      const geometry = (child as THREE.Mesh | THREE.Points).geometry
      if (geometry) {
        const positionAttribute = geometry.attributes.position
        if (positionAttribute) {
          totalVertices += positionAttribute.count
        }
        if (geometry.index) {
          totalFaces += geometry.index.count / 3
        } else if ((child as THREE.Mesh).isMesh) {
          totalFaces += positionAttribute.count / 3
        }
      }
    }
  })

  formatInfo.textContent = format.toUpperCase()
  verticesInfo.textContent = totalVertices.toLocaleString()
  facesInfo.textContent = totalFaces > 0 ? Math.floor(totalFaces).toLocaleString() : 'N/A'
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

  controls.target.set(0, 0, 0)
  controls.update()
}

// Toggle wireframe
function toggleWireframe() {
  if (!currentModel) return

  isWireframe = !isWireframe
  toggleWireframeBtn.classList.toggle('active', isWireframe)

  currentModel.traverse((child) => {
    if ((child as THREE.Mesh).isMesh) {
      const mesh = child as THREE.Mesh
      if (Array.isArray(mesh.material)) {
        mesh.material.forEach(mat => {
          if (mat instanceof THREE.MeshStandardMaterial ||
              mat instanceof THREE.MeshBasicMaterial) {
            mat.wireframe = isWireframe
          }
        })
      } else {
        const material = mesh.material as THREE.Material
        if (material instanceof THREE.MeshStandardMaterial ||
            material instanceof THREE.MeshBasicMaterial) {
          material.wireframe = isWireframe
        }
      }
    }
  })
}

// Toggle grid
function toggleGrid() {
  gridHelper.visible = !gridHelper.visible
  toggleGridBtn.classList.toggle('active', gridHelper.visible)
}

// Toggle points mode
function togglePoints() {
  if (!currentModel) return

  isPointsMode = !isPointsMode
  togglePointsBtn.classList.toggle('active', isPointsMode)

  currentModel.traverse((child) => {
    if ((child as THREE.Mesh).isMesh) {
      const mesh = child as THREE.Mesh
      const geometry = mesh.geometry

      if (isPointsMode) {
        // Convert to points
        const material = new THREE.PointsMaterial({
          size: 0.05,
          color: 0x888888,
          sizeAttenuation: true
        })
        const points = new THREE.Points(geometry, material)
        points.position.copy(mesh.position)
        points.rotation.copy(mesh.rotation)
        points.scale.copy(mesh.scale)

        // Store original mesh for restoration
        ;(points as any).originalMesh = mesh

        if (mesh.parent) {
          const parent = mesh.parent
          parent.remove(mesh)
          parent.add(points)
        }
      } else {
        // Restore original mesh (handled by reloading for simplicity)
        // In production, you'd store the original material
      }
    }
  })
}

// Show/hide loading indicator
function showLoading(show: boolean) {
  if (show) {
    loadingIndicator.classList.add('active')
  } else {
    loadingIndicator.classList.remove('active')
  }
}

// File input handler
fileInput.addEventListener('change', (e) => {
  const file = (e.target as HTMLInputElement).files?.[0]
  if (file) {
    loadFile(file)
  }
})

// Drag and drop handlers
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

// Control button handlers
resetCameraBtn.addEventListener('click', resetCamera)
toggleWireframeBtn.addEventListener('click', toggleWireframe)
toggleGridBtn.addEventListener('click', toggleGrid)
togglePointsBtn.addEventListener('click', togglePoints)

// Initialize
initScene()
onWindowResize() // Set initial size

console.log('3D Scan Viewer initialized!')
