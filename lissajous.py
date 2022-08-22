import matplotlib.pyplot as plt
import numpy as np

def lissajous(desfase):

    A=1 
    theta=np.linspace(0, 2*np.pi, 200)
    fig = plt.figure(figsize=(4,4))
    nx = [1,2,3,4,5]
    n=5
    k=0
    for i in range(1,len(nx)+1):
        k+=i-1
        for g in range(i,len(nx)+1):
            
            k+=1
            imagen=fig.add_subplot(n,n,k)
            imagen.plot(A*(np.sin(i*theta)), A*(np.sin(g*theta + desfase)))
            plt.axis("off")
                     
desfase = [0, np.pi/4, np.pi/2]         
for j in range(0,3):
    lissajous(desfase[j])
    
plt.show()


                

                                  

    
                

                
    
                

               
    
    
    
 
               
