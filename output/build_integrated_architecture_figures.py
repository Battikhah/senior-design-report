"""Export the seven integrated-system pages from the editable draw.io source.

Requires reportlab and Poppler's pdftoppm. Other draw.io pages are left alone.
Only simple rectangular nodes and orthogonal arrows used by these pages are
supported; keep the source in this subset when revising these report figures.
"""
from html import unescape
from pathlib import Path
import math
import re
import subprocess
import xml.etree.ElementTree as ET

from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'diagrams' / 'Senior_Design_Section4_EdgeML.drawio.xml'
FIGURES = ROOT / 'figures'
PAGES = {
    'System Block Diagram': 'system_fig_diagram',
    'Three-Tier Node Architecture': '3Node_Arch',
    'Class Architecture (Conceptual)': 'Class_Architecture_edge',
    'Result-Centred Data Architecture': 'ER_Diagram',
    'Sensing Layer Operational Flow': 'Sensing_layer_flowchart',
    'Cluster Layer Operational Flow': 'Cluster_layer_flowchart',
    'Edge Inference and Alternative Feature Codec': 'codec_current_pipeline',
}
INK = colors.HexColor('#333333')
LINE = colors.HexColor('#808080')


def style(cell):
    return dict(part.split('=', 1) for part in cell.get('style', '').split(';') if '=' in part)


def lines(cell):
    return [unescape(re.sub('<[^>]+>', '', line)) for line in
            re.split(r'<br\s*/?>', cell.get('value', ''))]


def render(diagram, stem):
    model = diagram.find('mxGraphModel')
    width, height = float(model.get('pageWidth')), float(model.get('pageHeight'))
    cells = list(model.find('root'))
    nodes = {cell.get('id'): cell for cell in cells if cell.get('vertex') == '1'}
    geometry = {key: tuple(float(cell.find('mxGeometry').get(attr)) for attr in ('x', 'y', 'width', 'height'))
                for key, cell in nodes.items()}
    page = canvas.Canvas(str(FIGURES / f'{stem}.pdf'), pagesize=(width, height), invariant=1)
    page.setTitle(lines(nodes['title'])[0])
    page.setAuthor('Senior Design - illustrative architecture')
    page.setLineWidth(1)
    # Arrows first so all connectors terminate cleanly at the node borders.
    for cell in cells:
        if cell.get('edge') != '1':
            continue
        ax, ay, aw, ah = geometry[cell.get('source')]
        bx, by, bw, bh = geometry[cell.get('target')]
        horizontal = style(cell).get('exitX') == '1'
        if horizontal:
            start, end = (ax + aw, ay + ah / 2), (bx, by + bh / 2)
            points = [start, end]
        else:
            start, end = (ax + aw / 2, ay + ah), (bx + bw / 2, by)
            mid = (start[1] + end[1]) / 2
            points = [start, (start[0], mid), (end[0], mid), end]
        points = [(x, height - y) for x, y in points]
        page.setStrokeColor(LINE)
        path = page.beginPath(); path.moveTo(*points[0])
        for point in points[1:]:
            path.lineTo(*point)
        page.drawPath(path)
        ex, ey = points[-1]
        angle = 0 if horizontal else -math.pi / 2
        page.setFillColor(LINE)
        arrow = page.beginPath(); arrow.moveTo(ex, ey)
        for delta in (-0.45, 0.45):
            arrow.lineTo(ex - 7 * math.cos(angle + delta), ey - 7 * math.sin(angle + delta))
        arrow.close(); page.drawPath(arrow, fill=1, stroke=0)
        label = cell.get('value', '')
        if label:
            size = 11
            label_width = stringWidth(label, 'Helvetica', size)
            lx = (start[0] + end[0]) / 2
            ly = height - (start[1] + end[1]) / 2 + 3
            page.setFillColor(colors.white)
            page.rect(lx - label_width / 2 - 3, ly - 2, label_width + 6, size + 3, stroke=0, fill=1)
            page.setFillColor(INK); page.setFont('Helvetica', size)
            page.drawCentredString(lx, ly, label)
    for key, cell in nodes.items():
        x, y, w, h = geometry[key]
        settings = style(cell)
        text = lines(cell)
        size = float(settings.get('fontSize', '14'))
        font = 'Helvetica-Bold' if key in ('title', 'primary', 'alternative') else 'Helvetica'
        assert x >= 0 and y >= 0 and x + w <= width and y + h <= height, key
        assert max(stringWidth(line, font, size) for line in text) <= w - 12, (stem, key, 'text too wide')
        assert len(text) * size * 1.2 <= h, (stem, key, 'text too tall')
        if settings.get('strokeColor') != 'none':
            page.setFillColor(colors.HexColor('#F4F4F4'))
            page.setStrokeColor(LINE)
            page.setDash([4, 3] if settings.get('dashed') == '1' else [])
            page.roundRect(x, height - y - h, w, h, 5, stroke=1, fill=1)
            page.setDash([])
        page.setFont(font, size); page.setFillColor(INK)
        baseline = height - y - h / 2 + (len(text) - 1) * size * 0.6 - size * 0.34
        for index, line in enumerate(text):
            page.drawCentredString(x + w / 2, baseline - index * size * 1.2, line)
    page.save()
    subprocess.run(['pdftoppm', '-r', '160', '-png', '-singlefile',
                    str(FIGURES / f'{stem}.pdf'), str(FIGURES / stem)], check=True)


def main():
    diagrams = {d.get('name'): d for d in ET.parse(SOURCE).getroot()}
    for name, stem in PAGES.items():
        render(diagrams[name], stem)
    # Existing companion previews must stay in step with the imported flowcharts.
    for source, alias in [('Sensing_layer_flowchart', 'sensing_layer'), ('Cluster_layer_flowchart', 'cluster_layer')]:
        path = FIGURES / f'{alias}.png'
        if path.exists():
            path.write_bytes((FIGURES / f'{source}.png').read_bytes())
    print(f'Rendered {len(PAGES)} integrated architecture PDF/PNG pairs.')


if __name__ == '__main__':
    main()
