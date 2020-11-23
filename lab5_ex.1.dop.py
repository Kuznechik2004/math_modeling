from sympy import symbols 
from sympy.vector import CoordSys3D
from sympy import acos, trigsimp
import math

N=CoordSys3D('N')
#a,b,c=symbols('a,b,c') 

a = 4*N.i + 3*N.j + 8*N.k
b = -2*N.i + 8*N.j + 7*N.k
c = -5*N.i - 6*N.j + 12*N.k

def aaaa(v1,v2):
    res = v1.dot(v2)/(a1*b1)
    return res


P = a.dot(b)
V = a.dot(c)
K = b.dot(c)

a1 = a.magnitude()
b1 = b.magnitude()
c1 = c.magnitude()

r1 = P/(a1*b1)
x=acos(r1)

r2 = V/(a1*c1)
y=acos(r2)

r3 = K/(b1*c1)
z=acos(r3)

print(math.degrees(x.evalf()))
print(math.degrees(y.evalf()))
print(math.degrees(z.evalf()))


