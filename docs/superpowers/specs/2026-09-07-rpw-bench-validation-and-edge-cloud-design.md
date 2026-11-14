# RPW Bench Validation and Edge-Cloud Design

## Purpose

Extend the Senior Design report without changing its central goal: a low-cost IoT system for earlier acoustic/vibration-based screening of red palm weevil (RPW) activity. The report will add packet compaction and split learning as research investigations and define a defensible bench-validation method.

## Evidence Boundary

The project has two validation stages.

1. **Controlled bench emulation.** An RPW recording is converted to a mechanical vibration and propagated through wood to the sensing node. This stage validates signal injection, propagation, acquisition, preprocessing, packet design, and classification under controlled conditions.
2. **Live-RPW validation, if access is obtained.** Tests on naturally infested palms evaluate the same system with real biological activity.

If access to naturally infested palms is not obtained, the report must state that the work validates emulated vibration propagation and detection only. It must not claim real RPW detection, field recall, or early-stage biological detection.

## Bench Method

The signal path is:

`RPW recording -> amplifier -> mechanically coupled vibration exciter -> wood -> piezoelectric reference sensor and measurement sensor -> MCP6002 -> ESP32 -> filtering/MFCC -> classifier`

The exciter is mechanically attached to the wood rather than playing sound through air. The reference sensor sits near the exciter and measures the injected vibration. The measurement sensor is placed at the tested distance and measures propagated vibration.

The bench matrix varies source-to-sensor distance, playback amplitude, and controlled background vibration/noise level. For each condition, the project records playback fidelity, SNR versus distance, classifier recall versus distance/noise, and precision, recall, and F1 score. A condition is reported separately rather than pooled without its distance and noise level.

## Edge-Cloud Investigations

### Packet compaction

The team will compare a baseline feature packet with compact representations that may include quantized MFCCs, delta or run-length encoding where appropriate, compact timestamp and identifier fields, and a versioned binary packet format. It will report payload bytes, airtime, packet-loss rate, energy use, and classification change. The report must not assume a fixed 214-byte packet or a fixed node capacity before measurement.

### Split learning

The team will investigate a candidate split point after an ESP32-feasible preprocessing or lightweight neural layer. The sensing node will send either the compact feature packet or an activation representation to the cloud, where the remaining model runs. The baseline cloud classifier remains available. Split learning is retained only if its measured payload, runtime, memory use, energy use, and detection metrics are acceptable; it is not described as automatically reducing traffic because activation tensors can be larger than compact MFCC packets.

## Report Changes

The following sections will be updated: Problem Statement, Literature Survey, Functional and Non-Functional Requirements, Cost Analysis, Project Management, and Social Impact. To keep the report internally consistent, Technical Approach, Testing/Validation, Performance Analysis, and Risk Analysis will also be updated.

## Revision Marking

The LaTeX source will define two macros:

- `\earlierrevision{...}`: blue text for all earlier edits made during this conversation.
- `\newrevision{...}`: green text for this extension.

Unchanged original text remains black. The bibliography remains uncoloured. The visual review PDF, if rebuilt without the original figure assets, remains labelled as using placeholders for missing figures.

## Cost Treatment

The cost analysis will add a separate provisional bench-validation line for a vibration exciter, amplifier, reference piezo sensor, mounting/coupling material, and wood test specimen. No unsupported AED total will be presented; vendor selection and quotations are required before a final purchase total is stated.

## Project Gates

1. Verify the bench apparatus with the reference sensor and report playback fidelity.
2. Run the controlled distance, amplitude, and noise matrix.
3. Compare baseline, compact-packet, and candidate split-learning paths against the same test conditions.
4. Proceed to live-RPW validation only if access to naturally infested palms is obtained and relevant approvals/safety procedures are in place.

## Credible Sources to Add

- Appel, H. M., and R. B. Cocroft. 2014. *Plants respond to leaf vibrations caused by insect herbivore chewing*. Oecologia 175(4):1257–1266. DOI: 10.1007/s00442-014-2995-6. Uses piezoelectric vibration playback mechanically coupled to a leaf.
- Escalante, I., et al. 2024. *On the function of a female-like signal type in the vibrational repertoire of Enchenopa male treehoppers*. Journal of Evolutionary Biology 37(1):110–122. DOI: 10.1093/jeb/voad010. Calibrates transmitted multicomponent playback components within ±3 dB.
- Agis, D., and F. Pozo. 2020. *Vibration-Based Structural Health Monitoring Using Piezoelectric Transducers and Parametric t-SNE*. Sensors 20(6):1716. DOI: 10.3390/s20061716. Demonstrates piezoelectric transducers operating as exciters and sensors on a solid structure.
- Duan, Q., S. Hu, R. Deng, and Z. Lu. 2022. *Combined Federated and Split Learning in Edge Computing for Ubiquitous Intelligence in Internet of Things*. Sensors 22(16):5983. DOI: 10.3390/s22165983. Reviews split learning in constrained IoT settings and its communication trade-offs.
- LoRa Alliance. 2023. *RP002-1.0.4 Regional Parameters*. Official LoRaWAN regional-parameter specification. Payload constraints depend on region and data rate.
