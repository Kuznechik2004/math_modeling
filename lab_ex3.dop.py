import numpy as np
A=int(input('Введите значение A:'))
B=int(input('Введите значение B:'))
my_array1=np.zeros(shape = (A,B))

my_array3=np.zeros(B)
for (i,j),x in np.ndenumerate(my_array1):
    print(i,j,x, sep=";")
    m = input(f'введите значения array1:[{i},{j}]:')
    my_array1[i,j] = float(m)
print(my_array1)


for (i,j),x in np.ndenumerate(my_array1):
    if(my_array3[j] < my_array1[i,j]):
        my_array3[j]=my_array1[i,j]
    
    
print(my_array3)   

