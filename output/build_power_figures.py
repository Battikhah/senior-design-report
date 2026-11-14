"""Reproduce report power plots from the supplied measurement files."""
from pathlib import Path
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from zipfile import ZipFile
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parent
source = Path('/Users/khalidhamdan/Downloads/FuckSenior')
figures = root / 'figures'
figures.mkdir(exist_ok=True)
with (source / 'EverythingElse.csv').open() as stream:
    readings = list(csv.DictReader(stream))
# Keep one standby entry and use the project's current ESP32-inclusive values.
readings = [r for r in readings if not (r['mode'] == 'radio_idle' and r['run'] == '2')]
assert [float(r['current_ma_representative']) for r in readings] == [40, 50, 60, 40, 40]
for reading, current in zip(readings, [33, 42, 53, 33, 33]):
    reading['current_ma_representative'] = str(current)
with ZipFile(source / 'LoRa_Power_Consumption(3.3V).xlsx') as archive:
    sheet = ET.fromstring(archive.read('xl/worksheets/sheet1.xml'))
ns = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
rows = [[float(c.find('s:v', ns).text) for c in row.findall('s:c', ns)]
        for row in sheet.findall('s:sheetData/s:row', ns)[1:]]
for tx, current, power, energy, packet, byte in rows:
    assert abs(power - 3.3 * current) < 1e-8
    assert abs(energy - power * 42 / 1000) < 1e-8
    assert abs(packet - energy) < 1e-8
    assert abs(byte - packet / 9) < 1e-8
plt.rcParams.update({'font.size': 10, 'pdf.fonttype': 42})
fig, ax = plt.subplots(figsize=(6.5, 3.4), layout='constrained')
ax.plot([r[0] for r in rows], [r[2] for r in rows], marker='o', color='#246184')
ax.set(xlabel='Configured TX power (dBm)', ylabel='Calculated power at 3.3 V (mW)', xticks=[r[0] for r in rows])
ax.grid(alpha=.25)
fig.savefig(figures / 'lora_power_sweep.pdf')
fig.savefig(figures / 'lora_power_sweep.png', dpi=180)
plt.close(fig)
fig, ax = plt.subplots(figsize=(6.5, 3.6), layout='constrained')
labels = ['Idle', 'Sensing', 'CNN active', 'CNN idle', 'Radio standby']
totals = [float(r['current_ma_representative']) for r in readings]
increments = [total - 33 for total in totals]
assert totals == [33, 42, 53, 33, 33]
assert increments == [0, 9, 20, 0, 0]
ax.barh(labels, [33]*len(labels), color='#a4bac5', label='ESP32-inclusive idle baseline')
ax.barh(labels, increments, left=33, color='#246184', label='Estimated increment above idle')
for i, value in enumerate(increments):
    ax.text(totals[i]+1, i, f'{totals[i]:g} (+{value:g})', va='center', fontsize=9)
ax.legend(fontsize=8, loc='lower right')
ax.invert_yaxis()
ax.set(xlabel='Total current (mA)', xlim=(0, 70))
ax.grid(axis='x', alpha=.25)
fig.savefig(figures / 'operating_mode_current.pdf')
fig.savefig(figures / 'operating_mode_current.png', dpi=180)
plt.close(fig)
print('Verified 4 LoRa calculation rows; plotted 5 operating conditions.')
