# HDPE Pipe Diameter Selector

A focused Python command-line tool: enter a required flow rate and target velocity, and the program selects a suitable documented HDPE pipe size from its catalogue.

## What it does
1. Prompts for flow rate in m³/h and target velocity in m/s.
2. Uses PE grade and SDR (defaults: PE100 and SDR 11).
3. Reads only sizes present in the local JSON catalogue.
4. Calculates nominal internal diameter and velocity for every size.
5. Selects the **smallest catalogue size whose calculated velocity does not exceed the target**.
6. Displays the recommendation and alternatives. If no size meets the target, it warns and shows the largest available size.

## Quick start
Requires Python 3.10+. No third-party packages are required.

```powershell
git clone https://github.com/alizarei-eng/hdpe-pipe-diameter-selector.git
cd hdpe-pipe-diameter-selector
python main.py
```

Example: flow 50 m³/h, target velocity 1.5 m/s, PE100 SDR11. The current starter catalogue selects OD 140 mm, nominal ID 114.6 mm and velocity about 1.34 m/s.

## Calculation
- Q (m³/s) = Q (m³/h) / 3600
- ID (mm) = OD (mm) - 2 × nominal wall thickness (mm)
- V = Q / A = 4Q / (π × ID²), with ID converted to metres.

## Project structure
```text
core/pipe_database.py
core/pipe_sizing.py
databases/pipe_standards.json
tests/test_pipe_sizing.py
docs/USER_GUIDE.md
main.py
```

## Engineering limitations
The starter database contains 22 PE100 SDR11 sizes, OD 32–630 mm. Dimensions were transcribed from BSI Kitemark Licence KM 546725 referring to ISO 4427-2:2007. This is a historical, limited dataset—not a complete current catalogue. Nominal ID is not guaranteed minimum bore.

This is preliminary velocity-based selection only. It does not check pressure class/PN, operating pressure, head loss, pump curve, water hammer, temperature derating, chemical compatibility, installation conditions or manufacturer availability. Verify the current controlled standard and selected manufacturer's datasheet before procurement or engineering release.

## Tests
```powershell
python -m unittest discover -s tests -v
```
