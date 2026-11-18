"""Render edge-inference work packages and the report's existing planning dates."""

import calendar
from datetime import datetime
from pathlib import Path
import re
import subprocess

from reportlab.lib import colors
import reportlab
from reportlab.pdfbase.pdfmetrics import registerFont, stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parent
FIGURES = ROOT / 'figures'
INK = colors.HexColor('#333333')
LINE = colors.HexColor('#808080')
FONT = 'VeraSans'
registerFont(TTFont(FONT, str(Path(reportlab.__file__).parent / 'fonts' / 'Vera.ttf')))


def write_lines(page, lines, x, y, font_size, centered=False):
    page.setFillColor(INK)
    page.setFont(FONT, font_size)
    for index, line in enumerate(lines):
        baseline = y - index * font_size * 1.25
        if centered:
            page.drawCentredString(x, baseline, line)
        else:
            page.drawString(x, baseline, line)


def work_package(name, title, tasks):
    width = 600
    height = 132 + ((len(tasks) + 1) // 2) * 78
    page = canvas.Canvas(str(FIGURES / f'{name}.pdf'), pagesize=(width, height))
    page.setTitle(' '.join(title))
    page.setStrokeColor(LINE)
    page.setLineWidth(1.4)
    page.roundRect(170, height - 78, 260, 58, 4, stroke=1, fill=0)
    write_lines(page, title, 300, height - 42, 17, centered=True)
    spine_top = height - 78
    spine_bottom = height - 116 - ((len(tasks) - 1) // 2) * 78
    page.line(300, spine_top, 300, spine_bottom)
    for index, task in enumerate(tasks):
        x = 14 if index % 2 == 0 else 326
        y = height - 146 - index // 2 * 78
        page.line(264 if index % 2 == 0 else 300, y + 30, 300 if index % 2 == 0 else 326, y + 30)
        page.roundRect(x, y, 250, 60, 4, stroke=1, fill=0)
        top = y + 34 + (len(task) - 1) * 10
        write_lines(page, task, x + 125, top, 16, centered=True)
    page.save()


def schedule():
    text = (ROOT / 'senior_design_report_enhanced.tex').read_text()
    table = text.split('\\label{tab:gantt}', 1)[1].split('\\end{longtable}', 1)[0]
    rows = []
    for line in table.splitlines():
        fields = line.split(' & ')
        if len(fields) != 4 or not re.fullmatch(r'[A-Z][a-z]{2} \d+ -- [A-Z][a-z]{2} \d+', fields[1]):
            continue
        label = fields[0].replace('\\newrevision{', '').replace('}', '')
        label = label.replace('\\&', '&').replace('$\\leftrightarrow$', '<->')
        label = label.replace('---', '-').replace('$<$', '<').replace('\\%', '%')
        start, end = [datetime.strptime(day + ' 2026', '%b %d %Y') for day in fields[1].split(' -- ')]
        rows.append((label, fields[2], start, end))
    if len(rows) != 34:
        raise ValueError(f'Expected the 34 existing schedule tasks, found {len(rows)}')

    width, height = 1120, 510
    page = canvas.Canvas(str(FIGURES / 'edge_project_schedule.pdf'), pagesize=(width, height))
    page.setTitle('Original project schedule with edge-inference tasks')
    left, task_width, lead_width = 15, 395, 90
    chart_x = left + task_width + lead_width
    chart_width = width - chart_x - 16
    top, header_height, row_height = height - 20, 46, 24
    first, last = datetime(2026, 1, 1), datetime(2026, 7, 1)
    date_x = lambda day: chart_x + (day - first).days / (last - first).days * chart_width
    for first_row in (0, 17):
        section = rows[first_row:first_row + 17]
        bottom = top - header_height - len(section) * row_height
        page.setFillColor(colors.HexColor('#EAEAEA'))
        page.rect(left, top - header_height, width - 31, header_height, fill=1, stroke=0)
        write_lines(page, ['Task / deliverable'], left + 5, top - 26, 12)
        write_lines(page, ['Lead'], left + task_width + 5, top - 26, 12)
        for month in range(1, 7):
            start = datetime(2026, month, 1)
            finish = datetime(2026, month + 1, 1)
            midpoint = (date_x(start) + date_x(finish)) / 2
            write_lines(page, [calendar.month_abbr[month] + ' 2026'], midpoint, top - 17, 11, centered=True)
            write_lines(page, ['1'], date_x(start) + 4, top - 36, 9)
        for index, (label, lead, start, end) in enumerate(section):
            y = top - header_height - (index + 1) * row_height
            if index % 2 == 0:
                page.setFillColor(colors.HexColor('#F5F5F5'))
                page.rect(left, y, width - 31, row_height, stroke=0, fill=1)
            size = min(12, (task_width - 10) / stringWidth(label, FONT, 1))
            write_lines(page, [label], left + 5, y + 7, size)
            write_lines(page, [lead], left + task_width + 5, y + 7, 11)
            x = date_x(start)
            bar_width = max(3, date_x(end) - x)
            page.setFillColor(colors.HexColor('#333333'))
            page.roundRect(x, y + 6, bar_width, 12, 2, stroke=0, fill=1)
        page.setStrokeColor(colors.HexColor('#D5D5D5'))
        page.setLineWidth(0.5)
        for month in range(1, 7):
            x = date_x(datetime(2026, month, 1))
            page.line(x, top, x, bottom)
        page.setStrokeColor(LINE)
        for x in (left, left + task_width, chart_x, width - 16):
            page.line(x, bottom, x, top)
        page.line(left, bottom, width - 16, bottom)
        page.showPage()
    page.save()


work_package('WP2', ['Acoustic Sensing Unit'], [
    ['Piezoelectric sensor', 'prototyping'],
    ['Surface-contact', 'mounting'],
    ['Signal acquisition', 'and ADC checks'],
    ['Bandpass filtering', 'and input conditioning'],
    ['Controlled laboratory', 'signal validation'],
])
work_package('WP3', ['Wireless Sensor Network'], [
    ['LoRa result framing', 'and radio configuration'],
    ['Delivery acknowledgments', 'and retry handling'],
    ['Cluster-head Wi-Fi', 'result forwarding'],
    ['Power and enclosure', 'integration'],
    ['Prototype network', 'delivery tests'],
])
work_package('WP4', ['Deep Learning Classifier'], [
    ['Labeled data preparation', 'and augmentation'],
    ['Candidate features', 'and model training'],
    ['Hyperparameter tuning', 'and grouped evaluation'],
    ['Model conversion', 'for ESP32 execution'],
    ['Model-matched', 'embedded frontend'],
    ['ESP32 inference and', 'resource validation'],
])
work_package('WP5', ['Integration & Field Validation'], [
    ['Server result ingestion', 'and storage'],
    ['ESP32 preprocessing', 'and model integration'],
    ['Score-based alert rules', 'and notifications'],
    ['Monitoring dashboard', 'and result queries'],
    ['Field setup', 'and calibration'],
    ['End-to-end', 'result validation'],
    ['Comparison with', 'manual inspection'],
])
schedule()
for name in ('WP2', 'WP3', 'WP4', 'WP5'):
    subprocess.run([
        'pdftoppm', '-r', '160', '-png', '-singlefile',
        str(FIGURES / f'{name}.pdf'), str(FIGURES / name),
    ], check=True)
for number in (1, 2):
    subprocess.run([
        'pdftoppm', '-f', str(number), '-l', str(number), '-r', '160', '-png', '-singlefile',
        str(FIGURES / 'edge_project_schedule.pdf'), str(FIGURES / f'edge_project_schedule_{number}'),
    ], check=True)
