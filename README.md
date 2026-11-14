# Senior Design: Low-Cost Acoustic Screening for Red Palm Weevil (RPW)

LaTeX source, figures, prototype wiring files and design notes for a senior-design project. The project is a low-cost IoT system that screens date palms for red palm weevil activity from acoustic and vibration signals.

> **Evidence boundary.** Bench work uses RPW recordings played through a mechanically coupled vibration exciter into wood. It validates signal injection, propagation, acquisition, preprocessing, packet design and classification under controlled conditions. It does **not** show detection of live weevils in infested palms. See `docs/superpowers/specs/`.

## System at a glance

```
piezo sensor -> MCP6002 -> ESP32 (filter + MFCC + compression) -> LoRa (SX1278) -> cluster node -> cloud / dashboard
```

- **Sensing layer:** ESP32 DevKit V1 (30-pin) with a piezo sensor module and an SX1278 LoRa radio.
- **Compression:** MFCC features are int8-quantized, delta-coded and Rice-coded into a versioned packet with a CRC (`output/compression_design.tex`, `output/mfcc_compression.tex`).
- **Cluster layer:** collects node packets and forwards them for classification.
- **Analysis:** power, communication and compression results, plus a cost analysis.

## Repository layout

| Path | Contents |
|---|---|
| `output/senior_design_report_enhanced.tex` | Main report. Pulls in the section files listed below. |
| `output/senior_design_report_template_aligned.tex` | Report aligned to the course template. |
| `output/*.tex` (other) | Section fragments: `compression_design`, `compression_results`, `compression_schedule_bank`, `mfcc_compression`, `communication_results`, `power_measurements`, `power_measurements_check`, `cost_analysis`. |
| `output/References.bib` | Bibliography (biblatex + biber, IEEE style). |
| `output/*.pdf` | Compiled reports. |
| `output/figures/` | All figures (PNG, JPG, PDF). Some are third-party (see Licensing). |
| `output/build_*.py` | Matplotlib scripts that regenerate figures (see Reproducing figures). |
| `output/stripboard/` | Stripboard prototype layouts (`*-input.json`) and `ASSEMBLY.md`, with pin map and build notes. |
| `output/academic_source_and_content_corrections.md` | Register of citation and content corrections made to the report. |
| `output/.latexmkrc` | latexmk config (macOS TeX Live path, biber). |
| `sources/` | Original submitted report (`main.tex`, PDF). **Read-only reference.** |
| `docs/superpowers/specs/`, `plans/` | Bench-validation and edge-cloud design spec and implementation plan. |
| `Untitled_Project.json`, `schema-sample.json` | Circuit-editor project files (ESP32 + SX1278 schematic data). |

## Building the report

Requires TeX Live (memoir, biblatex, biber, siunitx, algorithm2e, listings) and latexmk.

```bash
cd output
latexmk -pdf senior_design_report_enhanced.tex
# or
latexmk -pdf senior_design_report_template_aligned.tex
```

`.latexmkrc` hard-codes `/Library/TeX/texbin` (macOS MacTeX). Edit it on other systems. Build artifacts (`.aux`, `.log`, `.bbl`, ...) are git-ignored; the compiled PDFs are committed.

## Reproducing figures

```bash
pip install matplotlib
python3 output/build_codec_figures.py   # self-contained
```

`build_communication_figure.py` and `build_power_figures.py` read raw measurement data (a communication-log CSV and power-measurement files) from **absolute paths on the author's machine** that are not in this repository. They will not run unchanged. Point the paths at your own copy of the data. The generated figures are already committed in `output/figures/`.

## Hardware prototype

`output/stripboard/ASSEMBLY.md` gives the full pin map. Summary (ESP32 DevKit V1): SX1278 on SPI with SCK=GPIO18, MISO=GPIO19, MOSI=GPIO23, NSS=GPIO27, RST=GPIO14, DIO0=GPIO26; WANGCL piezo module AO on GPIO34 (sensing node only). Physical hardware verification is not yet complete. Read the assembly notes before building (power decoupling, antenna, copper-strip cuts).

## Status and known limits

- Layouts were verified by JSON parsing and schematic graph checks only; not by physical test.
- Packet size and node capacity are to be measured, not assumed.
- Real-RPW field recall is not claimed.

## Licensing

No license has been chosen for the original text and code, so default copyright applies. Several figures come from published papers, a university logo and personal photos (`output/figures/`, `output/AUSlogo.png`). They remain the property of their owners. Confirm permission or replace them before reuse.
