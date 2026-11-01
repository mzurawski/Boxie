import json
import os
import math

def process_erp_import(json_path):
    with open(json_path) as f:
        data = json.load(f)

    gen = data["generator"]
    mat = data["material_specification"]

    Lg = gen["length_mm"]
    Wg = gen["width_mm"]
    Hg = gen["height_mm"]
    Tw = mat["panel_thickness_mm"]
    Tins = mat["lining_thickness_mm"]

    Cmin = 75.0
    Cex = 150.0
    Lbaffle_intake = 120.0
    Lbaffle_exhaust = 140.0
    Hisolator = 45.0
    Hduct = 30.0
    Hcaster = 30.0

    Lint = Lg + 2 * Cmin + Lbaffle_intake + Lbaffle_exhaust
    Wint = Wg + 2 * Cmin
    Hint = Hg + Cmin + Hisolator + Hduct

    Lext = Lint + 2 * (Tw + Tins)
    Wext = Wint + 2 * (Tw + Tins)
    Hext = Hint + 2 * (Tw + Tins) + Hcaster

    return {
        "job": data["work_order"],
        "part_number": data["part_number"],
        "material": mat["core_material"],
        "panel_thickness_mm": Tw,
        "foam_thickness_mm": Tins,
        "generator_model": gen["make_model"],
        "generator_dims": {"L": Lg, "W": Wg, "H": Hg},
        "internal_dims": {"L": round(Lint, 1), "W": round(Wint, 1), "H": round(Hint, 1)},
        "external_dims": {"L": round(Lext, 1), "W": round(Wext, 1), "H": round(Hext, 1)},
    }

def generate_interactive_3d_html(calc, output_path):
    L = calc["external_dims"]["L"] / 10.0 # scale to cm for 3d display
    W = calc["external_dims"]["W"] / 10.0
    H = calc["external_dims"]["H"] / 10.0

    gL = calc["generator_dims"]["L"] / 10.0
    gW = calc["generator_dims"]["W"] / 10.0
    gH = calc["generator_dims"]["H"] / 10.0

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Boxie 3D Viewer - {calc['job']} ({calc['material']})</title>
  <style>
    body {{ margin: 0; padding: 0; background: #1e1e24; color: #fff; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; overflow: hidden; }}
    #header {{ position: absolute; top: 16px; left: 16px; z-index: 100; background: rgba(20, 20, 28, 0.85); backdrop-filter: blur(8px); padding: 16px 20px; border-radius: 8px; border: 1px solid #333; }}
    #header h1 {{ margin: 0 0 6px 0; font-size: 18px; color: #4ade80; }}
    #header p {{ margin: 3px 0; font-size: 13px; color: #cbd5e1; }}
    #controls {{ position: absolute; bottom: 16px; left: 16px; z-index: 100; background: rgba(20, 20, 28, 0.85); padding: 12px 18px; border-radius: 8px; font-size: 13px; color: #94a3b8; }}
    #canvas-container {{ width: 100vw; height: 100vh; display: block; }}
  </style>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
</head>
<body>
  <div id="header">
    <h1>Boxie 3D Viewer — {calc['job']}</h1>
    <p><strong>Part:</strong> {calc['part_number']} | <strong>Material:</strong> {calc['material']} ({calc['panel_thickness_mm']}mm)</p>
    <p><strong>Outer Envelope:</strong> {calc['external_dims']['L']}mm × {calc['external_dims']['W']}mm × {calc['external_dims']['H']}mm</p>
    <p><strong>Generator:</strong> {calc['generator_model']} ({calc['generator_dims']['L']} × {calc['generator_dims']['W']} × {calc['generator_dims']['H']} mm)</p>
  </div>
  <div id="controls">
    Rotate: Left-Click + Drag &nbsp;|&nbsp; Pan: Right-Click + Drag &nbsp;|&nbsp; Zoom: Scroll Wheel
  </div>
  <div id="canvas-container"></div>

  <script>
    const container = document.getElementById('canvas-container');
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x18181b);
    scene.fog = new THREE.FogExp2(0x18181b, 0.003);

    const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 2000);
    camera.position.set(160, 120, 180);

    const renderer = new THREE.WebGLRenderer({{ antialias: true }});
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.shadowMap.enabled = true;
    container.appendChild(renderer.domElement);

    const controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;

    // Lighting
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
    scene.add(ambientLight);
    const dirLight = new THREE.DirectionalLight(0xffffff, 0.8);
    dirLight.position.set(150, 200, 100);
    dirLight.castShadow = true;
    scene.add(dirLight);

    // Floor Grid
    const grid = new THREE.GridHelper(400, 40, 0x3f3f46, 0x27272a);
    grid.position.y = 0;
    scene.add(grid);

    // Main Box Group
    const boxGroup = new THREE.Group();
    scene.add(boxGroup);

    // Outer Enclosure (Transparent Wood or Metal)
    const boxGeo = new THREE.BoxGeometry({L}, {H}, {W});
    const boxMat = new THREE.MeshStandardMaterial({{
      color: 0xc29b68, // Wood Baltic Birch hue
      roughness: 0.6,
      metalness: 0.1,
      transparent: true,
      opacity: 0.45,
      wireframe: false
    }});
    const outerBox = new THREE.Mesh(boxGeo, boxMat);
    outerBox.position.y = {H} / 2 + 3.0; // elevated on wheels
    boxGroup.add(outerBox);

    // Outer Box Wireframe Outline
    const wireGeo = new THREE.EdgesGeometry(boxGeo);
    const wireMat = new THREE.LineBasicMaterial({{ color: 0x4ade80, linewidth: 2 }});
    const wireframe = new THREE.LineSegments(wireGeo, wireMat);
    wireframe.position.y = outerBox.position.y;
    boxGroup.add(wireframe);

    // Generator Unit (Core Block inside)
    const genGeo = new THREE.BoxGeometry({gL}, {gH}, {gW});
    const genMat = new THREE.MeshStandardMaterial({{
      color: 0xd93829, // Honda Red
      roughness: 0.3,
      metalness: 0.4
    }});
    const genMesh = new THREE.Mesh(genGeo, genMat);
    genMesh.position.set(5.0, {gH}/2 + 5.0, 0);
    boxGroup.add(genMesh);

    // Acoustic Maze Baffles
    const baffleMat = new THREE.MeshStandardMaterial({{ color: 0x38bdf8, roughness: 0.4 }});
    const b1 = new THREE.Mesh(new THREE.BoxGeometry(1.8, {H} * 0.7, {W} * 0.75), baffleMat);
    b1.position.set(-{L}/2 + 10.0, {H}/2 + 3.0, -{W} * 0.1);
    boxGroup.add(b1);
    const b2 = new THREE.Mesh(new THREE.BoxGeometry(1.8, {H} * 0.7, {W} * 0.75), baffleMat);
    b2.position.set(-{L}/2 + 18.0, {H}/2 + 3.0, {W} * 0.1);
    boxGroup.add(b2);

    // Exhaust Heat Shield & Flange
    const shieldMat = new THREE.MeshStandardMaterial({{ color: 0xf43f5e, metalness: 0.8, roughness: 0.2 }});
    const shield = new THREE.Mesh(new THREE.BoxGeometry(2.0, 18.0, 18.0), shieldMat);
    shield.position.set({L}/2 - 3.0, {H}/2 + 6.0, 0);
    boxGroup.add(shield);

    // Wheels
    const wheelGeo = new THREE.CylinderGeometry(7.5, 7.5, 4.0, 24);
    const wheelMat = new THREE.MeshStandardMaterial({{ color: 0x111827, roughness: 0.8 }});
    const wheel1 = new THREE.Mesh(wheelGeo, wheelMat);
    wheel1.rotation.x = Math.PI / 2;
    wheel1.position.set({L}/2 - 10.0, 7.5, {W}/2 + 2.0);
    boxGroup.add(wheel1);
    const wheel2 = wheel1.clone();
    wheel2.position.z = -{W}/2 - 2.0;
    boxGroup.add(wheel2);

    // Fold Handle
    const handleMat = new THREE.MeshStandardMaterial({{ color: 0x94a3b8, metalness: 0.7 }});
    const handle = new THREE.Mesh(new THREE.BoxGeometry(2.0, 4.0, {W} * 0.6), handleMat);
    handle.position.set(-{L}/2 - 3.0, {H} * 0.75, 0);
    boxGroup.add(handle);

    // Animation Loop
    function animate() {{
      requestAnimationFrame(animate);
      controls.update();
      renderer.render(scene, camera);
    }}
    animate();

    window.addEventListener('resize', () => {{
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    }});
  </script>
</body>
</html>
"""
    with open(output_path, "w") as f:
        f.write(html_content)
    print(f"Generated 3D Viewer at {output_path}")

if __name__ == "__main__":
    calc = process_erp_import("examples/erp_import_wo_8841_plywood.json")
    print("Processed ERP Work Order:")
    print(json.dumps(calc, indent=2))
    generate_interactive_3d_html(calc, "docs/enclosure_3d_viewer.html")
