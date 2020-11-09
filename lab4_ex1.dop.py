def AKM(a,n):
    if n==0:
        return 1
    elif n>0: return a*AKM(a, n-1) 

a=float(input('Введите число:'))
n=int(input('Введите число:'))

print(AKM(a,n))
    