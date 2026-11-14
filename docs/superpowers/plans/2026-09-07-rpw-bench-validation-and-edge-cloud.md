# RPW Bench Validation, Communication Efficiency, and Revision Marking Plan

> **For implementation:** carry out this plan inline in the shared project workspace. The project is not a Git repository, so no branch or commit step is available.

**Goal:** Update the enhanced RPW report without changing its central aim: clearly separate controlled mechanical emulation from live RPW validation; add packet-compaction and split-learning investigations; cite credible sources; and show existing revisions in blue and this extension in green.

**Source of truth:**
- Original report (read-only): `sources/main.tex`
- Working report: `output/senior_design_report_enhanced.tex`
- Working bibliography: `output/References.bib`
- Existing correction log: `output/academic_source_and_content_corrections.md`

## Marking convention

- Keep unchanged original material black.
- Add `\earlierrevision{...}` for all prose, headings, table entries, and factual corrections already made in the enhanced report. This macro renders blue.
- Add `\newrevision{...}` for every addition or replacement made for this request. This macro renders a readable dark green.
- Do not colour bibliography entries. They remain a clean reference list.
- Deleted original text cannot appear in the final PDF; the surrounding replacement text is marked in the appropriate revision colour.

## 1. Add source-backed bibliography records

**Files:** `output/References.bib`, `output/academic_source_and_content_corrections.md`

1. Add these records, using stable, credible primary or peer-reviewed sources:
   - `appel2014`: Appel and Cocroft (2014), *Oecologia*, mechanically coupled piezoelectric replay of herbivore-induced vibrations.
   - `escalante2024`: Escalante et al. (2024), *Journal of Evolutionary Biology*, plant-coupled vibrational playback and reported signal reproduction within approximately ±3 dB across the calibrated band.
   - `agis2020`: Agis and Pozo (2020), *Sensors*, piezoelectric actuator-to-solid-to-sensor structural-health-monitoring precedent.
   - `duan2022`: Duan et al. (2022), *Sensors*, peer-reviewed edge-IoT review of federated and split learning, including communication bottlenecks.
   - `lorawan2023`: LoRa Alliance RP002-1.0.4 regional-parameters specification, used only for the fact that payload constraints depend on region and data rate.
2. Record in the corrections log that these support the new experimental method and are not evidence that a wood-plank test detects live RPW larvae.

## 2. Establish the visible revision system and mark earlier work

**File:** `output/senior_design_report_enhanced.tex`

1. Define `\earlierrevision` and `\newrevision` in the preamble, using the already loaded `xcolor` package.
2. Compare the working report against `sources/main.tex` and wrap every retained earlier change in `\earlierrevision{...}`. This includes the earlier grammar simplifications, corrected claims, requirements wording, cost corrections, project-management clarifications, social-impact revisions, and revised section title.
3. Keep LaTeX commands structurally valid: wrap complete paragraphs, list items, table cells, or headings rather than placing colour macros through an environment boundary.

## 3. Add green content to the required report sections

**File:** `output/senior_design_report_enhanced.tex`

### Problem Statement

1. State that the project will evaluate efficient transmission rather than assume that raw or fixed-size feature packets are suitable for LoRa.
2. Define the real-world evidence boundary: a mechanically excited material test is bench validation; only tests with naturally RPW-infested palms may support a live-detection claim.
3. State the fallback: if access to such palms is unavailable, the project will perform emulation and label conclusions accordingly.

### Literature Survey

1. Add a concise vibrational-playback subsection. Cite Appel and Cocroft for mechanical coupling to plant material; cite Escalante et al. for calibrated plant-coupled playback and fidelity; cite Agis and Pozo only as a solid-material piezo actuator/sensor methodological parallel.
2. Add a concise communication-efficiency subsection. Cite the LoRa Alliance specification for region/data-rate-dependent payload limits, then state the project will measure actual payload and airtime rather than presume a universal limit.
3. Add a concise split-learning subsection. Cite Duan et al., state the sensing-side/cloud partition will be investigated, and explicitly note that intermediate activations can be larger than compact features, so traffic reduction must be measured rather than claimed in advance.

### Requirements

1. Add functional requirements for a versioned compact binary packet, packet-size/airtime logging, and a baseline-versus-compacted feature comparison.
2. Add functional requirements for the bench apparatus: RPW recording, suitable amplifier, mechanically attached vibration exciter, wood specimen, piezo sensor, MCP6002, ESP32, filtering/MFCC/classifier, and a second reference piezo sensor near the exciter.
3. Add requirements to vary source-to-sensor distance, playback amplitude, and controlled noise/SNR; record conditions and metrics for every run.
4. Add a split-learning investigation requirement: compare the normal compact-feature packet with one candidate split point only when the ESP32 memory/runtime and measured uplink cost are acceptable.
5. Add a validation gate requiring explicit lab-emulation labeling unless naturally infested palms are tested.

### Technical Approach, Validation, and Performance Analysis

1. Add the bench path exactly as: recording -> amplifier -> mechanically coupled vibration exciter -> wood/palm material -> piezo measurement -> MCP6002 -> ESP32 -> filtering/MFCC/classifier.
2. Explain the role of the reference sensor: it measures the injected vibration; the distant sensor measures the propagated vibration.
3. Specify the phased material plan as wood plank first, then real palm material only where available. Do not include a palm-trunk-section stage.
4. Define the controlled experiment matrix: distance, amplitude, and added background vibration/noise/SNR. Preserve existing performance targets rather than invent results.
5. Define required reported measures: playback fidelity, SNR versus distance, detection recall versus distance/noise, and classifier precision, recall, and F1.
6. Specify that compact-packet experiments compare baseline and quantized MFCC variants, optional delta/run-length coding when beneficial, compact metadata, and a versioned binary layout. Report payload bytes, airtime, packet loss, energy, and classification change.
7. Specify that the split-learning comparison reports the same communication measures plus ESP32 runtime and memory, and retains the split only if it meets the stated resource and detection criteria.

### Cost Analysis

1. Preserve the existing prototype total; do not invent prices or alter it without supplier quotations.
2. Add a green procurement note identifying required bench-validation items not included in that total: vibration exciter, suitable amplifier, second piezo sensor, attachment/coupling hardware, and a wood specimen.
3. State that these items require quotations and must be costed before purchase.

### Project Management

1. Add green milestones for apparatus assembly/calibration, controlled wood-plank trials, packet-compaction comparison, split-learning feasibility comparison, and a final live-palm validation gate where access permits.
2. State the fallback decision: complete the emulation evaluation and report it as bench validation if naturally infested palms are unavailable.

### Social Impact and Risk Analysis

1. Add green social-impact text explaining that transparent lab-versus-field labeling avoids overclaiming and reduces the risk of a false management decision, including unnecessary treatment.
2. Add green risks and mitigations: coupling/calibration error, degradation with distance/noise, absence of infested palms, constrained LoRa payload, and a split point that raises rather than reduces transmission cost.

## 4. Update the correction record

**File:** `output/academic_source_and_content_corrections.md`

1. Add a dated section documenting the new sources and their limited, accurate purpose.
2. Explain that the current plan does not claim empirical performance values, live detection, a fixed LoRa payload capacity, or a guaranteed split-learning bandwidth reduction.
3. Retain all prior correction entries.

## 5. Verify the report

1. Check that every new citation key occurs in `output/References.bib` and every cited key resolves through Biber.
2. Compile the working report in a temporary build directory using `pdflatex`, `biber`, then `pdflatex` twice.
3. Inspect the log for undefined citations, undefined references, and colour/macro errors.
4. Verify that blue and green revision macros appear in the required sections and that bibliographic entries are not colour-wrapped.
5. Render the revised PDF if all required image assets are available. If source figures are still unavailable, state clearly that Biber/LaTeX checks passed but full visual PDF verification is limited by those missing assets.
