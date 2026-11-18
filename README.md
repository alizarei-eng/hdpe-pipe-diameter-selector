# HDPE Pipe Diameter Selector

Velocity-based selection of a documented HDPE catalogue size.

## Features
- PE80 and PE100 grade selection.
- Grade-specific SDR menus.
- OD catalogue selection and nominal ID calculation.
- Recommended size and catalogue alternatives.
- Optional EC-based TDS/density/viscosity screening display.

## Run
```bash
python main.py
python -m unittest discover -s tests -v
```

## Important
The pipe recommendation remains based on flow rate, target velocity, grade, SDR and catalogue geometry. Fluid properties do not change the velocity calculation for a specified volumetric flow and pipe bore. EC-based fluid properties are displayed for continuity with the hydraulic projects, not used to select the diameter.

EC-to-TDS factor is approximate and depends on ionic composition. EC alone cannot identify individual ion concentrations. The optional seawater ionic profile is not applied to groundwater or RO concentrate without laboratory confirmation.
