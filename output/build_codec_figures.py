"""Draw codec diagrams and reported packet sizes from supplied project notes."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

dest = Path(__file__).resolve().parent / 'figures'
fig, ax = plt.subplots(figsize=(8, 5.1), layout='constrained')
ax.set(xlim=(0, 10), ylim=(0, 10))
ax.axis('off')
left = ['10 s audio at 8 kHz', 'MFCC + temporal pooling\n15 × 13 float matrix', 'Quantize: 195 int8 values\n+ exact float32 scale', 'Keep frame 0 (13 bytes)\n182 temporal deltas', 'Zigzag + bounded Rice\nVersion, schedule, bits, CRC']
right = ['Approximate MFCCs\nfor agreed classifier input', 'Exact 15 × 13 int8 matrix\n+ exact scale bytes', 'Cumulative reconstruction\nfrom frame 0 + deltas', 'Rice decode + inverse zigzag\n182 temporal differences', 'Receive and validate\npacket and schedule']
for x, texts in [(0.1, left), (5.6, right)]:
    for i, text in enumerate(texts):
        y = 8.2 - i * 1.8
        ax.add_patch(FancyBboxPatch((x, y), 4.2, 1.25, boxstyle='round,pad=.08', facecolor='#eaf2f6', edgecolor='#246184'))
        ax.text(x + 2.1, y + .625, text, ha='center', va='center', fontsize=10)
        if i < 4:
            start, end = ((x+2.1,y-.08),(x+2.1,y-.47)) if x < 1 else ((x+2.1,y-.47),(x+2.1,y-.08))
            ax.annotate('', xy=end, xytext=start, arrowprops={'arrowstyle':'->','color':'#246184'})
ax.annotate('', xy=(5.5,1.625), xytext=(4.4,1.625), arrowprops={'arrowstyle':'->','color':'#246184'})
ax.text(5, 2.35, 'LoRa\nbytes', ha='center', fontsize=9)
for ext in ['pdf','png']:
    fig.savefig(dest / f'mfcc_codec_pipeline.{ext}', dpi=180)
plt.close(fig)
fig, ax = plt.subplots(figsize=(6.5,3.6), layout='constrained')
x = range(3)
means = [59.68,80.40,72.16]
p99 = [65,103,98]
ax.bar([i-.18 for i in x], means, width=.36, label='Reported mean', color='#246184')
ax.bar([i+.18 for i in x], p99, width=.36, label='Reported p99', color='#83b5c9')
ax.axhline(209, linestyle='--', color='#555555', label='Raw experimental packet: 209 B')
ax.set(xticks=list(x), xticklabels=['LAB','FIELD','FARM-LIKE proxy'], ylabel='Complete experimental packet (bytes)', ylim=(0,250))
ax.legend(fontsize=8, loc='upper left')
ax.grid(axis='y', alpha=.2)
for ext in ['pdf','png']:
    fig.savefig(dest / f'mfcc_packet_comparison.{ext}', dpi=180)
plt.close(fig)
print('Generated codec pipeline and packet-size comparison.')
