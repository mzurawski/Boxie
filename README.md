# Boxie — Parametric Portable Generator Enclosure

Boxie is a parametric, sound-attenuating, thermally managed portable generator enclosure designed for drafting and fabrication in **AutoCAD** and automated CNC manufacturing workflows.

For maintenance workflows and agent instructions, see [`AGENTS.md`](./AGENTS.md) (or [`agents.md`](./agents.md)).
For the complete engineering specifications, AutoCAD formulation equations, and Requirements Traceability Matrix, see [`REQUIREMENTS.md`](./REQUIREMENTS.md).

---

## 1. System Pipeline Overview

```
+------------------------------------+        +---------------------------+        +---------------------------+
| Global Shop Solutions (GSS) ERP    |        | Parametric Formulator     |        | AutoCAD / Fabrication     |
| - Work Order / Part Master Import  | =====> | - Calculates Clearances   | =====> | - AIA Layer Generation    |
| - Dimensions, Materials & Options  |        | - Sizes Acoustic Baffles  |        | - Closed CNC Polylines    |
| (REQ-INT-01 / INT-02)              |        | - Heat Shield Stand-off   |        | - Reconciled Cut-List BOM |
+------------------------------------+        +---------------------------+        +---------------------------+
```

---

## 2. Visual Design Views (Generated from Requirements)

The diagrams below represent the enclosure layout, airflow pathways, dimensions, and sub-assemblies derived from the specifications in `REQUIREMENTS.md`.

### 2.1 Isometric View & Sub-Assembly Layout

```
                  +==============================================+
                 /  [Hinged Service Lid w/ Gas Struts]          /|
                /   (REQ-PHY-06)                               / |
               +==============================================+  |
               |                                              |  |
  [Air Intake  |  +------------------------+                  |  | [Dual High-Flow
   Louvered    |  |                        |                  |  |  Cooling Exhaust
   Hood]       |  |  Acoustic Maze Chamber |                  |  |  & Muffler Port]
   (REQ-SAF-04)|  |  (REQ-ACO-03)          |                  |  |  (REQ-THM-01/03)
      |        |  +------------------------+                  |  |     |
     [v]       |              |                               |  |    [v]
    +-----+    |              v                               |  |  +======+
    | / / |    |   +------------------------------------+     |  |  | ()(} |
    |/ / /|    |   |     GENERATOR CENTRAL BAY          |     |  |  | ()(} |
    +-----+    |   |                                    |     |  +--+======+
       |       |   |   +----------------------------+   |     | /  (Upper Hot Air
  (Cool Air    |   |   |  Portable Generator Unit   |   |     |/    Discharge)
   Enters      |   |   |  (up to 650x480x520 mm)    |   |     /
   Low)        |   |   +----------------------------+   |    /
               |   +------------------------------------+   /
 [Fold-down    |        | (4x Shore 50A Dampers REQ-ACO-04)|
  Handle] ===O |   =====+===============================+===
 (REQ-PHY-05)  |   | [M-ELEC-PORT] Weatherproof Cable   |
               |   | Pass-Through Grommet (REQ-SAF-01)  |
               +---+------------------------------------+---O  [Heavy-Duty Axle
                   \    \______________________________/   /   & All-Terrain
                    \   Front Removable Service Panel  /    Wheels Ø150mm]
                     \  (REQ-PHY-06)                  /     (REQ-PHY-05)
                      +------------------------------+
```

---

### 2.2 Longitudinal Section & Airflow View (Side Elevation)

Demonstrating compliance with **REQ-THM-01**, **REQ-THM-02**, **REQ-ACO-02**, and **REQ-ACO-03**:

```
                       <- L_ext = 1000 mm (REQ-PHY-03) ->
       +====================================================================+  ^
       || [Top Lid Panel: 18mm Plywood / 25mm Foam Lining] (REQ-ACO-02)   ||  |
       ||==================================================================||  |
   AIR || [Intake Maze]        |          MAIN GENERATOR BAY       | [Exh] ||  |
   IN  ||                      |                                   |  HOT  ||  |
  ===> ||  |\  (Acoustic       |   +---------------------------+   |  AIR  ||  |
       ||  | \  Baffle Maze)   |   | Engine Air Intake / Tank  |   |  OUT  || H_ext
       ||  |  \ (REQ-ACO-03)   |   +---------------------------+   | ====> ||  =
       ||  |   \               |   |                           |   | [Fan] || 750 mm
       ||  |    \   [Air Flow] |   |   Portable Generator      |   | [200  || (REQ-PHY-03)
       ||  +-----+  ========>  |   |   Core Bay                |   |  CFM] ||  |
       ||  | Fan |             |   +---------------------------+   |       ||  |
       ||  +-----+             |   | [Muffler] ===[Decoupled]=====>| [Exh] ||  |
       ||                      |   +---------------------------+   | [Tip] ||  |
       ||==================================================================||  |
       || [Vibration Isolated Floating Bed] (REQ-ACO-04)                   ||  |
       +====================================================================+  v
          (O) [Front Skid]                             [Rear Wheel Ø150] (O)
```

---

### 2.3 Plan View / Internal Component Layout (Top-Down Cross Section)

Demonstrating compliance with **REQ-PHY-01** (clearances), **REQ-SAF-01**, and **REQ-CAD-02** (layer mapping):

```
+----------------------------------- L_ext = 1000 mm -----------------------------------+
|  ACOUSTIC INTAKE CHAMBER |              MAIN EQUIPMENT BAY               | EXHAUST PLENUM  |
|  (Layer: M-VENT-INTK)    |              (Layer: M-ENCL-PVIS)             | (M-VENT-EXHT)   |
|--------------------------+-----------------------------------------------+-----------------|
|                          | <-------- Clear Width W_int = 630 mm -------> |                 |
| [Fresh Air Louvers]      |                                               | [Active Exhaust |
|  - Downward 45°          |   +---------------------------------------+   |  Fans: 2x120mm] |
|  - IP44 Mesh             |   |  GENERATOR CLEARANCE ENVELOPE         |   |                 |
|  (REQ-SAF-04)            |   |  L_g: 650 mm, W_g: 480 mm             |   | [Ceramic Fiber  |
|                          |   |  (REQ-PHY-01)                         |   |  Heat Shield    |
|   +----+  +----+         |   |                                       |   |  T=10mm]        |
|   |    |  |    |         |   |   +-------------------------------+   |   | (REQ-THM-03)    |
|   | B1 |  | B2 |  ====>  |   |   |   Portable Generator Body     |   |   |                 |
|   |    |  |    | Airflow |   |   |                               |===|===|==> Muffler      |
|   +----+  +----+         |   |   +-------------------------------+   |   |    Exit Pipe    |
|   (Dual Sound Baffles    |   |                                       |   |                 |
|    REQ-ACO-03)           |   +---------------------------------------+   |                 |
|                          |                                               |                 |
| [CO Alarm Monitor]       |   [C_min = 75mm]              [C_ex = 150mm]  | [Thermal Cutoff |
| (REQ-SAF-02)             |   (REQ-PHY-01)                (REQ-PHY-02)    |  Switch: 50°C]  |
|--------------------------+-----------------------------------------------+-----------------|
| [Pass-Through Port Ø75]  | Exterior Wall: 18mm Plywood + 25mm Foam       | [M8 Ground Lug] |
| (Layer: M-ELEC-PORT)     | (Layer: M-ENCL-PVIS / M-ENCL-INSL)            | (REQ-SAF-03)    |
+-------------------------------------------------------------------------------------------+
```

---

## 3. Dimensional & Design Summary Table

| Attribute | Specification | Traceability ID | Description |
| :--- | :--- | :--- | :--- |
| **External Envelope** | $1000\text{ mm (L)} \times 700\text{ mm (W)} \times 750\text{ mm (H)}$ | `REQ-PHY-03` | Sized to clear standard doorways and truck beds |
| **Max Generator Size**| $650\text{ mm (L)} \times 480\text{ mm (W)} \times 520\text{ mm (H)}$ | `REQ-PHY-01` | Accommodates 2000W - 4500W inverter & frame units |
| **Clearance Margins** | Side/Top: $75\text{ mm}$, Exhaust: $150\text{ mm}$ | `REQ-PHY-01`, `02` | Ensures cooling airflow and prevents hotspot ignition |
| **Wall Construction** | $18\text{ mm}$ Baltic birch plywood or $2.5\text{ mm}$ 5052 alum | `REQ-PHY-04` | High density, structural rigidity for acoustic mass |
| **Sound Insulation**  | $25\text{ mm}$ Class 1 / UL 94 HF-1 foam + MLV barrier | `REQ-ACO-02` | Absorbs airborne engine drone & mechanical noise |
| **Acoustic Rating**   | $\ge 18\text{ dBA}$ reduction at $7\text{ m}$ ($< 58\text{ dBA}$) | `REQ-ACO-01` | Neighborhood & campsite quiet compliance |
| **Cooling Airflow**   | $200\text{ CFM}$ active forced ventilation | `REQ-THM-01`, `02` | Dual 120mm high-static-pressure fans ($<15^\circ\text{C}$ rise) |
| **Mobility Hardware** | Dual $\varnothing 150\text{ mm}$ wheels + fold-down handle | `REQ-PHY-05` | Single-operator rolling on rough terrain |
| **Safety Features**   | IP55 brush port, CO alarm, M8 ground lug | `REQ-SAF-01..04` | Weatherproofing, electrical safety & gas safety |
| **Data Interfacing**  | Structured work orders, extraction & cut-list BOM | `REQ-INT-01..03` | Automated job ingestion & reconciled inventory BOM |

---

## 4. AutoCAD Layer Organization

The box model elements map directly to AutoCAD drawing layers:

| Layer Name | Color | Linetype | Content / Features |
| :--- | :--- | :--- | :--- |
| `M-ENCL-PVIS` | 7 (White) | Continuous | Exterior panels, chassis frame, lid boundary |
| `M-ENCL-INSL` | 2 (Yellow) | Hidden2 | 25mm acoustic foam lining & MLV backing boundaries |
| `M-VENT-INTK` | 4 (Cyan) | Continuous | Intake louvers, baffle plates, intake fan mounting |
| `M-VENT-EXHT` | 1 (Red) | Continuous | Exhaust heat cowl, muffler flange, exhaust baffles |
| `M-HARD-ACCS` | 3 (Green) | Continuous | Wheels, axle, folding handle, gas struts, latches |
| `M-ELEC-PORT` | 6 (Magenta)| Continuous | Brush cable pass-through, grounding terminal, CO mount |
| `G-ANNO-DIMS` | 8 (Gray) | Continuous | Dual dimensions (mm [in]) per `REQ-CAD-04` |
| `G-ANNO-TEXT` | 7 (White) | Continuous | Engineering notes, title block, material callouts |

---

## 5. Fabrication & Usage Instructions

1. **AutoCAD Generation**:
   - Ingest job record or run the parametric LISP script (`GEN_BOXIE`) with generator dimensions $(L_g, W_g, H_g)$.
   - Verify geometry against `REQUIREMENTS.md`.
2. **CNC Cutting**:
   - Export layers `M-ENCL-PVIS` and `M-VENT-INTK` to DXF.
   - Cut outer walls using an $18\text{ mm}$ sheet on CNC router with $0.2\text{ mm}$ kerf allowance.
3. **Assembly & Sealing**:
   - Assemble outer panels using pocket screws and polyurethane glue.
   - Adhere $25\text{ mm}$ acoustic foam to inner walls using heat-resistant contact adhesive.
   - Mount vibration isolators, intake/exhaust fans, and electrical pass-through port.
4. **Operation**:
   - Place generator onto isolated baseplate.
   - Attach flexible exhaust tube to exterior muffler port.
   - Plug cooling fans into generator accessory outlet or 12V auxiliary power.
   - Route extension cords through the brush grommet and latch the lid before starting.
