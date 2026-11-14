# Senior Design stripboard prototypes

These projects assume a **30-pin ESP32 DevKit V1** carrying ESP32-WROOM. Confirm your board labels and header spacing before assembly. SX1278 and WANGCL modules attach through labeled 2.54 mm harness connectors; the connector order is deliberate and is not a claim about either module's physical pin order.

| Interface | ESP32 |
|---|---|
| SX1278 VCC | 3V3 |
| SX1278 GND | common GND |
| SX1278 SCK | GPIO18 |
| SX1278 MISO | GPIO19 |
| SX1278 MOSI | GPIO23 |
| SX1278 NSS / CS | GPIO27 |
| SX1278 RST | GPIO14 |
| SX1278 DIO0 | GPIO26 |
| WANGCL VCC (sensing only) | 3V3 |
| WANGCL GND (sensing only) | common GND |
| WANGCL AO (sensing only) | GPIO34 |

Use USB power for the ESP32 development board. Confirm its regulator can supply the combined ESP32 and LoRa peak current. Keep the LoRa harness short. Fit **100 nF ceramic + 100 µF electrolytic (at least 6.3 V rating)** directly across the SX1278 VCC and GND terminals. Electrolytic positive goes to 3V3. The correct antenna connects directly to the radio, before transmitting. Leave unused DIO pins and sensor DO disconnected.

Confirm the exact WANGCL module supports 3.3 V operation and measure AO before attaching it to GPIO34. No raw piezo disc should connect directly to the ADC in place of the module.

The layout is for horizontal copper-strip board, viewed from the component side. Ordinary isolated-pad perfboard has different copper connectivity. Make every indicated cut; inspect both sides and check continuity plus absence of supply shorts before powering.

Verification at this stage: JSON parsing, expected net membership, and a schematic graph check that detects unintended pin or wire-end junctions. Physical hardware has not been tested. Final native-editor routing verification is recorded separately after import.
