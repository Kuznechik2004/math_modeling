c=int(input('ВВЕДИТЕ ЧИСЛО:'))
for a in range (0,c):
    s=0
    for b in range(1,a):
        if a%b==0:
           s=s+b
    if s==a:
        print(a)