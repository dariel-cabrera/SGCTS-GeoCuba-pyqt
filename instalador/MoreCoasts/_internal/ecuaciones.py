import math
def transporte_logitudinal_arena(p,k,ps,n,hb,a,g):
    # p-Densidad del Mar  1025
    # g aceleracion gravitatoria 9.8 
    # k- Inidice de Rompiente 0.78
    # ps- Densidad Arena 2650
    # n -Coeficiente de porocidad  0.4
    # hb altura 0.29
    # a- angulo de Rompiente 20
    # K- Constante de Komar e Inman 0.77
   

    N=(p * math.sqrt(g))
    D=(16 * math.sqrt(k) )* (ps-p)*(1-n)
   
    
    if D==0:
        return False
    else:
        Q= (N)/ (D) * math.sqrt(math.pow(hb,5))* math.sin(2*a)
        print(Q)
        return Q


def obtniedo_K(P,Q):
    if Q==0:
        return False
    else:
        return P / Q 
