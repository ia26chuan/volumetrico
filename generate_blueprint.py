import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch, Arc
import numpy as np
import os

fig, ax = plt.subplots(1, 1, figsize=(14, 10), dpi=200)
ax.set_xlim(0, 1400)
ax.set_ylim(0, 1000)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor('#0a0e1a')

# === GRID BACKGROUND ===
for x in range(0, 1401, 25):
    ax.axvline(x, color='#0d1220', linewidth=0.3, zorder=0)
for y in range(0, 1001, 25):
    ax.axhline(y, color='#0d1220', linewidth=0.3, zorder=0)

# === TITLE BLOCK (top) ===
tb = patches.FancyBboxPatch((20, 940), 1360, 50, boxstyle="round,pad=2",
                             facecolor='none', edgecolor='#2a4060', linewidth=1.2)
ax.add_patch(tb)
ax.plot([500, 500], [940, 990], color='#2a4060', linewidth=0.8)
ax.plot([850, 850], [940, 990], color='#2a4060', linewidth=0.8)
ax.plot([1100, 1100], [940, 990], color='#2a4060', linewidth=0.8)

ax.text(260, 972, 'VOLUMETRIC LED MATRIX — ISOMETRIC PROJECTION',
        fontsize=11, color='#5a8ab0', fontfamily='monospace', fontweight='bold',
        ha='center', va='center', fontstyle='italic')
ax.text(675, 978, 'PROJECT', fontsize=6, color='#3a5a7a', fontfamily='monospace', ha='center')
ax.text(675, 965, 'PROTOTIPO VOLUMETRICO 10x10x10', fontsize=8, color='#6a9ab0',
        fontfamily='monospace', ha='center')
ax.text(975, 978, 'SCALE', fontsize=6, color='#3a5a7a', fontfamily='monospace', ha='center')
ax.text(975, 965, '1 : 5', fontsize=10, color='#7ab0d0', fontfamily='monospace', ha='center', fontweight='bold')
ax.text(1200, 978, 'DWG NO', fontsize=6, color='#3a5a7a', fontfamily='monospace', ha='center')
ax.text(1200, 965, 'VL-001', fontsize=10, color='#7ab0d0', fontfamily='monospace', ha='center', fontweight='bold')
ax.text(1300, 978, 'REV', fontsize=6, color='#3a5a7a', fontfamily='monospace', ha='center')
ax.text(1300, 965, '1.0', fontsize=10, color='#7ab0d0', fontfamily='monospace', ha='center')

# === ISOMETRIC PROJECTION FUNCTIONS ===
cx, cy = 520, 460  # center of cube
edge = 320  # half-edge in isometric
iso_angle = np.radians(30)

def iso_project(x, y, z):
    """Project 3D coords to 2D isometric."""
    px = cx + (x - y) * np.cos(iso_angle)
    py = cy - (x + y) * np.sin(iso_angle) - z
    return px, py

# Cube corners (0-1 in each axis, scaled)
corners = {}
for i in range(2):
    for j in range(2):
        for k in range(2):
            corners[(i,j,k)] = iso_project(i*edge, j*edge, k*edge)

# === WIREFRAME CUBE ===
# Hidden edges (dashed)
hidden_edges = [
    ((0,0,0), (1,0,0)), ((0,0,0), (0,1,0)), ((0,0,0), (0,0,1)),
]
for a, b in hidden_edges:
    x1, y1 = corners[a]
    x2, y2 = corners[b]
    ax.plot([x1, x2], [y1, y2], color='#1a2a3a', linewidth=0.8, linestyle='--', zorder=2)

# Visible edges
visible_edges = [
    ((1,0,0), (1,1,0)), ((0,1,0), (1,1,0)),
    ((1,0,0), (1,0,1)), ((0,1,0), (0,1,1)),
    ((1,1,0), (1,1,1)),
    ((1,0,1), (1,1,1)), ((0,1,1), (1,1,1)),
    ((1,0,1), (0,0,1)), ((0,1,1), (0,0,1)),
    ((0,0,1), (1,0,1)), ((0,0,1), (0,1,1)),
]
for a, b in visible_edges:
    x1, y1 = corners[a]
    x2, y2 = corners[b]
    ax.plot([x1, x2], [y1, y2], color='#3a6a8a', linewidth=1.0, zorder=3)

# === FACE GRIDS (10x10) ===
grid_color = '#1a2a3a'
grid_lw = 0.3
n = 10

# Top face grid (z=1, x and y vary)
for i in range(n+1):
    t = i / n
    x1, y1 = iso_project(t*edge, 0, edge)
    x2, y2 = iso_project(t*edge, edge, edge)
    ax.plot([x1, x2], [y1, y2], color=grid_color, linewidth=grid_lw, zorder=2)
    x1, y1 = iso_project(0, t*edge, edge)
    x2, y2 = iso_project(edge, t*edge, edge)
    ax.plot([x1, x2], [y1, y2], color=grid_color, linewidth=grid_lw, zorder=2)

# Left face grid (y=0, x and z vary)
for i in range(n+1):
    t = i / n
    x1, y1 = iso_project(t*edge, 0, 0)
    x2, y2 = iso_project(t*edge, 0, edge)
    ax.plot([x1, x2], [y1, y2], color=grid_color, linewidth=grid_lw, zorder=2)
    x1, y1 = iso_project(0, 0, t*edge)
    x2, y2 = iso_project(edge, 0, t*edge)
    ax.plot([x1, x2], [y1, y2], color=grid_color, linewidth=grid_lw, zorder=2)

# Right face grid (x=edge, y and z vary)
for i in range(n+1):
    t = i / n
    x1, y1 = iso_project(edge, t*edge, 0)
    x2, y2 = iso_project(edge, t*edge, edge)
    ax.plot([x1, x2], [y1, y2], color=grid_color, linewidth=grid_lw, zorder=2)
    x1, y1 = iso_project(edge, 0, t*edge)
    x2, y2 = iso_project(edge, edge, t*edge)
    ax.plot([x1, x2], [y1, y2], color=grid_color, linewidth=grid_lw, zorder=2)

# === LED NODE MARKERS (cross marks at intersections) ===
def draw_led_cross(ax, px, py, size=2.5, color='#2a5a6a'):
    ax.plot([px-size, px+size], [py-size, py+size], color=color, linewidth=0.5, zorder=4)
    ax.plot([px-size, px+size], [py+size, py-size], color=color, linewidth=0.5, zorder=4)

# Top face LEDs
for i in range(n):
    for j in range(n):
        t1 = (i + 0.5) / n
        t2 = (j + 0.5) / n
        px, py = iso_project(t1*edge, t2*edge, edge)
        draw_led_cross(ax, px, py, 2.5, '#2a4a6a')

# Left face LEDs
for i in range(n):
    for k in range(n):
        t1 = (i + 0.5) / n
        t2 = (k + 0.5) / n
        px, py = iso_project(t1*edge, 0, t2*edge)
        draw_led_cross(ax, px, py, 2.5, '#1a4a4a')

# Right face LEDs
for j in range(n):
    for k in range(n):
        t1 = (j + 0.5) / n
        t2 = (k + 0.5) / n
        px, py = iso_project(edge, t1*edge, t2*edge)
        draw_led_cross(ax, px, py, 2.5, '#4a1a3a')

# === DIMENSION LINES ===
dim_color = '#4a7a9a'
dim_font = {'fontsize': 7, 'color': '#5a9aba', 'fontfamily': 'monospace', 'ha': 'center', 'va': 'center'}

# Z axis (height) - left side
zx1, zy1 = iso_project(0, 0, 0)
zx2, zy2 = iso_project(0, 0, edge)
offset_x = -55
ax.annotate('', xy=(zx1+offset_x, zy1), xytext=(zx1+offset_x, zy2),
            arrowprops=dict(arrowstyle='<->', color=dim_color, lw=0.8))
ax.plot([zx1, zx1+offset_x], [zy1, zy1], color=dim_color, linewidth=0.4, linestyle=':')
ax.plot([zx2, zx1+offset_x], [zy2, zy2], color=dim_color, linewidth=0.4, linestyle=':')
ax.text(zx1+offset_x-18, (zy1+zy2)/2, '100 cm', **dim_font, rotation=90)
ax.text(zx1+offset_x-18, (zy1+zy2)/2+25, '(10 x 10cm)', fontsize=5, color='#3a6a8a',
        fontfamily='monospace', ha='center', rotation=90)

# Z mid marker
zx_mid, zy_mid = iso_project(0, 0, edge/2)
ax.plot([zx1-3, zx1+3], [zy_mid, zy_mid], color=dim_color, linewidth=0.6)
ax.text(zx1+offset_x+8, zy_mid, '50', fontsize=6, color='#4a7a9a', fontfamily='monospace', ha='center')

# X axis (width) - bottom
xx1, xy1 = iso_project(0, 0, 0)
xx2, xy2 = iso_project(edge, 0, 0)
offset_y = 50
ax.annotate('', xy=(xx1, xy1+offset_y), xytext=(xx2, xy2+offset_y),
            arrowprops=dict(arrowstyle='<->', color=dim_color, lw=0.8))
ax.plot([xx1, xx1], [xy1, xy1+offset_y], color=dim_color, linewidth=0.4, linestyle=':')
ax.plot([xx2, xx2], [xy2, xy2+offset_y], color=dim_color, linewidth=0.4, linestyle=':')
ax.text((xx1+xx2)/2, xy1+offset_y+15, '100 cm', **dim_font)
ax.text((xx1+xx2)/2, xy1+offset_y+30, '(10 x 10cm)', fontsize=5, color='#3a6a8a',
        fontfamily='monospace', ha='center')

# X mid marker
xx_mid, xy_mid = iso_project(edge/2, 0, 0)
ax.plot([xx_mid, xx_mid], [xy1+offset_y-3, xy1+offset_y+3], color=dim_color, linewidth=0.6)
ax.text(xx_mid, xy1+offset_y-8, '50', fontsize=6, color='#4a7a9a', fontfamily='monospace', ha='center')

# Y axis (depth) - bottom right
yx1, yy1 = iso_project(edge, 0, 0)
yx2, yy2 = iso_project(edge, edge, 0)
ax.annotate('', xy=(yx1, yy1+offset_y), xytext=(yx2, yy2+offset_y),
            arrowprops=dict(arrowstyle='<->', color=dim_color, lw=0.8))
ax.plot([yx1, yx1], [yy1, yy1+offset_y], color=dim_color, linewidth=0.4, linestyle=':')
ax.plot([yx2, yx2], [yy2, yy2+offset_y], color=dim_color, linewidth=0.4, linestyle=':')
ax.text((yx1+yx2)/2, (yy1+yy2)/2+offset_y+15, '100 cm', **dim_font)
ax.text((yx1+yx2)/2, (yy1+yy2)/2+offset_y+30, '(10 x 10cm)', fontsize=5, color='#3a6a8a',
        fontfamily='monospace', ha='center')

# Y mid marker
yx_mid, yy_mid = iso_project(edge, edge/2, 0)
ax.plot([yx_mid-3, yx_mid+3], [yy1+offset_y, yy1+offset_y], color=dim_color, linewidth=0.6)

# === CORNER VERTEX MARKERS ===
vertex_labels = {
    (1,0,0): 'A', (1,1,0): 'B', (0,1,0): 'C', (0,0,0): 'D',
    (1,0,1): 'E', (1,1,1): 'F', (0,1,1): 'G', (0,0,1): 'H',
}
for (i,j,k), label in vertex_labels.items():
    px, py = iso_project(i*edge, j*edge, k*edge)
    circle = plt.Circle((px, py), 3, fill=True, facecolor='#3a6a8a', edgecolor='#5a9aba', linewidth=0.6, zorder=5)
    ax.add_patch(circle)
    ox = 8 if i == 0 or (i == 1 and j == 1) else -8
    oy = 8 if k == 1 else -8
    ax.text(px+ox, py+oy, label, fontsize=7, color='#6a9aba', fontfamily='monospace',
            ha='center', va='center', fontweight='bold', zorder=6)

# === AXIS LABELS ===
ax.text(iso_project(edge/2, -20, -15)[0], iso_project(edge/2, -20, -15)[1],
        'X', fontsize=12, color='#4a7a9a', fontfamily='monospace', ha='center', fontweight='bold')
ax.text(iso_project(edge+20, edge/2, -15)[0], iso_project(edge+20, edge/2, -15)[1],
        'Y', fontsize=12, color='#4a7a9a', fontfamily='monospace', ha='center', fontweight='bold')
ax.text(iso_project(-20, -10, edge/2)[0], iso_project(-20, -10, edge/2)[1],
        'Z', fontsize=12, color='#4a7a9a', fontfamily='monospace', ha='center', fontweight='bold')

# === FACE LABELS ===
# Left face center
lf = iso_project(edge/2, -8, edge/2)
ax.text(lf[0], lf[1], 'FACE LEFT (XZ)', fontsize=6, color='#2a5a6a',
        fontfamily='monospace', ha='center', va='center', rotation=-60, fontstyle='italic')

# Right face center
rf = iso_project(edge+8, edge/2, edge/2)
ax.text(rf[0], rf[1], 'FACE RIGHT (YZ)', fontsize=6, color='#4a2a4a',
        fontfamily='monospace', ha='center', va='center', rotation=60, fontstyle='italic')

# Top face center
tf = iso_project(edge/2, edge/2, edge+8)
ax.text(tf[0], tf[1], 'FACE TOP (XY)', fontsize=6, color='#3a3a5a',
        fontfamily='monospace', ha='center', va='center', fontstyle='italic')

# === SECTION MARKER A-A ===
sa_top = iso_project(edge/2, -5, edge)
sa_bot = iso_project(edge/2, -5, 0)
ax.plot([sa_top[0], sa_top[0]], [sa_top[1], sa_top[1]+15], color='#6a5a2a', linewidth=0.6, linestyle='--')
ax.plot([sa_bot[0], sa_bot[0]], [sa_bot[1], sa_bot[1]-15], color='#6a5a2a', linewidth=0.6, linestyle='--')
ax.text(sa_top[0], sa_top[1]+20, 'A', fontsize=8, color='#8a7a3a', fontfamily='monospace',
        ha='center', fontweight='bold')
ax.text(sa_bot[0], sa_bot[1]-20, 'A', fontsize=8, color='#8a7a3a', fontfamily='monospace',
        ha='center', fontweight='bold')

# === SIGNAL PATH ANNOTATION ===
# Draw a data flow arrow from controller area to cube
arr_start = iso_project(-15, edge/2, edge/2)
arr_end = iso_project(0, edge/2, edge/2)
ax.annotate('', xy=arr_end, xytext=arr_start,
            arrowprops=dict(arrowstyle='->', color='#2a6a4a', lw=1.0, connectionstyle='arc3,rad=0'))
ax.text(arr_start[0]-5, arr_start[1]+12, 'DDP DATA', fontsize=5.5, color='#3a7a5a',
        fontfamily='monospace', ha='center')
ax.text(arr_start[0]-5, arr_start[1]+3, 'INPUT', fontsize=5.5, color='#3a7a5a',
        fontfamily='monospace', ha='center')

# === POWER ANNOTATION ===
pw_start = iso_project(edge/2, edge+15, 0)
pw_end = iso_project(edge/2, edge, 0)
ax.annotate('', xy=pw_end, xytext=pw_start,
            arrowprops=dict(arrowstyle='->', color='#6a3a2a', lw=1.0))
ax.text(pw_start[0], pw_start[1]+12, '12V DC', fontsize=5.5, color='#8a5a3a',
        fontfamily='monospace', ha='center')
ax.text(pw_start[0], pw_start[1]+3, 'POWER IN', fontsize=5.5, color='#8a5a3a',
        fontfamily='monospace', ha='center')

# === LED COUNT ANNOTATIONS ===
ax.text(700, 920, 'LEDs per face: 10 x 10 = 100 nodes',
        fontsize=7, color='#3a5a7a', fontfamily='monospace', ha='center')
ax.text(700, 905, 'Total volume: 10 x 10 x 10 = 1,000 RGB pixels',
        fontsize=7, color='#4a6a8a', fontfamily='monospace', ha='center')
ax.text(700, 890, 'Control: 96 Art-Net Universes via DDP Protocol',
        fontsize=7, color='#3a5a7a', fontfamily='monospace', ha='center')

# === REVISION / NOTES (bottom) ===
ax.plot([20, 1380], [45, 45], color='#1a2a3a', linewidth=0.6)
ax.text(30, 32, 'NOTES:', fontsize=7, color='#3a5a7a', fontfamily='monospace', fontweight='bold')
ax.text(30, 18, '1. All dimensions in centimeters (cm). Tolerance: +/- 2mm per node.', fontsize=6,
        color='#2a4a6a', fontfamily='monospace')
ax.text(30, 6, '2. Material: WS2811 LED Pebble Pixels with IP65 weather rating.', fontsize=6,
        color='#2a4a6a', fontfamily='monospace')
ax.text(700, 32, 'UNITS: Metric', fontsize=6, color='#2a4a6a', fontfamily='monospace')
ax.text(700, 18, 'PROJECTION: Isometric 30 deg', fontsize=6, color='#2a4a6a', fontfamily='monospace')
ax.text(700, 6, 'THIRD ANGLE', fontsize=6, color='#2a4a6a', fontfamily='monospace')
ax.text(1350, 32, 'SHEET 1 / 1', fontsize=6, color='#3a5a7a', fontfamily='monospace', ha='right')
ax.text(1350, 18, 'DATE: 2026-07-26', fontsize=6, color='#3a5a7a', fontfamily='monospace', ha='right')
ax.text(1350, 6, 'DRAWN BY: IA ENGINEERING', fontsize=6, color='#3a5a7a', fontfamily='monospace', ha='right')

# === FRAME BORDER ===
frame = patches.Rectangle((10, 50), 1380, 940, linewidth=1.5, edgecolor='#1a3050', facecolor='none', zorder=10)
ax.add_patch(frame)
inner = patches.Rectangle((15, 55), 1370, 930, linewidth=0.4, edgecolor='#0f1a2a', facecolor='none', zorder=10)
ax.add_patch(inner)

plt.tight_layout(pad=0.5)
output_path = os.path.join(os.path.dirname(__file__), 'img', 'prototipo-volumetrico-blueprint.png')
plt.savefig(output_path, dpi=200, facecolor='#0a0e1a', bbox_inches='tight', pad_inches=0.3)
plt.close()
print(f"Blueprint saved to: {output_path}")
print(f"File size: {os.path.getsize(output_path) / 1024:.0f} KB")
