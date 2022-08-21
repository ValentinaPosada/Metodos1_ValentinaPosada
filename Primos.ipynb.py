import matplotlib.pyplot as plt
import numpy as np

def primos():
    
    n=1
    numerosprimos=[]
    
    while n <= 7925:
        contador=1
        divisores=0
        while contador <= n:
            if n % contador ==0:
                divisores+=1
            contador+=1
        if divisores == 2:
            numerosprimos.append(n)
            
        n+=1
    
    return numerosprimos

def primeros10numerosprimos():
    
    lista=primos()    
    primeros10=[]
    
    for i in range(0,10):
        primeros10.append(lista[i])

    return primeros10
    
def graficaprimos():
    
    lista=primos()
    
    x=np.linspace(1,1000,1000)
    plt.plot(x, lista, color="red")
    
    
    
    
    

    