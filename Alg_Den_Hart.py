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
fi2 = sp.Symbol('fi2')
fi3 = sp.Symbol('fi3')
fi4 = sp.Symbol('fi4')
fi5 = sp.Symbol('fi5')
fi6 = sp.Symbol('fi6')
l3 = sp.Symbol('l3')
l5 = sp.Symbol('l5')
l1 = sp.Symbol('l1')
l2 = sp.Symbol('l2')
d4 = sp.Symbol('d4')

m1 = matriz_algoritmo(30*sp.pi/180,475,150,-sp.pi/2)
m2 = matriz_algoritmo(60*sp.pi/180-sp.pi/2,0,600,0)
m3 = matriz_algoritmo((45-60)*sp.pi/180,0,120,-sp.pi/2)
m4 = matriz_algoritmo(fi4,720,0,sp.pi/2)
m5 = matriz_algoritmo(fi5,0,0,-sp.pi/2)
m6 = matriz_algoritmo(fi6+sp.pi,85,0,0)
msol = mm.multiplica_por_la_derecha(4,m1,m2,m3)
sp.pprint(sp.simplify(msol))

m06 = sp.Matrix([[-0.7405, 0.5611, -0.3696, 1062.88],
                [0.4837, 0.8271, 0.2869, 656.154],
                [0.4664, 0.0332, -0.8839, 275.605],
                [0,0,0,1]])

t36 = msol.inv()*m06
sp.pprint(fb.simplifica_matriz(t36))

t362 = mm.multiplica_por_la_derecha(4,m4,m5,m6)
sp.pprint(sp.simplify(t362))