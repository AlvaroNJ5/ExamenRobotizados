import pyquaternion as pq
import numpy as np
import sympy as sp
import simbolicquaternions as sq
#######Notas
'''
https://kieranwynn.github.io/pyquaternion/#welcome

https://www.tutorialspoint.com/sympy/sympy_quaternion.htm


###PYQUATERNIONS

-   Se normalizan AUTOMATICAMENTE AL DECLARARLOS
-   ROTACION DE UN VECTOR
    q1 = pq.Quaternion(axis=[3,-2,1], angle=np.pi/2)
    solucion = q1.rotate([5,2,-6])

###SYMPY
-   ROTACIÓN DE UN VECTOR
    q1 = sq.quaternion_simbolico_normalizado(axis=[3,-2,1], angle=np.pi/2)
    q1conj = sq.conjugado_cuaternio(q1)
    vector = sp.Quaternion(0, 5, 2, -6)   #OJO. No es realmente un cuaternio. Hay que definirlo de esta manera.
    solucion = q1.mul(vector).mul(q1conj)
'''

q1 = pq.Quaternion(axis=[3,-2,1], angle=np.pi/2)
r_prim = q1.rotate([5,2,-6])










