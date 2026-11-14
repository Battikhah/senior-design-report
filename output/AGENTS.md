# Senior Design report instructions

## Start here

Edit `senior_design_report_enhanced.tex` and its included section files in this directory. Read the root README for the file map and build command. Preserve files under `../sources/` as read-only references. The template-aligned report, older `mfcc_compression.tex`, exploratory codec plots, correction register, and early plans are historical; verify them against the current report before reuse.

## Editing rules

- Make the smallest supported change, using simple language and preserving the RPW detection goal. Preserve the literature review unless the user specifically authorizes its revision.
- Preserve the revision scheme: earlier edits use `\earlierrevision{...}` (blue), newer edits use `\newrevision{...}` (green). Apply it to new text and tables; keep diagrams legible.
- Put system/codec specifications in Technical Approach; confirmed build status in Implementation; measured/offline results in Preliminary Results; procedures and acceptance checks in Validation; exact schedule vectors in the appendix.
- Distinguish proposed, team-reported, offline-measured, and hardware-validated claims. Retain unresolved fields instead of inventing values. Report substantive source or idea corrections to the user.
- Use credible primary sources for added academic claims. Project measurements are project evidence, not independent literature. Check bibliography keys and preserve citation provenance.

## Facts and boundaries to preserve

- Surface-contact WANGCL sensor pressed by a plate; MCP602E conditioning; sensing ESP32; 433 MHz SX1278; second ESP32 forwards LoRa packets to the server over Wi-Fi. The full schematic uses a 38-pin board; earlier 30-pin stripboard layouts need reconciliation.
- Radio-log settings: SF7, 125 kHz, CR 4/5, configured TX power 10 dBm, spring antennas. Partially obstructed tests reached 350 m. Runs lack a distance mapping, so aggregate delivery cannot be assigned specifically to 350 m.
- Communication-test packets are eight-byte synthetic records. They are separate from the specified compressed-feature payload with its six-byte header and three-bit schedule index.
- Codec: 15 × 13 int8 MFCC values, first-frame anchor, 182 temporal deltas, ZigZag, static ordered eight-schedule Rice bank. Quantization is lossy; exact reconstruction refers to quantized values and scale. Current layout leaves date/battery meanings and version identification unresolved. Do not add an assumed CRC or bounded-Rice escape format.
- Offline compression summaries pool all splits and exclude eight metadata bytes. They are not held-out generalization or verified on-air sizes; do not add six bytes to them without confirming compatible accounting. The exact firmware bank is not verified as identical to the named Field-only 8 CSV variant.
- Offline feature preparation omits SNR gating and signal squaring; older operational flowcharts include them. Firmware numerical equivalence is pending.
- Idle/sensing/CNN-active currents are 33/42/53 mA, including ESP32 and connected loads. Use the current power section's eight-byte energy accounting. Do not reintroduce the superseded meter-offset or 10 mA display-step explanation.
- Playback is mechanical exciter → material → contact sensor. Emulation is the fallback if infested palms are unavailable, and is bench validation rather than proof of live-RPW detection.
- TreeVibes is used for model development. Final classifier, embedded codec performance, end-to-end cloud operation, and biological validation remain pending. Solar is a future option, not purchased hardware.

## Verification and publication

Build from this directory with `latexmk -pdf -interaction=nonstopmode -halt-on-error senior_design_report_enhanced.tex`. For non-MacTeX installations use `-norc` and TeX tools on PATH. Check the final log for missing citations/references and errors; render and inspect pages affected by layout changes. Commit the rebuilt PDF with its source changes and summarize exactly what was checked.

Keep receipts, banking details, credentials, private correspondence, and temporary build outputs out of this public repository. Inspect staged files before pushing. Preserve other contributors' edits; flag conflicting evidence instead of silently choosing a result.
