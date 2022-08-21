def factorial(n:int):
    
    base=1
    
    while n > 1:
        base=base*n
        n=n-1
    
    return base 

def variacionessinrepeticion(n:int, r:int):
    
    x=factorial(n)
    y=n-r
    z=factorial(y)
    resultado= x/z
    
    return int(resultado)

def combinacionessinrepeticion(n:int, m:int):
    
    x=factorial(n)
    y=factorial(m)
    z=n-m
    w=factorial(z)
    
    resultado= x/(y*w)
    
    return int(resultado)
