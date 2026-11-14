# Original power inputs

These files are preserved as supplied, not rewritten to match later corrections.

- `EverythingElse.csv`: raw operating-mode readings; the team's later report values are idle 33 mA, sensing 42 mA, CNN active 53 mA, CNN idle 33 mA, and one radio-standby reading of 33 mA. Sensing duration is 60 s at 4.8 V. Non-transmission readings include ESP32 and connected circuitry. These are readings observed at a point in time, not demonstrated run-average currents.
- `LoRa_Power_Consumption(3.3V).xlsx`: original transmission worksheet. The team corrected its packet size to eight bytes. The report recalculates energy per byte using eight, while retaining measured current/power and run/packet energy. The workbook's original nine-byte calculation is historical.

Use `../../output/power_measurements.tex` for current reporting and measurement limitations. The existing figure script verifies the original worksheet arithmetic and uses later team values for operating-current plots; its absolute input directory needs changing for another machine. Rebuilding the LaTeX report uses the committed figures and does not require running this script.
