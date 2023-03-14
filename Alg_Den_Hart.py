import numpy as np
import sympy as sp
import Multiplica_matrices as mm
import funciones_basicas as fb

    
def matriz_algoritmo(fi, d, a, alfa):
    'Devuelve una matriz de la forma del algoritmo'

    return sp.Matrix([[sp.cos(fi), -sp.cos(alfa)*sp.sin(fi), sp.sin(alfa)*sp.sin(fi), a*sp.cos(fi)],
                      [sp.sin(fi), sp.cos(alfa)*sp.cos(fi), -sp.sin(alfa)*sp.cos(fi), a*sp.sin(fi)],
                      [0, sp.sin(alfa), sp.cos(alfa), d], 
                      [0,0,0,1]])


#############################################
#Crea las matrices e introducelas a solucion#
#############################################
      

fi1 = sp.Symbol('fi1')
l1 = sp.Symbol('l1')
d2 = sp.Symbol('d2')
d3 = sp.Symbol('d3')
l2 = sp.Symbol('l2')
d4 = sp.Symbol('d4')
fi5 = sp.Symbol('fi5')
l3 = sp.Symbol('l3')
l4 = sp.Symbol('l4')
fi6 = sp.Symbol('fi6')

m1 = matriz_algoritmo(np.pi/2+np.pi/2,l1,0,np.pi/2)

m2 = matriz_algoritmo(np.pi/2,0,0,-np.pi/2)
m3 = matriz_algoritmo(np.pi/2,-1,l2,-np.pi/2)
m4 = matriz_algoritmo(0,1,0,-np.pi/2)
m5 = matriz_algoritmo(-np.pi/2-np.pi/2,l3,0,-np.pi/2)
m6 = matriz_algoritmo(0,l4,0,0)
Solucion = mm.multiplica_por_la_derecha(4, m1,m2,m3,m4,m5,m6)
print(Solucion)






