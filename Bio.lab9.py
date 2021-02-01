import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 1, 0.5)

def bk_function(m, t):
    dm=k*m
    return dm

m_0=10
k=1.5
   
solve_Bi = odeint(bk_function, m_0, t)
plt.plot(t, solve_Bi[:, 0], label='Увеличение бактерий')
plt.xlabel('Скорость размножения, секунды')
plt.ylabel('Количество бактерий')
pit.title('Скорость размножения бактерий')
plt.legend()

plt.show()