import numpy as np 
N=5
my_array1=np.zeros(N)
for j in range (N-1):
    my_array1[j] = int(input(f'Input {j}: '))
print(my_array1)
num=int(input('Число'))
k=int(input('Позиция'))
if k>=N:
    print('Позиция плохая')
my_array1=np.insert(my_array1,k,num)
my_array1=np.resize(my_array1, N)
print(my_array1)