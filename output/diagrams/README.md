# Section 4 diagrams: integrated system

`Senior_Design_Section4_EdgeML.drawio.xml` is the editable source. Open it in diagrams.net; each report figure has its own page. The original file in Downloads is unchanged.

| Report figure | draw.io page | PDF imported by the report |
|---|---|---|
| 4.1 | System Block Diagram | `../figures/system_fig_diagram.pdf` |
| 4.2 | Sensing Node: Full Connections | `../figures/sensing_node_full_schematic_edge.pdf` |
| 4.5 | Three-Tier Node Architecture | `../figures/3Node_Arch.pdf` |
| 4.6 | Class Architecture (Conceptual) | `../figures/Class_Architecture_edge.pdf` |
| 4.7 | Result-Centred Data Architecture | `../figures/ER_Diagram.pdf` |
| 4.8 | Sensing Layer Operational Flow | `../figures/Sensing_layer_flowchart.pdf` |
| 4.9 | Cluster Layer Operational Flow | `../figures/Cluster_layer_flowchart.pdf` |
| 4.10 | Edge Inference and Alternative Feature Codec | `../figures/codec_current_pipeline.pdf` |

The seven architecture and flow figures depict the current integrated path: WANGCL / MCP602E, ESP-IDF acquisition and stream1s_w8_d4 inference, single-result 13-byte LoRa DATA sessions, Arduino cluster head with a 512-record volatile RAM queue, and hosted NAKHEL ingestion / PostgreSQL / worker / Next.js dashboard. They are illustrative architecture, not measurements. The class and data pages describe conceptual responsibilities and logical relationships, not an exact code-class or SQL schema inventory. The MFCC Rice codec is a separate study that the current head does not accept; an embedded round trip remains pending.

## Rebuild

From the repository root, using Python with `reportlab` installed and Poppler's `pdftoppm` on PATH:

```sh
python3 output/build_integrated_architecture_figures.py
```

The builder reads these seven draw.io pages directly and exports vector PDF plus matching 160 dpi PNG files. It also refreshes the existing `sensing_layer.png` and `cluster_layer.png` companion previews. It asserts text fits inside boxes and that boxes fit inside the canvas. No TeX files are modified. The electrical schematic page and its exports are left alone.

The builder supports the simple subset used here: rectangular text nodes, explicit `<br>` line breaks, solid or dashed borders, and orthogonal directed connections. Keep edits within this subset, or extend the renderer before adding other draw.io shapes. Preserve black/grey text, a white background, and legibility at report width. Render and visually review all seven outputs after edits.
