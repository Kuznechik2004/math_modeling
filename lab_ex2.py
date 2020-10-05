b=input('Первое число:')
b=int(b)
q=input('Знаменатель:')
q=int(q)
n=input('Количество членов прогрессии:')
n=int(n)
for c in range(1,n+1,1):
     print(b*q**(n-1))