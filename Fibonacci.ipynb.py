from matplotlib import pyplot  as plt 
import math

def sucesionfibonacci():
    
    lista=[0,1]
    
    for i in range(2,21):
            lista.append(lista[i-1]+lista[i-2])
            
    return lista 

def graficafibonacci():
    
    x=sucesionfibonacci()
    
    plt.plot(x, label=" Serie Fibonacci")
    plt.xticks(range(0,25,5))
    plt.legend()
    plt.show
    
def numeroaureo():
    
    numeroaureo= (1 + math.sqrt(5))/2  
    lista=sucesionfibonacci()
    limites=[]
    
    for i in range(2,len(lista)):
        
        ultimo=lista[i]
        penultimo=lista[i-1]
        aureo= ultimo/penultimo
        limites.append(aureo)
        
    plt.axhline(numeroaureo, xmin=0, xmax= 17.5, color="red", linestyle="dashed",
                label="Numero Aureo")
    plt.plot(limites, label="Estimacion usando la serie")
    plt.legend()     
    plt.show()

    
    
    
    

