# AGENTS.md

Welcome to **Boxie** (Parametric Portable Generator Enclosure Design). This guide outlines the conventions, architecture, tooling workflows, and operational basics for AI agents and human contributors maintaining this project.

---

## 1. Project Overview & Scope

The purpose of this project is to maintain, formulate, and generate engineering designs for portable generator enclosures ("Boxie") ready for drafting and fabrication in **AutoCAD** (via DXF, AutoLISP, or Script files) and modern CNC/sheet-metal/plywood workflows, driven by structured input job data.

Key objectives:
- **Acoustic Attenuation**: Enclosure sound suppression (target -15 dBA to -25 dBA reduction) using maze-baffle geometry and sound-dampening acoustic foam.
- **Thermal Management & Airflow**: Active/passive forced air ventilation separating intake cool air from high-temp combustion exhaust.
- **Portability & Serviceability**: Modular flat-pack or quick-latch assembly, fold-out handles, all-terrain casters, and quick-access maintenance panels.
- **Parametric CAD Generation**: Formulated mathematical models that translate input dimensions $(L_g, W_g, H_g, P_{\text{watt}})$ into AutoCAD entities (layers, polylines, 3D solids, cutouts).
- **Manufacturing Data Interfacing**: Structured ingestion of work orders, material specifications, and cut-list export to interface enterprise shop and manufacturing systems.

---

## 2. Repository Layout

```
.
├── AGENTS.md            # Maintenance guide and rules for AI agents & contributors (aliased as agents.md)
├── REQUIREMENTS.md      # Engineering requirements, CAD parametric formulation & Traceability Matrix (RTM)
├── README.md            # Project presentation, overview diagrams, and generator box visual specifications (aliased as read.MD)
├── LICENSE              # Repository license
└── scripts/             # (Optional) Parametric generators, AutoLISP routines, DXF generation tools
```

---

## 3. AutoCAD / CAD Automation Standards

When writing scripts, formulas, or documentation for AutoCAD:

### 3.1 Layer Naming Conventions
Follow AIA / ISO 13567 compliant layer standards:
- `M-ENCL-PVIS`: Primary Enclosure Visible Edges / Outer Walls (Color: White/7, Continuous)
- `M-ENCL-INSL`: Acoustic Insulation Lining (Color: Yellow/2, Hidden2)
- `M-VENT-INTK`: Air Intake Baffles & Louvers (Color: Cyan/4, Continuous)
- `M-VENT-EXHT`: Exhaust Port & Heat Shielding (Color: Red/1, Continuous)
- `M-HARD-ACCS`: Hardware (Hinges, Latches, Handles, Wheels) (Color: Green/3, Continuous)
- `M-ELEC-PORT`: Electrical Pass-Through & Port Cutouts (Color: Magenta/6, Continuous)
- `G-ANNO-DIMS`: Enclosure Dimensions & Callouts (Color: 8/Gray, Continuous)
- `G-ANNO-TEXT`: Notes and Labels (Color: White/7)

### 3.2 Geometric & Tolerancing Rules
- **Units**: Default units are Millimeters (Metric) with Dual Dimensioning (Inches) supported.
- **Clearance Margins**:
  - Minimum clearance from generator frame to inner wall insulation: $C_{\text{min}} \ge 75\text{ mm}$ (3.0 in).
  - Exhaust clearance to heat shield: $C_{\text{ex}} \ge 150\text{ mm}$ (6.0 in).
- **Sheet Stock Thickness ($T$)**:
  - Plywood / Composite: $T = 18\text{ mm}$ (0.75 in).
  - Sheet Metal (Aluminum 5052-H32 / Galvanized Steel): $T = 2.0\text{ mm} - 3.0\text{ mm}$.
- **Kerf & Joinery Allowance**: Box joint / finger joint kerf compensation of $0.2\text{ mm}$ for CNC routing or laser cutting.

---

## 4. Maintenance & Contribution Guidelines

### 4.1 Requirement Traceability
- Every design decision, cutout, baffle dimension, or CAD layer MUST trace back to a Requirement ID in `REQUIREMENTS.md` (e.g., `REQ-PHY-01`, `REQ-ACO-02`, `REQ-INT-01`, `REQ-CAD-01`).
- When modifying enclosure geometry or AutoCAD formulation scripts, update the **Requirements Traceability Matrix (RTM)** in `REQUIREMENTS.md` and verify diagram consistency in `README.md`.

### 4.2 Formatting & Conventions
- Maintain clear Markdown formatting across all `.md` files.
- Keep `agents.md` and `read.MD` synchronized or linked with `AGENTS.md` and `README.md`.
- Diagrams should be represented with clear ASCII/Unicode orthographic projections (Top, Front, Side views) and isometric projections so they are readable in terminal and web markdown viewers.
- Math equations should be expressed in clean LaTeX format (e.g., $V_{\text{box}} = L \times W \times H$).

### 4.3 Validation Workflow
Before submitting any changes:
1. Verify that all requirement IDs in `REQUIREMENTS.md` match entries in the Traceability Matrix.
2. Confirm dimensional consistency across `REQUIREMENTS.md`, `README.md`, and any CAD scripts.
3. Check layer naming against the AutoCAD Layer Standard (Section 3.1).
4. Run syntax and integrity checks on all documentation and CAD automation files.
