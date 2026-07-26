import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

fig, ax = plt.subplots(1, 1, figsize=(16, 11), dpi=200)
ax.set_xlim(0, 1600)
ax.set_ylim(0, 1100)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor('#080c18')

# === TITLE BLOCK (top) ===
tb = patches.Rectangle((20, 1040), 1560, 50, linewidth=1.2, edgecolor='#2a4060', facecolor='none')
ax.add_patch(tb)
ax.plot([480, 480], [1040, 1090], color='#2a4060', linewidth=0.8)
ax.plot([820, 820], [1040, 1090], color='#2a4060', linewidth=0.8)
ax.plot([1100, 1100], [1040, 1090], color='#2a4060', linewidth=0.8)
ax.plot([1340, 1340], [1040, 1090], color='#2a4060', linewidth=0.8)

ax.text(250, 1072, 'VOLUMETRIC LED MATRIX', fontsize=13, color='#5a8ab0',
        fontfamily='monospace', fontweight='bold', ha='center')
ax.text(250, 1058, 'ISOMETRIC PROJECTION', fontsize=8, color='#3a6a8a',
        fontfamily='monospace', ha='center')
ax.text(650, 1078, 'PROJECT', fontsize=6, color='#3a5a7a', fontfamily='monospace', ha='center')
ax.text(650, 1065, 'PROTOTIPO VOLUMETRICO 10x10x10', fontsize=9, color='#6a9ab0',
        fontfamily='monospace', ha='center')
ax.text(960, 1078, 'SCALE', fontsize=6, color='#3a5a7a', fontfamily='monospace', ha='center')
ax.text(960, 1065, '1 : 5', fontsize=11, color='#7ab0d0', fontfamily='monospace',
        ha='center', fontweight='bold')
ax.text(1220, 1078, 'DWG NO', fontsize=6, color='#3a5a7a', fontfamily='monospace', ha='center')
ax.text(1220, 1065, 'VL-001', fontsize=11, color='#7ab0d0', fontfamily='monospace',
        ha='center', fontweight='bold')
ax.text(1470, 1078, 'REV', fontsize=6, color='#3a5a7a', fontfamily='monospace', ha='center')
ax.text(1470, 1065, '1.0', fontsize=11, color='#7ab0d0', fontfamily='monospace', ha='center')

# === ISOMETRIC ===
cx, cy = 560, 560
edge = 300
iso_angle = np.radians(30)

def iso(x, y, z):
    return cx + (x - y) * np.cos(iso_angle), cy - (x + y) * np.sin(iso_angle) - z

# Wireframe edges
def line(a, b, color='#3a6a8a', lw=1.0, ls='-'):
    x1, y1 = iso(*a)
    x2, y2 = iso(*b)
    ax.plot([x1, x2], [y1, y2], color=color, linewidth=lw, linestyle=ls, zorder=3)

# Hidden edges (dashed)
line((0,0,0), (1,0,0), '#1a2a3a', 0.7, '--')
line((0,0,0), (0,1,0), '#1a2a3a', 0.7, '--')
line((0,0,0), (0,0,1), '#1a2a3a', 0.7, '--')

# Visible edges
for a, b in [
    ((1,0,0),(1,1,0)), ((0,1,0),(1,1,0)),
    ((1,0,0),(1,0,1)), ((0,1,0),(0,1,1)),
    ((1,1,0),(1,1,1)),
    ((1,0,1),(1,1,1)), ((0,1,1),(1,1,1)),
    ((1,0,1),(0,0,1)), ((0,1,1),(0,0,1)),
    ((0,0,1),(1,0,1)), ((0,0,1),(0,1,1)),
]:
    line(a, b)

# === 3D GRID (each face, 10x10) ===
gc = '#141e2e'
for i in range(11):
    t = i / 10
    # Top face
    line((t, 0, 1), (t, 1, 1), gc, 0.25)
    line((0, t, 1), (1, t, 1), gc, 0.25)
    # Left face
    line((t, 0, 0), (t, 0, 1), gc, 0.25)
    line((0, 0, t), (1, 0, t), gc, 0.25)
    # Right face
    line((1, t, 0), (1, t, 1), gc, 0.25)
    line((1, 0, t), (1, 1, t), gc, 0.25)

# === LED NODES (cross marks at each intersection) ===
def cross(px, py, s=2.5, c='#2a4a5a'):
    ax.plot([px-s, px+s], [py-s, py+s], color=c, linewidth=0.5, zorder=4)
    ax.plot([px-s, px+s], [py+s, py-s], color=c, linewidth=0.5, zorder=4)

for i in range(10):
    for j in range(10):
        t1 = (i + 0.5) / 10
        t2 = (j + 0.5) / 10
        # Top
        cross(*iso(t1, t2, 1), c='#2a3a5a')
        # Left
        cross(*iso(t1, 0, t2), c='#1a3a3a')
        # Right
        cross(*iso(1, t1, t2), c='#3a1a2a')

# === DIMENSION LINES (engineering standard) ===
dc = '#4a7a9a'
df = {'fontsize': 7.5, 'color': '#5a9aba', 'fontfamily': 'monospace', 'ha': 'center', 'va': 'center'}

# --- Z axis (vertical, left side) ---
zx0, zy0 = iso(0, 0, 0)
zx1, zy1 = iso(0, 0, 1)
ox = -60
ax.plot([zx0+ox, zx0+ox], [zy0, zy1], color=dc, linewidth=0.7, zorder=3)
ax.plot([zx0-3, zx0+3], [zy0, zy0], color=dc, linewidth=0.6)
ax.plot([zx0-3, zx0+3], [zy1, zy1], color=dc, linewidth=0.6)
# Extension lines
ax.plot([zx0, zx0+ox], [zy0, zy0], color=dc, linewidth=0.3, linestyle=':', zorder=2)
ax.plot([zx0, zx0+ox], [zy1, zy1], color=dc, linewidth=0.3, linestyle=':', zorder=2)
ax.plot([zx0, zx0+ox], [zy0/2+zy1/2, zy0/2+zy1/2], color=dc, linewidth=0.3, linestyle=':', zorder=2)
# Tick marks
ax.plot([zx0+ox-3, zx0+ox+3], [zy0/2+zy1/2, zy0/2+zy1/2], color=dc, linewidth=0.6)
# Text
ax.text(zx0+ox-12, zy0/2+zy1/2, '100 cm', rotation=90, **df)
ax.text(zx0+ox+12, (zy0+zy1)/2, '50', fontsize=6.5, color='#4a7a9a', fontfamily='monospace', ha='center')
ax.text(zx0+ox-12, zy1+20, '(10 x 10cm)', fontsize=5, color='#3a6a8a', fontfamily='monospace', ha='center', rotation=90)

# --- X axis (bottom left) ---
xx0, xy0 = iso(0, 0, 0)
xx1, xy1 = iso(1, 0, 0)
oy = 55
ax.plot([xx0, xx1], [xy0+oy, xy1+oy], color=dc, linewidth=0.7, zorder=3)
ax.plot([xx0, xx0], [xy0, xy0+oy], color=dc, linewidth=0.3, linestyle=':', zorder=2)
ax.plot([xx1, xx1], [xy1, xy1+oy], color=dc, linewidth=0.3, linestyle=':', zorder=2)
# Midpoint extension
xm = (xx0+xx1)/2
ym = (xy0+xy1)/2
ax.plot([xm, xm], [ym, ym+oy], color=dc, linewidth=0.3, linestyle=':', zorder=2)
ax.plot([xx0-3, xx0+3], [xy0+oy, xy0+oy], color=dc, linewidth=0.6)
ax.plot([xx1-3, xx1+3], [xy1+oy, xy1+oy], color=dc, linewidth=0.6)
ax.plot([xm-3, xm+3], [ym+oy, ym+oy], color=dc, linewidth=0.6)
ax.text((xx0+xx1)/2, xy0+oy+12, '100 cm', **df)
ax.text(xx0/2+xx1/2, xy0+oy-8, '50', fontsize=6.5, color='#4a7a9a', fontfamily='monospace', ha='center')
ax.text((xx0+xx1)/2, xy0+oy+25, '(10 x 10cm)', fontsize=5, color='#3a6a8a', fontfamily='monospace', ha='center')

# --- Y axis (bottom right) ---
yx0, yy0 = iso(1, 0, 0)
yx1, yy1 = iso(1, 1, 0)
ax.plot([yx0, yx1], [yy0+oy, yy1+oy], color=dc, linewidth=0.7, zorder=3)
ax.plot([yx0, yx0], [yy0, yy0+oy], color=dc, linewidth=0.3, linestyle=':', zorder=2)
ax.plot([yx1, yx1], [yy1, yy1+oy], color=dc, linewidth=0.3, linestyle=':', zorder=2)
ym2 = (yy0+yy1)/2
ax.plot([(yx0+yx1)/2, (yx0+yx1)/2], [ym2, ym2+oy], color=dc, linewidth=0.3, linestyle=':', zorder=2)
ax.plot([yx0-3, yx0+3], [yy0+oy, yy0+oy], color=dc, linewidth=0.6)
ax.plot([yx1-3, yx1+3], [yy1+oy, yy1+oy], color=dc, linewidth=0.6)
ax.plot([(yx0+yx1)/2-3, (yx0+yx1)/2+3], [ym2+oy, ym2+oy], color=dc, linewidth=0.6)
ax.text((yx0+yx1)/2, ym2+oy+12, '100 cm', **df)
ax.text((yx0+yx1)/2, ym2+oy-8, '50', fontsize=6.5, color='#4a7a9a', fontfamily='monospace', ha='center')
ax.text((yx0+yx1)/2, ym2+oy+25, '(10 x 10cm)', fontsize=5, color='#3a6a8a', fontfamily='monospace', ha='center')

# === VERTEX MARKERS + LABELS ===
verts = {}
for i in range(2):
    for j in range(2):
        for k in range(2):
            verts[(i,j,k)] = iso(i, j, k)

labels = {
    (1,0,0): ('A', (-12, -8)), (1,1,0): ('B', (8, -8)), (0,1,0): ('C', (8, -8)),
    (0,0,0): ('D', (-12, -8)),
    (1,0,1): ('E', (-12, 8)), (1,1,1): ('F', (8, 8)), (0,1,1): ('G', (8, 8)),
    (0,0,1): ('H', (-12, 8)),
}

for (i,j,k), (lbl, (ox2, oy2)) in labels.items():
    px, py = verts[(i,j,k)]
    c = plt.Circle((px, py), 4, fill=True, facecolor='#2a4a6a', edgecolor='#4a7a9a', linewidth=0.7, zorder=6)
    ax.add_patch(c)
    ax.text(px+ox2, py+oy2, lbl, fontsize=8, color='#6a9aba', fontfamily='monospace',
            ha='center', va='center', fontweight='bold', zorder=7)

# === AXIS LABELS ===
ax.text(iso(0.5, -0.08, -0.06)[0], iso(0.5, -0.08, -0.06)[1], 'X',
        fontsize=14, color='#4a7a9a', fontfamily='monospace', ha='center', fontweight='bold')
ax.text(iso(1.08, 0.5, -0.06)[0], iso(1.08, 0.5, -0.06)[1], 'Y',
        fontsize=14, color='#4a7a9a', fontfamily='monospace', ha='center', fontweight='bold')
ax.text(iso(-0.06, -0.06, 0.5)[0], iso(-0.06, -0.06, 0.5)[1], 'Z',
        fontsize=14, color='#4a7a9a', fontfamily='monospace', ha='center', fontweight='bold')

# === SECTION LINE A-A (vertical cut through center) ===
sa_top = iso(0.5, -0.06, 1)
sa_bot = iso(0.5, -0.06, 0)
ax.plot([sa_top[0], sa_top[0]], [sa_top[1], sa_top[1]+20], color='#6a5a2a', linewidth=0.7, linestyle='--')
ax.plot([sa_bot[0], sa_bot[0]], [sa_bot[1], sa_bot[1]-20], color='#6a5a2a', linewidth=0.7, linestyle='--')
ax.text(sa_top[0], sa_top[1]+28, 'A', fontsize=9, color='#8a7a3a', fontfamily='monospace', ha='center', fontweight='bold')
ax.text(sa_bot[0], sa_bot[1]-28, 'A', fontsize=9, color='#8a7a3a', fontfamily='monospace', ha='center', fontweight='bold')
# Dashed section line
ax.plot([sa_top[0], sa_bot[0]], [sa_top[1], sa_bot[1]], color='#6a5a2a', linewidth=0.5, linestyle='--', zorder=2)

# === FACE LABELS (rotated text on each face) ===
lf = iso(0.5, -0.06, 0.5)
ax.text(lf[0], lf[1], 'XZ', fontsize=9, color='#1a4a5a', fontfamily='monospace',
        ha='center', va='center', rotation=-60, fontstyle='italic', fontweight='bold')
rf = iso(1.06, 0.5, 0.5)
ax.text(rf[0], rf[1], 'YZ', fontsize=9, color='#4a1a3a', fontfamily='monospace',
        ha='center', va='center', rotation=60, fontstyle='italic', fontweight='bold')
tf = iso(0.5, 0.5, 1.06)
ax.text(tf[0], tf[1], 'XY', fontsize=9, color='#3a2a5a', fontfamily='monospace',
        ha='center', va='center', fontstyle='italic', fontweight='bold')

# === DATA FLOW + POWER ANNOTATIONS ===
d_start = iso(-0.12, 0.5, 0.5)
d_end = iso(0, 0.5, 0.5)
ax.annotate('', xy=d_end, xytext=d_start,
            arrowprops=dict(arrowstyle='->', color='#2a6a4a', lw=1.2))
ax.text(d_start[0]-5, d_start[1]+15, 'DDP DATA', fontsize=6, color='#3a7a5a',
        fontfamily='monospace', ha='center')
ax.text(d_start[0]-5, d_start[1]+5, 'INPUT', fontsize=6, color='#3a7a5a',
        fontfamily='monospace', ha='center')

p_start = iso(0.5, 1.12, 0)
p_end = iso(0.5, 1, 0)
ax.annotate('', xy=p_end, xytext=p_start,
            arrowprops=dict(arrowstyle='->', color='#6a3a2a', lw=1.2))
ax.text(p_start[0], p_start[1]+12, '12V DC', fontsize=6, color='#8a5a3a',
        fontfamily='monospace', ha='center')
ax.text(p_start[0], p_start[1]+3, 'POWER IN', fontsize=6, color='#8a5a3a',
        fontfamily='monospace', ha='center')

# === SPECS TABLE (right side) ===
tx, ty = 1050, 720
tw, th = 500, 310
spec_box = patches.Rectangle((tx, ty), tw, th, linewidth=1.0, edgecolor='#2a4060',
                               facecolor='#0a0e1a', zorder=5)
ax.add_patch(spec_box)
# Header
ax.plot([tx, tx+tw], [ty+th-28, ty+th-28], color='#2a4060', linewidth=0.6)
ax.text(tx+tw/2, ty+th-14, 'TECHNICAL SPECIFICATIONS', fontsize=9, color='#5a8ab0',
        fontfamily='monospace', ha='center', fontweight='bold')

specs = [
    ('LED Chip', 'WS2811 12V, 4-Wire, Pebble Pixel'),
    ('Pixel Density', '1,000 nodes (10x10x10 grid)'),
    ('Node Spacing', '50mm (5cm) center-to-center'),
    ('Total Volume', '100cm x 100cm x 100cm'),
    ('Controller', 'LINETX LNX-370SP (Art-Net 4)'),
    ('Power Supply', 'Mean Well LRS-350-12 (350W, 12V DC)'),
    ('Protocol', 'DDP over Ethernet (Cat6 UTP)'),
    ('Universes', '96 Art-Net Universes'),
    ('Weather Rating', 'IP65 Indoor/Outdoor'),
    ('Frame', 'Aluminum extrusion grid, modular'),
    ('Software', 'TouchDesigner / Madrix / xLights'),
]

for idx, (k, v) in enumerate(specs):
    ry = ty + th - 48 - idx * 24
    ax.plot([tx+10, tx+tw-10], [ry+4, ry+4], color='#111a2a', linewidth=0.3)
    ax.text(tx+15, ry-2, k, fontsize=7, color='#4a7a9a', fontfamily='monospace', fontweight='bold')
    ax.text(tx+170, ry-2, v, fontsize=7, color='#3a6a8a', fontfamily='monospace')

# === NOTES (bottom) ===
ax.plot([20, 1580], [48, 48], color='#1a2a3a', linewidth=0.6)
ax.text(30, 35, 'NOTES:', fontsize=7.5, color='#3a5a7a', fontfamily='monospace', fontweight='bold')
ax.text(30, 22, '1. All dimensions in centimeters. Tolerance: +/- 2mm per node position.', fontsize=6,
        color='#2a4a6a', fontfamily='monospace')
ax.text(30, 10, '2. Material: WS2811 LED Pebble Pixels. IP65 rated. Aluminum frame.', fontsize=6,
        color='#2a4a6a', fontfamily='monospace')
ax.text(800, 35, 'UNITS: Metric (cm/mm)', fontsize=6, color='#2a4a6a', fontfamily='monospace')
ax.text(800, 22, 'PROJECTION: Isometric 30 deg', fontsize=6, color='#2a4a6a', fontfamily='monospace')
ax.text(800, 10, 'THIRD ANGLE', fontsize=6, color='#2a4a6a', fontfamily='monospace')
ax.text(1550, 35, 'SHEET 1 / 1', fontsize=6, color='#3a5a7a', fontfamily='monospace', ha='right')
ax.text(1550, 22, 'DATE: 2026-07-26', fontsize=6, color='#3a5a7a', fontfamily='monospace', ha='right')
ax.text(1550, 10, 'DRAWN: IA ENGINEERING', fontsize=6, color='#3a5a7a', fontfamily='monospace', ha='right')

# === FRAME ===
frame = patches.Rectangle((10, 50), 1580, 1040, linewidth=1.5, edgecolor='#1a3050', facecolor='none', zorder=10)
ax.add_patch(frame)
inner = patches.Rectangle((15, 55), 1570, 1030, linewidth=0.4, edgecolor='#0f1a2a', facecolor='none', zorder=10)
ax.add_patch(inner)

plt.tight_layout(pad=0.3)
out = os.path.join(os.path.dirname(__file__), 'img', 'prototipo-volumetrico-blueprint.png')
plt.savefig(out, dpi=200, facecolor='#080c18', bbox_inches='tight', pad_inches=0.2)
plt.close()
print(f"Saved: {out} ({os.path.getsize(out)//1024} KB)")
