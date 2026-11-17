# HDPE Pipe Diameter Selector

A focused Python command-line tool: enter a required flow rate and target velocity, and the program selects a suitable documented/reference HDPE pipe size from its dimensional database.

## Current database scope
- Nominal outside diameter series: 16 to 3000 mm, based on ISO 4427-2:2019 Table 1.
- Material grades: PE80 and PE100.
- SDR currently populated: SDR 11 only.
- PE80 and PE100 share the same nominal geometry at a given OD and SDR; their pressure ratings are different.
- For OD values above 630 mm, nominal wall thickness is provisionally calculated from OD/SDR and rounded to 0.1 mm. These derived values must be checked against the controlled standard before design use.

## What it does
1. Prompts for flow rate in m³/h and target velocity in m/s.
2. Uses PE grade and SDR (defaults: PE100 and SDR 11).
3. Calculates nominal internal diameter and velocity for every matching database record.
4. Selects the smallest catalogue/reference size whose calculated velocity does not exceed the target.
5. Displays the recommendation and alternatives. If no size meets the target, it warns and shows the largest available size.

## Quick start
Requires Python 3.10+. No third-party packages are required.

```powershell
git clone https://github.com/alizarei-eng/hdpe-pipe-diameter-selector.git
cd hdpe-pipe-diameter-selector
python main.py
```

## Calculation
- Q (m³/s) = Q (m³/h) / 3600
- ID (mm) = OD (mm) - 2 × nominal wall thickness (mm)
- V = Q / A = 4Q / (π × ID²), with ID converted to metres.

## Engineering limitations
This is preliminary velocity-based selection only. It does not check pressure class/PN, operating pressure, head loss, pump curve, water hammer, temperature derating, chemical compatibility, installation conditions or manufacturer availability. For straight pipes with OD >= 900 mm, maximum out-of-roundness is to be agreed between manufacturer and end user. Verify all derived large-diameter wall thicknesses and pressure classes against the current controlled standard and project requirements before engineering release.

## Tests
```powershell
python -m unittest discover -s tests -v
```
