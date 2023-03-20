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
      
l1 = sp.Symbol('l1')
l2 = sp.Symbol('l2')
a = sp.Symbol('a')
l3 = sp.Symbol('l3')
l4 = sp.Symbol('l4')
l5 = sp.Symbol('l5')
m1 = matriz_algoritmo(3*sp.pi/2, l1+l2, -a, -sp.pi/2)
m2 = matriz_algoritmo(0, 0, -l3, sp.pi)
m3 = matriz_algoritmo(0, 0, l4, sp.pi)
m4 = matriz_algoritmo(-sp.pi/2, 0, 0, -sp.pi/2)
m6 = matriz_algoritmo(sp.pi/2, -l5, 0, sp.pi) 
sp.pprint(mm.multiplica_por_la_derecha(4,m1,m2,m3,m4,m6))




