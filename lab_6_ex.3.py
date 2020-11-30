import matplotlib.pyplot as plt
import numpy as np
def circlea_plotter(R=2, title='Circle'):
    x = np.arange(-3.0, 3.0, 0.1)
    y = np.arange(-3.0, 3.0, 0.1)
    X, Y=np.meshgrid(x, y)
    fxy = X**2+Y**2
    plt.contour(X,Y, fxy, levels=[6])
    plt.axis('equal')
    plt.show()
    
circlea_plotter(3)

def circlea_plotter2(R=2, a=1, b=1, title='Circle'):
    x = np.arange(-3.0, 3.0, 0.1)
    y = np.arange(-3.0, 3.0, 0.1)
    X, Y = np.meshgrid(x, y)
    fxy=((X/a)**2+(Y/b)**2)
    plt.contour(X,Y, fxy, levels=[1])
    plt.show()
    
circlea_plotter2(3)   
