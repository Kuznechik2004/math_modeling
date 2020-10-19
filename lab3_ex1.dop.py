import numpy as np 
my_array1=np.zeros(shape = (4,3))
for (i,j),x in np.ndenumerate(my_array1):
    print(i,j,x, sep=";")
    #m = input('введите значения:[%d,%d]: '%(i,j))
    m = input(f'введите значения array1:[{i},{j}]:')
    my_array1[i,j] = float(m)
print(my_array1)
my_array2=np.zeros(shape = (4,3))
for (i,j),x in np.ndenumerate(my_array2):
    print(i,j,x, sep=";")
    m = input(f'введите значения array2:[{i},{j}]:')
    my_array2[i,j] = float(m)
print(my_array2)
my_array3=np.zeros(shape = (4,3))
for (i,j),x in np.ndenumerate(my_array3):
    if my_array1[i,j] > my_array2[i, j]:
       my_array3[i,j] = my_array1[i, j]
    else:
       my_array3[i,j] = my_array2[i,j] 
print(my_array3)      
       