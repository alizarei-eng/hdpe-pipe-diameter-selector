# PE Pipe Data — Sources, Interpretation and Quality Rules

## Data layers

The repository intentionally keeps two datasets separate:

1. `databases/pipe_standards.json`: generic PE80/PE100 reference combinations. Its existing OD/SDR-derived wall values remain explicitly labelled as calculated and requiring verification against a controlled ISO table.
2. `databases/manufacturer_catalogues/gf_pe100_water_2022.json`: manufacturer-specific PE100 water-pipe dimensions and average mass transcribed from the GF Piping Systems Indonesia Utility Systems catalogue (revision 07.22).

Do not merge a manufacturer catalogue into the generic standards table. A manufacturer's catalogue is evidence of that product range, not proof that every manufacturer supplies the same combination.

## Manufacturer dataset fields

- `dn_od_mm`: nominal outside diameter.
- `mean_od_min_mm`, `mean_od_max_mm`: catalogue mean outside diameter limits.
- `max_out_of_roundness_mm`: catalogue maximum out-of-roundness.
- `sdr`, `nominal_pressure_bar`: catalogue SDR and pressure class.
- `minimum_wall_thickness_mm`: manufacturer-published minimum wall thickness.
- `average_mass_kg_m`: manufacturer-published average mass per metre.
- `source_table`, `source_page`: traceability to the source table.
- `availability_note`: source availability caveat where applicable.
- `record_status`: direct transcription status.

A missing row means the source catalogue did not publish that combination; it must not be interpreted as zero thickness or as a universal manufacturing prohibition.

## Pressure design

The PE100+ Association gives:

`MOP = (20 × MRS) / (C × (SDR − 1))`

where MOP is in bar, MRS in MPa, and C is the overall service/design coefficient. The guidance identifies MRS = 8 MPa for PE80 and 10 MPa for PE100/PE100-RC, with minimum C = 1.25 for water and pressure sewerage. Project codes may require a higher coefficient.

The GF catalogue explicitly states its PN reference at 20°C and requires derating at higher temperature. Therefore, the catalogue PN must not be presented as an unrestricted operating pressure at any temperature. Surge, fatigue, external loads, installation, chemical compatibility and design life also require project checks.

## Hydraulic inside diameter

For nominal geometry only:

`ID_nominal = OD_nominal − 2 × nominal wall thickness`

Do not use minimum wall thickness as if it were average wall thickness when calculating a guaranteed bore. Actual internal diameter depends on dimensional tolerances and manufacturing details. The current generic database's nominal ID calculation is a screening value, not a guaranteed minimum bore.

## Sources

See `sources/source_register.json` for source URLs and scope. Key references:

- ISO 4427-2:2019 — PE pipes for water supply and pressure drainage/sewerage.
- PE100+ Association — pressure design, MRS, SDR and service coefficient.
- PPI Handbook of Polyethylene Pipe (2022) — engineering design and hydraulic calculations.
- GF Piping Systems Indonesia Utility Systems catalogue (07.22) — direct manufacturer dimensional and mass tables.
- NEPROPLAST HDPE catalogue — independent manufacturer cross-check.

## Quality and use

- Standard-derived calculations, direct standard transcriptions and manufacturer transcriptions must remain distinguishable.
- Catalogue absence is not the same as non-manufacturability.
- Local stock, brand availability, certificates and current production status must be confirmed with the supplier.
- Use the current controlled standard and manufacturer datasheet for procurement, pressure design and construction documents.


## PE fitting data

The first manufacturer-specific fitting dataset is `databases/manufacturer_catalogues/gf_pe100_water_fittings_2022.json`. It transcribes GF India PE Systems — Water Utility catalogue entries for PE100 electrofusion couplers (SDR11 and SDR17), 90° elbows, equal 90° tees, reducers with integral pipe fixation, and 8 mm-cutter monoline tapping saddles. The records include the main/branch or outlet diameters, the dimensions actually shown in the source tables, product codes where published, weights, SDR/pressure notes, source page and transcription status.

**Important interpretation rules:**

- This is a manufacturer catalogue dataset, not the generic ISO 4427-3 dimensional database. ISO 4427-3:2019 defines requirements and test parameters for PE fittings; it does not mean every listed manufacturer product has identical geometry.
- The catalogue identifies PE100 water electrofusion products, with product-specific SDR and pressure declarations. Do not transfer a 16 bar rating from one fitting family to another without checking its exact entry.
- Tapping-saddle main diameter and branch/outlet diameter are different fields. The outlet is not the saddle's main-pipe size.
- Missing product rows are not evidence of universal unavailability. Local stock and current product status require manufacturer confirmation.
- Fitting dimensions are not automatically suitable as hydraulic loss coefficients. K-values or equivalent lengths require separate validated hydraulic data.
