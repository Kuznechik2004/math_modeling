import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

plt.style.use('dark_background')
plt.grid(True)
t = np.arange(0, 10, 0.08)

def bk_function(m, t):
    dm=-k*m
    return dm

m_0=1000
k=0.08
   
solve_Bi = odeint(bk_function, m_0, t)
plt.plot(t, solve_Bi[:, 0], label='Изменение инвестиций')
plt.xlabel('Время')
plt.ylabel('Объём инвестиций')
pit.title('Скорость размножения бактерий')
plt.legend()

plt.show()
