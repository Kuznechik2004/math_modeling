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

def f(x):
    return -507.5*x**2+5368.9*x+11354.9
y=np.vectories(f)
x=np.linespace(-10,10, 50)


plt.figure(figsize=(8,5))

plt.plot(x, y(x), 'r-');




