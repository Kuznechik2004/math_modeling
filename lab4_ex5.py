import math

def k(a):
    x=math.pi*(a**2)
    return x  

def p(a,b):
    x=a*b
    return x 

def t(a, b, c):
    h=(a+b+c)/2
    x = math.sqrt((h*(h-a)*(h-b)*(h-c)))
    return x

print('круг-', 1)
print('прямоугольник-', 2)
print('треугольник-', 3)
m=int(input('Выберете фигуру: '))

if m==1:
     a=float(input('Введите радиус:'))
     print(k(a)) 
     
elif m==2:
    a=float(input('Введите сторону а: '))
    b=float(input('Введите сторону b:'))
    print(p(a, b))
    
elif m==3:
    a=float(input('Введите сторону а: '))
    b=float(input('Введите сторону b: '))
    c=float(input('Введите сторону с: '))
    print(t(a, b, c))