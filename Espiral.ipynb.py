import numpy as np
import matplotlib.pyplot as plt

def espiralarquimedes():
    
    a=0
    b=1
    teta=np.arange(0, 6*np.pi, 0.01)
    
    r=a+(b*teta)
    
    x= r*(np.cos(teta))
    y=r*(np.sin(teta))  
    plt.plot(x,y, color="purple")
    plt.xticks(range(-15,25,5))
    plt.yticks(range(-15,25,5))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


