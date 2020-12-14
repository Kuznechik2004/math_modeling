import matplotlib.pyplot as plt
import matplotlib.image as image
import matplotlib.animation as animation
import numpy as np

plt.style.use('dark_background')

#fig = plt.figure()
fig, ax = plt.subplots()

ax.axis('equal')
ax.axis('off')

img = image.imread('./eee.png')
ax.imshow(img)

#ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
line, = plt.plot([], [], lw=3)

def init():
    pass
    line.set_data([], [])
    return line

xdata, ydata = [], []

ax.set_xlim(-50, 50) # Пределы изменения переменной Х
ax.set_ylim(-50, 50) # Пределы изменения переменной У

def animate(h):
    t = 0.1 * h
    x = 5*t * np.sin(t)
    y = 5*t * np.cos(t)*20.125
    
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata)
    return line, 

plt.title('Траектория полёта 2029-2068')


ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=10)
ani.save('MN4.gif')


