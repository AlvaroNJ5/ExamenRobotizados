import CreaMTH as cm
import sympy as sp
import Multiplica_matrices as mm
import simbolicquaternions as sq
import numpy as np
import pyquaternion as pq
import funciones_basicas as fb

'''
SISTEMAS ECUACIONES
ny =sp.Symbol('ny')
oy =sp.Symbol('oy')
ay =sp.Symbol('ay')
a = sp.solve([-1.872*ny+3.216*oy+0.388*ay-2, 0.915*ny+3.554*oy+0.726*ay-2, -0.9*ny+5.1*oy+2.26*ay-2], [ny, oy, ay])
'''
'''
PRODUCTO VECTORIAL
n1 = sp.Matrix([n2[0],n2[1],n2[2]])
o1 = sp.Matrix([o1[0],o1[1],o1[2]])
a1 = n1.cross(o1)
'''

q1 = sp.Quaternion(0.91085, 0.06403, -0.37728, -0.15459)
m1 = fb.cuaternio_a_matriz_rot(q1)
sp.pprint(m1)
print(f'\n\n\n')
angulo = [np.pi/2+np.pi/6,np.pi/2-np.pi/6, -np.pi/2+np.pi/6, -np.pi/2-np.pi/6]
for ang in angulo:
    sp.pprint(cm.mth_x(ang,0,0,0))
    print('----------------------------')

