import matplotlib_pyplot as plt

def stairs(N=0, title='Ladder'):
    x=[0]
    y=[0]
    
    for t in range(N):
        x+=[t, t+1]
        y+=[t+1]*2
        
    plt.plot(x, y, color='c', label='Ladder')
    
    plt.legend()
    plt.title(title)
    
    plt.show()
    
num=int(input('Number of steps= '))
stairs(num)