
import matplotlib.pyplot as plt
from math import sin, cos, pi

r_hub = 27
r_rim = 279
n_holes = 32

def centred_circle(p, r):
    p.gca().add_patch(p.Circle((0, 0), radius=r, fill=False))

def hole(r, i):
    return (r * cos(i * 2 * pi / n_holes), r * sin(i * 2 * pi / n_holes))

def spoke(p, i_hub, i_rim, **kargs):
    xr, yr = hole(r_rim, i_rim)
    xh, yh = hole(r_hub, i_hub)
    p.gca().add_line(p.Line2D((xr, xh), (yr, yh), **kargs))

def two_leading_two_trailing(p, delta, **kargs):
    for i in range(4):
        offset = n_holes * i / 4
        for j in range(2):
            spoke(p, delta + offset + 2 * j, delta + offset + 2 * j + 4, **kargs)
            spoke(p, delta + offset + 2 * j + 4, delta + offset + 2 * j, **kargs)

plt.axes()
centred_circle(plt, r_hub)
centred_circle(plt, r_rim)
two_leading_two_trailing(plt, 0, lw=2, color='grey')
two_leading_two_trailing(plt, 1, lw=2, color='black')
plt.axis('scaled')
plt.show()
