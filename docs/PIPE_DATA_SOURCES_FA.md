{
  "schema_version": "1.0.0",
  "sources": [
    {
      "source_id": "ISO_4427_2_2019",
      "type": "international_standard",
      "publisher": "International Organization for Standardization",
      "title": "ISO 4427-2:2019 — Plastics piping systems for water supply and for drainage and sewerage under pressure — PE — Part 2: Pipes",
      "url": "https://www.iso.org/standard/72184.html",
      "scope": "PE pipe dimensions and requirements; reference operating temperature 20°C; full controlled standard required for contractual design verification."
    },
    {
      "source_id": "ISO_4427_2_2019_AMD1_2023",
      "type": "amendment_reference",
      "publisher": "ISO",
      "title": "ISO 4427-2:2019/Amd 1:2023",
      "url": "https://cdn.standards.iteh.ai/samples/82985/36c0c29fed344ea1835b5f1798064d6a/ISO-4427-2-2019-Amd-1-2023.pdf",
      "scope": "Amendment reference for SDR and pressure classification. Confirm against a controlled copy."
    },
    {
      "source_id": "PE100PLUS_PRESSURE_DESIGN",
      "type": "technical_guidance",
      "publisher": "PE100+ Association",
      "title": "PE pipe design for given operating conditions",
      "url": "https://www.pe100plus.com/PE-Pipes/Technical-guidance/model/Design/PE-pressure-pipe/PE-pipe-design-i244.html",
      "scope": "MOP relation to MRS, SDR and design coefficient; PE80 MRS 8 MPa; PE100/PE100-RC MRS 10 MPa; minimum C 1.25 for water."
    },
    {
      "source_id": "PE100PLUS_OPERATING_PRESSURE",
      "type": "technical_guidance",
      "publisher": "PE100+ Association",
      "title": "PE pipe maximum operating pressure",
      "url": "https://www.pe100plus.com/PE-Pipes/Technical-guidance/model/Design/PE-pressure-pipe/operating-pressure-i245.html",
      "scope": "Operating pressure, material grade, SDR and design coefficient."
    },
    {
      "source_id": "PPI_PE_HANDBOOK_2022",
      "type": "engineering_handbook",
      "publisher": "Plastics Pipe Institute",
      "title": "Handbook of Polyethylene Pipe, 2022",
      "url": "https://plasticpipe.org/common/Uploaded%20files/Technical/PPI%20PEHandbook2022.pdf",
      "scope": "Material properties, design, pressure rating, hydraulic design, inside diameter, head loss, surge and installation."
    },
    {
      "source_id": "GF_UTILITY_SYSTEMS_2022",
      "type": "manufacturer_catalogue",
      "publisher": "GF Piping Systems Indonesia / PT Georg Fischer Indonesia",
      "title": "PE Product Range — Utility Systems",
      "revision": "07.22",
      "url": "https://www.gfps.com/content/dam/gfps/id/product-ranges/gfps-id-product-range-utility-systems-en.pdf",
      "scope": "Manufacturer-specific PE100 water pipe tables for SDR 7.4, 9, 11, 13.6, 17, 21 and 26; OD tolerances, out-of-roundness, minimum wall thickness and average mass."
    },
    {
      "source_id": "NEPROPLAST_HDPE_CATALOGUE",
      "type": "manufacturer_catalogue",
      "publisher": "New Products Industries Co. Ltd. (NEPROPLAST)",
      "title": "HDPE Water, Gas & Sewage System",
      "url": "https://neproplast.com/wp-content/uploads/2025/10/HDPE.pdf",
      "scope": "Manufacturer-specific PE100 dimensions, mass and pressure classifications; Table 5.1 and following table. Useful independent cross-check; not merged into the GF dataset."
    },
    {
      "source_id": "ISO_4427_3_2019",
      "type": "international_standard",
      "publisher": "International Organization for Standardization",
      "title": "ISO 4427-3:2019 — Plastics piping systems for water supply and for drainage and sewerage under pressure — PE — Part 3: Fittings",
      "url": "https://committee.iso.org/cms/live/live/en/sites/isoorg/contents/data/standard/07/21/72185.html?browse=ics",
      "scope": "Requirements and test parameters for PE fittings including fusion, mechanical and fabricated fittings. The current revision status must be checked; manufacturer catalogue data is not a substitute for the controlled standard."
    },
    {
      "source_id": "GF_PE_SYSTEMS_WATER_UTILITY_INDIA",
      "type": "manufacturer_catalogue",
      "publisher": "GF Piping Systems India",
      "title": "PE Systems — Water Utility",
      "url": "https://www.gfps.com/content/dam/gfps/in/product-ranges/gf-in-catalog-pe-systems-water-utility-en.pdf",
      "scope": "Manufacturer-specific PE100 electrofusion couplers, 90-degree elbows, equal tees, reducers and monoline tapping saddles; catalogue pages 14–20. Product data is not a universal standard or local-stock guarantee."
    }
  ],
  "data_policy": [
    "Generic ISO reference records and manufacturer-specific catalogue records are stored separately.",
    "Every pipe record must identify whether its dimensions are directly transcribed, standard-derived, or calculated.",
    "PN/MOP is not a universal pressure guarantee: temperature, design coefficient, fluid, surge, service life and applicable standard must be checked.",
    "Manufacturer product range does not establish local market stock or availability.",
    "Fitting dimensions, pressure ratings and product codes are stored in manufacturer-specific datasets and must not be inferred from pipe OD/SDR tables.",
    "A fitting's pressure class and compatible pipe SDR are product-specific; verify the exact manufacturer's data sheet, fusion compatibility and project design conditions."
  ]
}

## Transferred hydraulic fitting reference data

The file `databases/hydraulic_fittings.json` contains 11 records transferred from the existing `pipe-pressure-loss-calculator` repository (`databases/fittings.json`). It preserves the prior project's K values for long-radius 90° elbows, standard 90° elbows, 45° elbows, tee straight-run and branch-flow paths, fully open gate/ball/globe valves, swing check valve, sharp-edged entrance and exit into a large tank.

This file is a **generic hydraulic reference**, not a manufacturer dimensional catalogue. Its K values are approximate and retained as legacy screening values. They must not be assigned to the GF catalogue products as if measured for those products. For tees, select the coefficient for the actual path (straight run or branch); never add both coefficients for one flow path. Reducing tees, laterals and fabricated manifolds require geometry-specific data.

The two fitting data layers now have separate purposes:

- `databases/manufacturer_catalogues/gf_pe100_water_fittings_2022.json`: product geometry, dimensions, product codes, mass and manufacturer-specific pressure notes.
- `databases/hydraulic_fittings.json`: generic minor-loss K references for preliminary hydraulic calculations.
