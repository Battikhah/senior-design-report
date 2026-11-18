# Original power inputs

These files are preserved as supplied, not rewritten to match later corrections.

- `EverythingElse.csv`: raw operating-mode readings; the team's later report values are idle 33 mA, sensing 42 mA, CNN active 53 mA, CNN idle 33 mA, and one radio-standby reading of 33 mA. Sensing duration is 60 s at 4.8 V. Non-transmission readings include ESP32 and connected circuitry. These are readings observed at a point in time, not demonstrated run-average currents.
- `LoRa_Power_Consumption(3.3V).xlsx`: original transmission worksheet. The team corrected its packet size to eight bytes. The report recalculates energy per byte using eight, while retaining measured current/power and run/packet energy. The workbook's original nine-byte calculation is historical.

Use `../../output/power_measurements.tex` for current reporting and measurement limitations. The existing figure script verifies the original worksheet arithmetic and uses later team values for operating-current plots; its absolute input directory needs changing for another machine. Rebuilding the LaTeX report uses the committed figures and does not require running this script.

## Scheduled-node planning estimate

`estimated_energy_budget.csv` records the inputs, assumptions, calculated energies and solar scenarios used by `../../output/power_budget_estimate.tex` and `../../output/figures/estimated_node_solar_energy.pdf`. These are calculations, not additional measured power or solar data. The model uses 12 wake-ups/day, a 20 s assumed active period, and the reported 4 mA sleep current at an assumed whole-node 5 V boundary. Conversion losses, upstream standing drain and usable battery fraction are explicit assumptions. Solar scenarios use a hypothetical 1 W panel and 60% combined panel-to-battery harvest efficiency. The model covers one sensing node, excluding head and server power. The current report remains authoritative for limitations and parameter definitions.
