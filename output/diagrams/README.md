# Section 4 diagrams: edge ML

Open `Senior_Design_Section4_EdgeML.drawio.xml` in diagrams.net. Each report figure has its own editable page. The original file in Downloads was left unchanged.

| Report figure | draw.io page | PDF imported by the report |
|---|---|---|
| 4.1 | System Block Diagram | `../figures/system_fig_diagram.pdf` |
| 4.2 | Sensing Node: Full Connections | `../figures/sensing_node_full_schematic_edge.pdf` |
| 4.3 | Three-Tier Node Architecture | `../figures/3Node_Arch.pdf` |
| 4.4 | Class Architecture (Conceptual) | `../figures/Class_Architecture_edge.pdf` |
| 4.5 | Result-Centred Data Architecture | `../figures/ER_Diagram.pdf` |
| 4.6 | Sensing Layer Operational Flow | `../figures/Sensing_layer_flowchart.pdf` |
| 4.7 | Cluster Layer Operational Flow | `../figures/Cluster_layer_flowchart.pdf` |
| 4.8 | Edge Inference and Alternative Feature Codec | `../figures/codec_current_pipeline.pdf` |

The PDF exports are vector diagrams; the supplied electrical schematic remains an embedded raster image with an added software-role note. Its wires and component values were not changed. New captions and directly related report text use the existing green revision macro.

The selected path runs inference on the sensing ESP32 and forwards a result. The head validates and queues packets, then uploads them over Wi-Fi. LoRa acceptance and computer persistence have different boundaries. Acquisition/model integration still needs validation. Class and database diagrams describe conceptual responsibilities and logical records, not exact source-code classes or SQL columns. The MFCC codec remains a separate investigation.

To revise a figure, edit its page and export that page as PDF using the mapped filename. Preserve a white background and legible text. Matching PNG previews use the same stem; `sensing_layer.png` and `cluster_layer.png` are companion previews of the flowcharts. Rebuild the report from `output/` and inspect affected pages before committing.
