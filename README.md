# HDPE Pipe Diameter Selector

Velocity-based selection of a documented HDPE catalogue size.

## Features
- PE80 and PE100 grade selection.
- Grade-specific SDR menus.
- OD catalogue selection and nominal ID calculation.
- Recommended size and catalogue alternatives.
- Optional EC-based TDS/density/viscosity screening display.

## Pipe data sources
- Generic ISO reference dataset: `databases/pipe_standards.json`.
- Manufacturer-specific GF PE100 water-pipe catalogue data (OD tolerances, ovality, minimum wall and average mass): `databases/manufacturer_catalogues/gf_pe100_water_2022.json`.
- Manufacturer-specific GF PE100 water-fitting catalogue data (electrofusion couplers, elbows, tees, reducers and tapping saddles): `databases/manufacturer_catalogues/gf_pe100_water_fittings_2022.json`.
- Transferred generic hydraulic fitting K references (elbows, tee flow paths, valves, entrances and exits): `databases/hydraulic_fittings.json`.
- Source register: `sources/source_register.json`.
- Data interpretation and engineering limitations: `docs/PIPE_DATA_SOURCES_FA.md`.

Pipe and fitting manufacturer catalogue data, and generic hydraulic K references, are kept in separate datasets. Missing catalogue combinations are not treated as zero or as universally unavailable. PN is referenced at 20°C and must be checked for temperature derating and project conditions.

## Run
```bash
python main.py
python -m unittest discover -s tests -v
```

## Important
The pipe recommendation remains based on flow rate, target velocity, grade, SDR and catalogue geometry. Fluid properties do not change the velocity calculation for a specified volumetric flow and pipe bore. EC-based fluid properties are displayed for continuity with the hydraulic projects, not used to select the diameter.

EC-to-TDS factor is approximate and depends on ionic composition. EC alone cannot identify individual ion concentrations. The optional seawater ionic profile is not applied to groundwater or RO concentrate without laboratory confirmation.
