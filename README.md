# Senior Design II: RPW Acoustic Detection

Team report and supporting materials for a low-cost IoT system that investigates acoustic screening for red palm weevil (RPW) activity.

**Start here:** [Current report PDF](output/senior_design_report_enhanced.pdf) · [Main LaTeX source](output/senior_design_report_enhanced.tex) · [Instructions for AI assistants](output/AGENTS.md)

## Current system

Surface-contact WANGCL piezo sensor → MCP602E conditioning → sensing ESP32 → SX1278 LoRa → second ESP32 → Wi-Fi → server/dashboard.

- The supplied full schematic shows a 38-pin ESP32 DevKit. Older stripboard layouts assume a 30-pin board and require reconciliation before assembly.
- Communication tests used 433 MHz spring antennas, SF7, 125 kHz bandwidth, coding rate 4/5, and configured TX power of 10 dBm. Tests included obstructions and reflective materials; the furthest distance reached was 350 m. The eight-byte test records contain synthetic probabilities, not classifier results.
- The specified feature codec uses a 15 × 13 int8 MFCC matrix, temporal deltas, ZigZag mapping, and a predefined eight-schedule Rice bank. Offline size results are separate from embedded/RF validation. Date/battery mappings and protocol versioning remain unresolved; a CRC is not established by the current application-layout specification.
- Final selection between local ESP32 classification and MFCC transmission for cloud classification remains pending.
- Mechanical playback uses a vibration exciter coupled to wood/palm material. Bench emulation does not establish detection of live larvae. Completed playback, classifier, and end-to-end results still need documentation.

## Files

| Path | Purpose |
|---|---|
| `output/senior_design_report_enhanced.tex` | Authoritative current report; edit this file in place |
| `output/senior_design_report_enhanced.pdf` | Compiled current report |
| `output/References.bib` | Bibliography |
| `output/compression_design.tex` | Current codec and payload specification |
| `output/compression_results.tex` | Supplied full-dataset offline size summaries |
| `output/compression_schedule_bank.tex` | Exact ordered schedule bank |
| `output/power_measurements.tex` | Current/power observations and calculations |
| `output/communication_results.tex` | Radio configuration, packet layout, and log results |
| `output/cost_analysis.tex` | Itemized procurement schedule |
| `output/figures/`, `output/uploads/`, `output/AUSlogo.png` | Report images and diagrams |
| `output/stripboard/` | Earlier prototype layout JSONs and assembly notes |
| `data/power/` | Available original power-measurement inputs and correction notes |
| `sources/` | Original report reference material; read-only |
| `docs/` | Earlier plans/specifications; historical context |

`output/senior_design_report_template_aligned.tex`, `output/mfcc_compression.tex`, the older codec plots, and the source-correction register describe earlier revisions. They are retained for history, not as replacements for the current report or current codec specification. Some existing architecture diagrams also need updating.

## Build

Install TeX Live or MacTeX with `latexmk`, `biber`, and the packages used by the main TeX file (including memoir, biblatex, siunitx, algorithm2e, and listings).

```bash
cd output
latexmk -pdf -interaction=nonstopmode -halt-on-error senior_design_report_enhanced.tex
```

`output/.latexmkrc` currently uses `/Library/TeX/texbin` for MacTeX. On Linux or another TeX installation, run with `latexmk -norc -pdf -interaction=nonstopmode -halt-on-error senior_design_report_enhanced.tex` so executables resolve through your PATH.

LaTeX auxiliary files are ignored. The compiled report PDF is tracked; rebuild and commit it with report changes. Inspect changed pages and check for undefined citations/references. Existing table-width and Gantt-layout warnings remain.

## Figure regeneration and data limits

Generated figures are included, so Python is not required to build the report. The existing `output/build_*.py` scripts use Matplotlib. The power and communication scripts still refer to the original author's absolute input paths; point them at local measurement files before running. `build_codec_figures.py` produces older exploratory figures, not the current schedule-bank summary.

The original communication CSV, compression-size CSV, quantized feature datasets, and updated firmware implementation were unavailable when this handoff was prepared. Compression statistics are reproduced from the supplied handoff and have not been independently recomputed from recording-level data. No firmware, dataset, or hardware validation is implied by the document build.

## Editing together

Use small branches and pull requests. Keep earlier revisions blue (`\earlierrevision{...}` in LaTeX) and newer edits green (`\newrevision{...}`). Preserve the project goal and use the smallest supported edit. Put methods in Technical Approach, actual implementation status in Implementation, measurements in Preliminary Results, and remaining evaluation procedures in Validation. Keep detailed schedule vectors and provenance in appendices.

The report is still in progress. The original January–June 2026 schedule and cover term are historical; current dates and completion status need team confirmation.

## Public sharing

Receipts, reimbursement documents, banking information, credentials, and local build logs are excluded. The report retains its academic authorship and title-page information. No license has been selected for original project material. Cited third-party figures and the university logo retain their owners' rights; public availability does not grant a reuse license.
