import numpy as np
my_arr=np.array([1,2,4,6])

def my(x):
    """Перемножение всеч элементов входного одномерного массива, 
       подающегося на вход в качестве аргумента"""
   
    x=np.prod(x)
    return x

result = my(my_arr)
print(result)
    
    

    