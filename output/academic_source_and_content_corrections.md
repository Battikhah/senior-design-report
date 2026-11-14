# Academic Source and Content Corrections

This register lists substantive corrections made while enhancing the requested sections. Routine grammar, punctuation, and sentence-simplification edits are not listed.

## Academic source corrections

1. **The 4 dB SNR threshold was cited to the wrong study.**
   - Original issue: the signal-processing and interface sections cited `wang2021` for a 4 dB threshold that produced 97 infestation alarms for an infested tree and 9 for a healthy tree.
   - Correction: the citation was changed to `ashry2020`. That paper reports the two-hour controlled experiment, the 4 dB threshold, and the 97-versus-9 alarm counts.
   - Source: https://doi.org/10.1038/s41598-020-60171-7

2. **TreeVibes performance values were mixed across studies and evaluation methods.**
   - Original issue: the literature review attributed 94.53% as the main InceptionResNet-V2 accuracy and attributed 97.38% to Boulila et al.
   - Correction: Karar et al. (2021) reported 97.18% on its train/test split and 94.53% +/- 1.69% under 10-fold cross-validation. The 97.38% result belongs to the later MixConvNet study by Karar et al. (2022), whose 10-fold result was 95.90% +/- 1.46%. The Boulila discussion now describes its feature-fusion findings without borrowing the MixConvNet value.
   - Sources: https://doi.org/10.32604/cmc.2021.019059, https://doi.org/10.1016/j.aej.2021.10.050, https://doi.org/10.1016/j.compag.2023.108154

3. **The TreeVibes labels were described too narrowly.**
   - Original issue: the dataset was presented as though its infested recordings were exclusively confirmed RPW signals.
   - Correction: the review now states that TreeVibes includes recordings of several wood-boring insects and that the RPW classifier study assumed infested date-palm recordings represented RPW activity. This limitation affects how model results should be interpreted.
   - Sources: https://doi.org/10.3390/smartcities4010017, https://doi.org/10.32604/cmc.2021.019059

4. **DAS laboratory, signal-level, and field claims were blended together.**
   - Original issue: the literature review presented high classification values as general field accuracy and described 1,000-tree operation as demonstrated deployment.
   - Correction: the revision distinguishes laboratory work using simulated sound, controlled and outdoor recordings with young larvae, signal-classification accuracy, and projected large-farm coverage. It no longer treats projected capacity as a validated 1,000-tree deployment or signal accuracy as whole-farm diagnostic accuracy.
   - Sources: https://doi.org/10.3390/s21051592, https://doi.org/10.3390/s22176491

5. **The molecular-marker sources did not support early diagnosis of hidden infestation.**
   - Original issue: population-genetics and ultrastructure studies were used to claim low-level tree diagnosis, rapid screening, and future portable detection.
   - Correction: the section now describes these studies as species/population characterization. Molecular analysis may confirm a collected biological sample, but the cited studies did not validate diagnosis from a living palm or an early-stage field assay.
   - Sources: https://doi.org/10.1016/j.sjbs.2021.05.078, https://doi.org/10.3390/d14050404

6. **The VOC biosensor was described as more specific and field-ready than the paper showed.**
   - Original issue: the text implied a targeted infestation-specific analyte, direct external detection, and readiness for continuous farm deployment.
   - Correction: the study is now described as a proof of concept using genetically modified bacterial stress reporters and controlled measurement. Field packaging, selectivity, lifetime, calibration, and false-positive performance remain unvalidated.
   - Source: https://doi.org/10.1016/j.jbiotec.2022.08.007

7. **Economic and social benefits were stated as guaranteed outcomes.**
   - Original issue: the report claimed that the proposed system would dramatically reduce costs, immediately offset its investment, eliminate recurring inspection labor, and reduce pesticide impacts.
   - Correction: these statements are now conditional benefits that require field and lifecycle evidence. Existing sources establish the scale of RPW damage and the promise of acoustic monitoring; they do not quantify savings, labor displacement, or pesticide reduction for this prototype.

## Design and internal-consistency corrections

1. **Non-invasive versus drilled installation.** The proposed metallic waveguide may require a small drilled mounting point. The system is now described as *minimally invasive*, while DAS remains the non-invasive approach.

2. **Continuous monitoring versus scheduled measurements.** The project uses scheduled daytime and nighttime wake-ups, not continuous node sampling or transmission. Claims of 24/7 monitoring were removed from descriptions of the proposed system.

3. **Unverified network scale.** The earlier claim that one SF7 cluster head supports 8,000 nodes with about 1 km field range was not backed by prototype measurements. It is now identified as a planning calculation. The requirements call for reporting measured airtime, packet loss, range, and supported prototype scale.

4. **Model validation leakage risk.** Grouped cross-validation was added so recordings or augmented copies from the same source tree/session cannot appear in both training and validation folds.

5. **Prototype BOM versus deployment cost.** The budget was renamed and scoped as a prototype estimate. It now explicitly excludes enclosure fabrication, PCB production, mounting hardware, solar charging, cloud/cellular service, labor, maintenance, delivery, and taxes.

6. **Duplicate storage cost.** The separate 32 GB microSD card was removed because the listed Raspberry Pi starter kit already includes a 64 GB card. The cluster-head subtotal changed from 745.62 AED to 680.62 AED, and the combined prototype total changed from 888.94 AED to 823.94 AED.

7. **Unsupported success thresholds.** Project-management text that treated greater than 97% accuracy as a required outcome was replaced with the stated evaluation priority: recall, supported by false-negative rate, precision, F1 score, and grouped cross-validation variability.

8. **Early-stage validation boundary.** TreeVibes does not provide the infestation-stage evidence needed to prove early-stage detection. The revised text prevents the project from claiming earlier detection unless larval age or infestation stage is independently documented.

## Source-package limitation

The original `References.bib` was later supplied separately and reconciled into the output package. The corrected bibliography contains all 26 original entries and covers all 25 citation keys used by the enhanced report. The synced source package still does not include the referenced figure files, so rebuilding the original 99-page layout requires those image assets.

## Bibliography reconciliation

1. Restored the full original metadata and the unused `alibob2019` entry.
2. Corrected the article numbers for `wang2021` (1592), `ashry2022cnn` (6491), `ding2025` (1266), and `na2024` (218).
3. Replaced abbreviated or malformed author fields in `karar2022` with the confirmed author names.
4. Changed `fonseca2018` from `@misc` to `@dataset`, restored the complete creator list, and used the Zenodo publication date of January 29, 2019.
5. Removed the non-resolving DOI from `saleem2022`, retained the publisher page, and documented the DOI-resolution issue in the entry note.
6. Restored the complete titles, scientific names, diacritics, publisher, conference series, volume, URLs, and version details that were shortened or lost in the reconstructed bibliography.

## 2026-09-07: Controlled mechanical-emulation and communication-efficiency additions

1. **Mechanical playback is a bench-validation method, not live RPW evidence.**
   - The report now uses Appel and Cocroft (2014) as evidence that piezoelectric actuators have been mechanically coupled to plant material for vibration playback, Escalante et al. (2024) as evidence of plant-coupled playback calibration, and Agis and Pozo (2020) only as a piezoelectric actuator--solid--sensor methodological parallel.
   - These papers do not validate RPW detection, palm measurements, or the proposed apparatus. A wood-plank result is now explicitly labelled as emulation/bench validation.
   - Sources: https://doi.org/10.1007/s00442-014-2995-6, https://doi.org/10.1093/jeb/voad010, https://doi.org/10.3390/s20061716

2. **The ±3 dB value is limited to the cited setup.**
   - Escalante et al. describe a compensating-filter target intended to keep frequency components within approximately ±3 dB at their target. The report does not present this as a universal playback-fidelity result.

3. **LoRa payload capacity is not fixed.**
   - The LoRa Alliance regional-parameters specification establishes that payload limits vary with the region and data rate. The report therefore requires measured payload bytes and airtime instead of claiming a universal capacity.
   - Source: https://resources.lora-alliance.org/technical-specifications/rp002-1-0-4-regional-parameters

4. **Split learning is an investigation, not a guaranteed bandwidth reduction.**
   - Duan et al. (2022) supports split learning as an edge-IoT topic with communication trade-offs. The revised report explicitly requires a comparison against compact feature packets because intermediate activations can be larger.
   - Source: https://doi.org/10.3390/s22165983

5. **No new empirical result is claimed.**
   - The report adds planned measures---playback fidelity, SNR versus distance, recall versus distance/noise, precision, recall, F1, payload bytes, airtime, packet loss, energy, and ESP32 resource use---but reports no measured performance values. Live detection may be claimed only after tests on naturally infested palms; if access is unavailable, the fallback is explicitly limited to emulation.
