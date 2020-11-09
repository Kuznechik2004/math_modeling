def fib(n):
 f1=1
 f2=2
 for x in range(3, n-1):
    y=f1
    f1=f2
    f2=y+f1
 return f2
print(fib(9))