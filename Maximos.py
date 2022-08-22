import matplotlib.pyplot as plt
import numpy as np

def graficadatos():
    
    x=np.loadtxt("EstrellaEspectro.txt", skiprows=1, usecols=[0], unpack=True)
    y=np.loadtxt("EstrellaEspectro.txt", skiprows=1, usecols=[1], unpack=True)

    maximos=[]
    for i in range(1,len(y)-1):
        if y[i+1]<y[i] and y[i]>y[i-1]:
            maximos.append(i)
            
    maximoslocales=maximos
    
    plt.plot(x,y)
    plt.scatter(x[maximoslocales], y[maximoslocales], color="red", marker="o")
    plt.show()
    

