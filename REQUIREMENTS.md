# REQUIREMENTS: Parametric Portable Generator Box ("Boxie")

This document specifies the functional, physical, acoustic, thermal, safety, input data interfacing, and CAD formulation requirements for the design and AutoCAD drafting of a portable generator enclosure box. It also includes the complete **Requirements Traceability Matrix (RTM)**.

---

## 1. System Requirements Specification

### 1.1 Physical & Geometric Requirements (PHY)

* **REQ-PHY-01 (Internal Envelope Clearance)**: The internal volume of the enclosure must accommodate portable inverter/open-frame generators up to $L_g = 650\text{ mm}$, $W_g = 480\text{ mm}$, $H_g = 520\text{ mm}$. A minimum air buffer clearance of $C_{\text{min}} = 75\text{ mm}$ must surround all sides (except exhaust).
* **REQ-PHY-02 (Exhaust Clearance)**: Minimum air buffer clearance on the engine exhaust face shall be $C_{\text{ex}} \ge 150\text{ mm}$ between the muffler tip and the enclosure inner heat shield wall.
* **REQ-PHY-03 (Outer Envelope)**: Overall external dimensions must not exceed $L_{\text{ext}} = 1000\text{ mm}$, $W_{\text{ext}} = 700\text{ mm}$, $H_{\text{ext}} = 750\text{ mm}$ to ensure fitment through standard doorways ($800\text{ mm}$) and truck beds.
* **REQ-PHY-04 (Wall Construction & Thickness)**: The box enclosure panels shall be constructed of rigid $T_{\text{wall}} = 18\text{ mm}$ exterior-grade Baltic birch plywood or $T_{\text{wall}} = 2.5\text{ mm}$ 5052-H32 aluminum sheet.
* **REQ-PHY-05 (Portability & Mobility)**: The enclosure must feature two $\varnothing 150\text{ mm}$ (6") heavy-duty all-terrain wheels on the rear axle and dual heavy-duty fold-down handles on the opposite end, supporting a gross loaded weight of up to $85\text{ kg}$.
* **REQ-PHY-06 (Service Access Panels)**: The enclosure must feature a gas-strut-supported hinged top lid for fueling/inspection and a removable or latched front panel for full access to the control panel and starter pull-cord.

### 1.2 Acoustic Requirements (ACO)

* **REQ-ACO-01 (Noise Attenuation)**: The enclosure must achieve at least $18\text{ dBA}$ sound attenuation at $7\text{ meters}$, reducing standard open generator noise ($\approx 72\text{--}76\text{ dBA}$) to below $58\text{ dBA}$.
* **REQ-ACO-02 (Acoustic Lining)**: All interior panel walls (intake chamber, main bay, roof) must be lined with $T_{\text{ins}} = 25\text{ mm}$ open-cell, flame-retardant sound absorption foam (Class 1 / UL 94 HF-1 compliant) with mass-loaded vinyl (MLV) barrier backing ($2.5\text{ kg/m}^2$).
* **REQ-ACO-03 (Baffle Silencing Chambers)**: Air intake and exhaust must pass through dual-turn S-bend acoustic maze baffles lined with sound-dampening material to prevent direct line-of-sight sound transmission.
* **REQ-ACO-04 (Vibration Isolation)**: The generator must rest on a decoupled floating baseplate with 4 elastomeric vibration isolation dampers (Shore 50A durometer, natural frequency $< 10\text{ Hz}$).

### 1.3 Thermal & Aerodynamic Requirements (THM)

* **REQ-THM-01 (Forced Cooling Ventilation)**: The enclosure must feature an active forced-air ventilation system delivering at least $200\text{ CFM}$ ($340\text{ m}^3\text{/h}$) airflow to limit internal ambient temperature rise to $\Delta T \le 15^\circ\text{C}$ above ambient at full generator load.
* **REQ-THM-02 (Intake/Exhaust Separation)**: Fresh air intake must be located at the lower front/side zone; hot engine exhaust and cooling exhaust must discharge through the upper opposite end to prevent thermal recirculation.
* **REQ-THM-03 (Exhaust Deflector & Thermal Shielding)**: An automotive-grade flexible silicone/stainless steel exhaust decoupling tube must direct muffler gases directly to an exterior galvanized/stainless steel exhaust port, backed by a ceramic fiber heat shield ($T \ge 10\text{ mm}$, rated to $650^\circ\text{C}$).
* **REQ-THM-04 (Over-temperature Protection)**: An integrated digital thermal switch must trigger secondary cooling boost fans if internal ambient temperature exceeds $50^\circ\text{C}$.

### 1.4 Electrical & Safety Requirements (SAF)

* **REQ-SAF-01 (Cable Pass-Through)**: Weatherproof IP55-rated brush-grommet cable pass-through port ($\varnothing 75\text{ mm}$) on the lateral side to route heavy-gauge extension cords without compromising sound sealing.
* **REQ-SAF-02 (Carbon Monoxide (CO) Mitigation)**: Dedicated mounting bracket for a battery-operated CO monitor with visual and audio alarm siren.
* **REQ-SAF-03 (Grounding Lug)**: External copper grounding terminal stud (M8 / 5/16") bonded directly to the internal generator ground chassis.
* **REQ-SAF-04 (Weatherproofing & Ingress)**: Louvered exterior air intakes angled at $45^\circ$ downward with fine mesh insect/water screens (IP44 equivalent) to prevent rain ingress during outdoor operation.

### 1.5 System Interfacing & Input Data Requirements (INT)

* **REQ-INT-01 (Global Shop Solutions ERP Interface)**: The program must interface with and import work order, part master, and Bill of Materials (BOM) records from **Global Shop Solutions (GSS) ERP** via standard integration interfaces (GSS ODBC database views, REST API endpoints, or structured XML/CSV work order exports) containing generator model, clearance requirements, inventory raw material stock codes, and customer configuration options.
* **REQ-INT-02 (Parametric Data Extraction)**: The system must automatically extract dimensional inputs ($L_g, W_g, H_g$), acoustic attenuation target, and material panel gauge from the inbound Global Shop Solutions job record to drive CAD generation without manual drafting re-entry.
* **REQ-INT-03 (BOM & Cut-List Reconciliation)**: Upon generating the AutoCAD box design, the program must output a reconciled fabrication cut-list (panel dimensions, cutouts, hardware part numbers) formatted to write back into Global Shop Solutions ERP inventory and routing modules.

### 1.6 AutoCAD Formulation & Scripting Requirements (CAD)

* **REQ-CAD-01 (Parametric Scripting Architecture)**: All enclosure geometry must be formulable via parametric AutoLISP / AutoCAD Script (`.scr`) commands taking generator dimensions $(L_g, W_g, H_g, T_{\text{wall}}, T_{\text{ins}})$ as input parameters.
* **REQ-CAD-02 (Layer Hierarchy & Standards)**: AutoCAD drawings must generate geometry on standardized layers according to AIA/ISO 13567 (`M-ENCL-PVIS`, `M-ENCL-INSL`, `M-VENT-INTK`, `M-VENT-EXHT`, `M-HARD-ACCS`, `M-ELEC-PORT`, `G-ANNO-DIMS`, `G-ANNO-TEXT`).
* **REQ-CAD-03 (Cutout & CNC Toolpath Compatibility)**: Panel cutouts (ventilation slots, fan cutouts, latch mortises, cable ports) must be output as closed lightweight 2D polylines (`LWPOLYLINE`) for direct CNC routing / laser cutting export.
* **REQ-CAD-04 (Dual-Dimension Callouts)**: Parametric drafting routines must automatically place associative linear dimensions with dual units (Metric mm [Imperial inches]).

---

## 2. Mathematical Formulation for AutoCAD Enclosure Generation

To Kraft the box in an automated program or AutoCAD script, the outer dimensions, internal chamber partitions, and cutout profiles are formulated as functions of the generator dimensions and input data:

### 2.1 Enclosure Sizing Formulation

Given generator envelope: $L_g, W_g, H_g$

$$\begin{aligned}
L_{\text{int}} &= L_g + 2 \cdot C_{\text{min}} + L_{\text{baffle\_intake}} + L_{\text{baffle\_exhaust}} \\
W_{\text{int}} &= W_g + 2 \cdot C_{\text{min}} \\
H_{\text{int}} &= H_g + C_{\text{min}} + H_{\text{isolator}} + H_{\text{roof\_duct}}
\end{aligned}$$

With default parameters:
- Minimum side clearance: $C_{\text{min}} = 75\text{ mm}$
- Exhaust clearance: $C_{\text{ex}} = 150\text{ mm}$
- Intake sound maze depth: $L_{\text{baffle\_intake}} = 120\text{ mm}$
- Exhaust sound maze depth: $L_{\text{baffle\_exhaust}} = 140\text{ mm}$
- Vibration isolator base height: $H_{\text{isolator}} = 45\text{ mm}$
- Wall panel thickness: $T_{\text{wall}} = 18\text{ mm}$
- Acoustic foam thickness: $T_{\text{ins}} = 25\text{ mm}$

Exterior Enclosure Envelope:
$$\begin{aligned}
L_{\text{ext}} &= L_{\text{int}} + 2 \cdot (T_{\text{wall}} + T_{\text{ins}}) \\
W_{\text{ext}} &= W_{\text{int}} + 2 \cdot (T_{\text{wall}} + T_{\text{ins}}) \\
H_{\text{ext}} &= H_{\text{int}} + 2 \cdot (T_{\text{wall}} + T_{\text{ins}}) + H_{\text{caster\_skid}}
\end{aligned}$$

For a standard generator ($L_g = 600\text{ mm}, W_g = 450\text{ mm}, H_g = 480\text{ mm}$):
- $L_{\text{ext}} = 600 + 150 + 120 + 140 + 2(18 + 25) = 1010 \approx 980\text{--}1000\text{ mm}$
- $W_{\text{ext}} = 450 + 150 + 2(18 + 25) = 686 \approx 690\text{ mm}$
- $H_{\text{ext}} = 480 + 75 + 45 + 30 + 2(18 + 25) + 30 = 746 \approx 750\text{ mm}$

### 2.2 Input Data Transformation & AutoCAD Script Formulation

The program parses the inbound job parameters and generates AutoCAD drawing commands:

```lisp
;; AutoLISP Parametric Box Formulation Routine
(defun c:GEN_BOXIE ( / Lg Wg Hg Cmin Lext Wext Hext Tw Tins JobID )
  ;; Default parameters or extracted from shop order data
  (setq JobID "WO-2026-8841")
  (setq Lg 600.0  Wg 450.0  Hg 480.0)
  (setq Cmin 75.0 Tw 18.0   Tins 25.0)
  (setq Lext (+ Lg (* 2 Cmin) 260.0 (* 2 (+ Tw Tins))))
  (setq Wext (+ Wg (* 2 Cmin) (* 2 (+ Tw Tins))))
  (setq Hext (+ Hg Cmin 75.0 (* 2 (+ Tw Tins))))

  ;; 1. Set Layer for Outer Panels (AIA Standard M-ENCL-PVIS)
  (command "-LAYER" "M" "M-ENCL-PVIS" "C" "7" "" "")
  ;; Draw Base / Outer Box Polyline
  (command "_RECTANG" (list 0.0 0.0) (list Lext Wext))

  ;; 2. Set Layer for Acoustic Insulation
  (command "-LAYER" "M" "M-ENCL-INSL" "C" "2" "" "")
  (command "_RECTANG" (list (+ Tw Tins) (+ Tw Tins))
                      (list (- Lext (+ Tw Tins)) (- Wext (+ Tw Tins))))

  ;; 3. Intake Baffle & Fan Cutout
  (command "-LAYER" "M" "M-VENT-INTK" "C" "4" "" "")
  (command "_CIRCLE" (list 100.0 (/ Wext 2.0)) 60.0) ; 120mm Intake Fan Cutout

  ;; 4. Exhaust Port Cutout & Heat Shield Mount
  (command "-LAYER" "M" "M-VENT-EXHT" "C" "1" "" "")
  (command "_RECTANG" (list (- Lext 150.0) (- (/ Wext 2.0) 60.0))
                      (list (- Lext 30.0)  (+ (/ Wext 2.0) 60.0)))

  ;; 5. Electrical Pass-through & Hardware
  (command "-LAYER" "M" "M-ELEC-PORT" "C" "6" "" "")
  (command "_CIRCLE" (list (+ Tw Tins 50.0) 0.0) 37.5) ; 75mm Brush Port

  (princ (strcat "\nBoxie AutoCAD Geometry generated for Job: " JobID))
  (princ)
)
```

---

## 3. Requirements Traceability Matrix (RTM)

The following matrix establishes forward and backward traceability between each System Requirement, its Technical Specification, the AutoCAD / CAD Formulation Element, the Physical Component, and the Verification Method.

| Requirement ID | Requirement Description | Technical Specification | AutoCAD / CAD Formulation Mapping | Affected Subsystem / Component | Verification Method |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **REQ-PHY-01** | Internal Clearance Envelope | $\ge 75\text{ mm}$ clearance around generator core | Calculated offset: `(list Cmin Cmin)` inside `M-ENCL-PVIS` | Inner Bay Frame / Acoustic Line | CAD Model Inspection / Physical Measurement |
| **REQ-PHY-02** | Exhaust Clearance | $\ge 150\text{ mm}$ standoff from muffler tip | Exhaust offset block on layer `M-VENT-EXHT` | Exhaust Heat Chamber | Dimensional Inspection |
| **REQ-PHY-03** | External Enclosure Limit | Max $1000 \times 700 \times 750\text{ mm}$ envelope | Outer bounding box dimensions on `G-ANNO-DIMS` | Outer Shell Assembly | CAD Bounding Box Verification |
| **REQ-PHY-04** | Wall Panel Construction | $18\text{ mm}$ Birch Plywood or $2.5\text{ mm}$ Alum | Parametric variable `Tw`; 3D Solid Extrusion thickness | Exterior Wall Panels | Material Cert & Caliper Inspection |
| **REQ-PHY-05** | Mobility & Handling | Dual $\varnothing 150\text{ mm}$ wheels, folding handle | Hardware blocks on layer `M-HARD-ACCS` | Running Gear & Handle Bracket | Load & Mobility Field Test (85 kg) |
| **REQ-PHY-06** | Service Access Panels | Hinged top lid, latching front panel | Split seam lines and hinge arcs on `M-HARD-ACCS` | Top Lid, Front Removable Panel | Ergonomic & Maintenance Demonstration |
| **REQ-ACO-01** | Acoustic Attenuation | $\ge 18\text{ dBA}$ reduction at 7 meters | Dual chamber acoustic isolation geometry | Full Enclosure System | Sound Level Meter (Type 2 SLM) ISO 3744 |
| **REQ-ACO-02** | Acoustic Foam Lining | $25\text{ mm}$ UL 94 HF-1 foam + MLV barrier | Boundary offset polyline on layer `M-ENCL-INSL` | Interior Lining Assembly | Flammability & Sound Absorption Test |
| **REQ-ACO-03** | S-Bend Baffle Maze | S-bend non-line-of-sight sound trap | Parametric baffle plates on `M-VENT-INTK` / `EXHT` | Air Intake & Exhaust Chambers | Sound Transmission Loss Test |
| **REQ-ACO-04** | Vibration Dampers | Decoupled floor with 4 Shore 50A mounts | Mounting bolt hole circle array on `M-HARD-ACCS` | Isolated Sub-floor Platform | Accelerometer Vibration Test |
| **REQ-THM-01** | Forced Cooling Airflow | $\ge 200\text{ CFM}$ active exhaust airflow | $\varnothing 120\text{ mm}$ fan cutout circles on `M-VENT-INTK` | 120mm / 240V Fan & Vent Shrouds | Anemometer Airflow Test |
| **REQ-THM-02** | Separation of Flow | Cold intake low; hot exhaust high opposite | Z-axis coordinate offset in elevation projection | Intake Lower / Exhaust Upper | Thermal Imaging & Smoke Flow Test |
| **REQ-THM-03** | Exhaust Decoupling & Shield | Direct pipe exit + $650^\circ\text{C}$ heat shield | Heat shield boundary polyline on `M-VENT-EXHT` | Exhaust Port & Stainless Flange | Thermal Couple Test ($< 60^\circ\text{C}$ wall) |
| **REQ-THM-04** | Over-temp Protection | Dual thermostat switch cut-in at $50^\circ\text{C}$ | Sensor bracket mounting holes on `M-ELEC-PORT` | Thermal Sensor & Fan Relay | Chamber Thermal Runaway Test |
| **REQ-SAF-01** | Cable Pass-Through | Weatherproof IP55 brush port $\varnothing 75\text{ mm}$ | $\varnothing 75\text{ mm}$ circle cutout on `M-ELEC-PORT` | Side Access Port | Ingress & Cable Seal Test |
| **REQ-SAF-02** | CO Monitor Mount | Interior bracket for certified CO alarm | Bracket footprint on layer `M-HARD-ACCS` | Carbon Monoxide Sensor | Sensor Operational Trigger Test |
| **REQ-SAF-03** | External Grounding Lug | M8 Copper chassis bonding terminal | M8 hole callout on `M-ELEC-PORT` / `G-ANNO-DIMS`| Chassis Grounding Stud | Resistance to Ground Test ($< 0.1\,\Omega$) |
| **REQ-SAF-04** | Ingress Protection | $45^\circ$ downward louvers, IP44 weather mesh | Louver profiles & blade angles on `M-VENT-INTK` | Exterior Intake & Exhaust Hoods | Water Spray / Ingress Testing |
| **REQ-INT-01** | Global Shop Solutions Interface | Structured work order / BOM data import from GSS ERP | Data parsing routine in generator script | GSS ERP Data Ingestion | ERP Schema & Data Ingestion Test |
| **REQ-INT-02** | Parametric Data Extraction | Extract $(L_g, W_g, H_g)$, material, options from GSS | Parametric variable assignment `(setq Lg ...)` | Input Transform Pipeline | Parameter Extraction Unit Test |
| **REQ-INT-03** | Cut-List & BOM Reconciliation | Export cut-list & hardware BOM back to GSS ERP | Polyline measurement & bill of materials dump | GSS Inventory & Shop Routing | BOM Cross-Check Against Inventory |
| **REQ-CAD-01** | Parametric Scripting | Script / LISP driver taking $(L_g, W_g, H_g)$ | AutoLISP function `c:GEN_BOXIE` & `.scr` file | CAD Automation Pipeline | Script Execution in AutoCAD |
| **REQ-CAD-02** | Layer Standardization | Standardized AIA/ISO 13567 CAD layers | Layer definition table implemented in script | Drawing File Structure | AutoCAD Layer Audit (`LAYWALK`) |
| **REQ-CAD-03** | Closed CNC Polylines | Closed `LWPOLYLINE` geometry for cutouts | Script generation using `_RECTANG` / `_PLINE` | DXF CNC Export | CAM Software DXF Toolpath Import Test |
| **REQ-CAD-04** | Dual-Dimension Callouts | Metric (mm) primary with Imperial (in) secondary | AutoCAD Dimension Style `DIMALT = 1` | Annotation Layer `G-ANNO-DIMS` | Visual CAD Drawing Review |

---

## 4. Verification & Validation Protocol

1. **CAD Automated Audit**: Prior to fabrication, the generated AutoCAD `.dwg` / `.dxf` must pass an automated linter verifying layer assignments, polyline closure for CNC paths, and clearance checks.
2. **Prototype Acoustic & Thermal Bench Test**:
   - Sound pressure level measured at 4 cardinal positions at $7\text{ m}$ distance with generator at 50% and 100% rated load.
   - 4-hour continuous burn test measuring interior ambient temperature, engine head temperature, and exhaust cowl temperature using K-type thermocouples.
3. **Transport & Ergonomics Validation**:
   - Verification of single-operator rollability, tilt leverage, handle comfort, and vehicle bed loading ergonomics.
