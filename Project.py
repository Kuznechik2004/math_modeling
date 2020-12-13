import matplotlib.pyplot as plt
import numpy as np

def MN4_plotter(R=6.371, title='Apofis2068'):
    x = np.arange(-40, 40, 0.5)
    y = np.arange(-40, 40, 0.5)
    X,Y = np.meshgrid(x,y)
    fxy = X**2+Y**2
    plt.contour(X, Y, fxy,levels=[120])
    plt.axis('equal')
    plt.grid()
MN4_plotter()


from matplotlib.path import Path
import matplotlib.patches as patches

verts=[(-40, -40),
       (-20, -30), 
       (0,-20),
       (20, -10),
       (15, 10),
       ]

codes = [Path.MOVETO,
         Path.CURVE4,
         Path.CURVE4,
         Path.CURVE4]

fig = plt.figure()
ax = fig.add_subplot(111)
patch = patches.PathPatch(Path, facecolor='none', lw=3)
ax.add_patch(patch)

xs, ys = zip(*verts)
ax.plot(xs, ys, 'x--', lw=3, color='r', ms=10)

ax.text(-10, -10, 'P0')
ax.text(16, 12, 'P1')

plt.show()


