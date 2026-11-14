"""Validate communication counts and plot the supplied run-level log."""
from pathlib import Path
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root = Path(__file__).resolve().parent
with Path('/Users/khalidhamdan/Downloads/Com Logs.csv').open(encoding='utf-8-sig') as f:
    rows = [{k: float(v) for k, v in r.items()} for r in csv.DictReader(f)]
assert len(rows) == 50
for r in rows:
    assert r['initial_unique'] + r['initial_missing'] == r['requested_packets']
    assert r['initial_unique'] + r['arq_recovered'] == r['final_unique']
    assert r['final_unique'] + r['final_missing'] == r['requested_packets']
    assert abs(r['initial_loss_pct'] - 100*r['initial_missing']/r['requested_packets']) < 1e-9
    assert r['final_missing'] == r['duplicates'] == r['local_failed_skipped'] == 0
assert sum(r['initial_missing'] for r in rows) == 290
assert sum(r['arq_tx_done'] for r in rows) == 290
fig, axes = plt.subplots(2, 1, figsize=(7, 4.6), sharex=True, layout='constrained')
x = list(range(1, 51))
axes[0].plot(x, [r['initial_loss_pct'] for r in rows], marker='.', color='#246184', label='Initial loss')
axes[0].plot(x, [r['final_loss_pct'] for r in rows], color='#56915d', label='Final loss after ARQ')
axes[0].set(ylabel='Packet loss (%)', ylim=(-.12, 2.5))
axes[0].legend(fontsize=8)
axes[1].plot(x, [r['observation_s'] for r in rows], marker='.', color='#246184')
axes[1].set(ylabel='Observation duration (s)', xlabel='Run (CSV row order)')
for ax in axes:
    ax.grid(alpha=.2)
for ext in ['pdf', 'png']:
    fig.savefig(root / 'figures' / f'communication_runs.{ext}', dpi=180)
print('Validated 50 runs: 50,000 requested, 290 recovered, zero final missing.')
