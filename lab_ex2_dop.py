a=int(input('a= '))
b=int(input('b= '))
c=int(input('c= '))
if a + b <= c or b + c <= a or a + c <= b:
     print('Треугольника не существует')
elif a==b and b==c  and a==c:
     print('Треугольник равносторонний')
elif a!=b and b!=c and c!=a:
     print('Треугольник разносторонний')
else:
     print('Треугольник равнобедренный')