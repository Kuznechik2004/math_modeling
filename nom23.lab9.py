import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

plt.grid(True)
t = np.arange(0, 5, 0.5)

def bk_function(V, t):
    a=F/m
    dmdt=V_0+a*t/2
    return V
F=5
m=5
V_0=0
k=5
   
solve_Bi = odeint(bk_function, V_0, t)
plt.plot(t, solve_Bi[:, 0], label='Материальная точка')
plt.xlabel('Время')
plt.ylabel('Скорость')
plt.title('Изменение скорости со временем')
plt.legend()

plt.show()
