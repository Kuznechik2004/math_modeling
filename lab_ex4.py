k=input('Введите число:')
k=int(k)
kc=1
kn=1
print(kc, kn, sep='\n')
for m in range (2, k, 1):
    S=kc+kn
    kc=kn
    kn=S
    print(S)