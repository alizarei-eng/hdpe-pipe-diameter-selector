# HDPE Pipe Diameter Selector

A lightweight Python command-line tool for preliminary HDPE pipe diameter selection. Enter the design flow rate and target water velocity, choose a material grade and SDR from numbered menus, and the program recommends a nominal outside diameter from the available reference dataset.

## Features

- Accepts flow rate in **m³/h** and target velocity in **m/s**.
- Lists all material grades present in the database; the user selects by menu number.
- Lists only the SDR values available for the selected grade; the user selects by menu number.
- Evaluates all available OD records for the selected grade/SDR combination.
- Recommends the **smallest available OD** whose calculated nominal velocity is not greater than the target.
- Displays nominal wall thickness, calculated nominal internal diameter, velocity, reference PN, and alternative sizes.
- Gives a warning if even the largest available size exceeds the target velocity.
- Uses only the Python standard library; no third-party packages are required.

## Database scope

| Item | Included data |
|---|---|
| Material grades | PE80, PE100 |
| Outside diameter series | 16–3000 mm |
| SDR values for PE80 | 6, 7.4, 9, 11, 13.6, 17, 21, 26, 33, 41 |
| SDR values for PE100 | 7.4, 9, 11, 13.6, 17, 21, 26, 33, 41 |
| Number of pipe records | 506 |
| Reference standard family | ISO 4427-2 |

PE100 SDR6 is not included in the database's grade/SDR mapping. The menus are generated from the records actually present in the JSON database, rather than from hard-coded lists.

## Quick start

Requires **Python 3.10 or newer**.

### 1. Clone the repository

```powershell
git clone https://github.com/alizarei-eng/hdpe-pipe-diameter-selector.git
cd hdpe-pipe-diameter-selector
```

### 2. Run the program

```powershell
python main.py
```

No virtual environment or package installation is required for the current command-line version.

## Program workflow

1. Enter flow rate (m³/h).
2. Enter target velocity (m/s).
3. Select a material grade by its displayed number (for example, PE100).
4. Select an SDR by its displayed number. Only SDR values available for the selected grade are shown.
5. Review the recommended pipe and the alternative-size table.

The program re-prompts when a non-positive number or invalid menu selection is entered.

## Calculation method

Flow conversion:

`Q (m³/s) = Q (m³/h) / 3600`

Nominal internal diameter:

`ID (mm) = OD (mm) - 2 × e (mm)`

Cross-sectional flow area:

`A = π × (ID / 1000)² / 4`

Mean velocity:

`V = Q / A`

The selector sorts the available records by OD and chooses the first record for which calculated nominal velocity is less than or equal to the target. If no record meets the target, it reports the largest available OD and displays a warning.

## Tests

Run the automated unit tests from the repository root:

```powershell
python -m unittest discover -s tests -v
```

The test suite covers basic selection, PE80 support, grade-specific SDR availability, unsupported PE100 SDR6, the upper OD range, the OD20 SDR11 minimum wall value, alternative outputs, and invalid inputs.

## Important engineering qualifications

**This program is a preliminary velocity-based selector, not a complete hydraulic design or a certified manufacturer's catalogue.**

The 506-record dataset is an expanded engineering reference dataset:

- The nominal OD series and grade/SDR mapping are based on the referenced ISO 4427-2 material.
- Except for retained SDR11 values for OD 32–630 mm and the corrected OD20 SDR11 value, most nominal wall thicknesses are generated from OD/SDR, rounded to 0.1 mm, and subject to minimum-wall rules. They are flagged in the JSON as requiring verification.
- These generated values are **not** a transcription of every dimensional-table entry. Verify the selected dimensions against a controlled copy of the applicable standard and the selected manufacturer's datasheet before procurement or design release.
- PN values are reference values. Temperature derating, design coefficient, service conditions, and project requirements must be checked separately.
- The dataset does not represent every manufacturer's product range, national deviation, tolerance, or actual bore.

The current selector does **not** calculate pressure loss or check pump curves, water hammer, temperature derating, chemical compatibility, installation conditions, structural loading, or manufacturer stock/availability. These checks are required before final engineering approval.

## Repository structure

```text
hdpe-pipe-diameter-selector/
├── core/
│   ├── pipe_database.py       # Database access and pipe geometry
│   └── pipe_sizing.py         # Velocity-based diameter selection
├── databases/
│   └── pipe_standards.json    # PE80/PE100 reference records
├── docs/
│   └── USER_GUIDE.md          # Persian user guide
├── tests/
│   └── test_pipe_sizing.py    # Unit tests
└── main.py                    # Command-line entry point
```

## Project status

The current command-line scope is complete for preliminary selection by flow rate, target velocity, PE grade, and SDR. Further hydraulic checks and manufacturer-specific validation are intentionally outside this version's scope.
