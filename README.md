# HDPE Pipe Diameter Selector

A Python command-line tool: enter flow rate and target velocity, then select the smallest available HDPE nominal outside diameter whose calculated nominal velocity does not exceed the target.

## Database scope
- Nominal OD series: 16 to 3000 mm, based on the ISO 4427-2 dimensional series.
- Material grades: PE80 and PE100.
- SDR series: 6, 7.4, 9, 11, 13.6, 17, 21, 26, 33 and 41.
- Grade/SDR combinations follow the ISO 4427-2 reference pressure mapping. PE100 SDR6 is not included; PE80 SDR6 is.
- Nominal PN reference is shown for each grade/SDR combination.

## Important dimensional-data qualification
This is an expanded engineering reference dataset, not a certified manufacturer's catalogue. SDR/OD combinations follow the dimensional availability pattern, but most nominal wall thicknesses are generated from OD/SDR with minimum-wall rules and rounded to 0.1 mm. The values are flagged in the JSON as requiring verification against a controlled copy of Table 2. Existing SDR11 values for 32–630 mm are retained from the historical source; OD20 SDR11 is corrected to 2.0 mm. Do not release a design based solely on unverified derived thicknesses.

## What it does
1. Prompts for flow rate (m³/h) and target velocity (m/s).
2. Lists valid SDR options for the selected PE grade.
3. Calculates nominal ID and velocity for every matching size.
4. Selects the smallest OD meeting the velocity target.
5. Displays PN reference and alternative sizes.

## Quick start
Requires Python 3.10+; no third-party packages are required.

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
This is preliminary velocity-based selection. It does not check pressure loss, pump curve, water hammer, temperature derating, chemical compatibility, installation or manufacturer availability. PN values are reference values and require temperature/design-factor checks. Verify all derived wall thicknesses and project requirements before engineering release.

## Tests
```powershell
python -m unittest discover -s tests -v
```
