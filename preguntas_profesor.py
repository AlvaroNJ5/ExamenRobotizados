import CreaMTH as cm
import sympy as sp
import Multiplica_matrices as mm

import simbolicquaternions as sq
import numpy as np
import pyquaternion as pq
import funciones_basicas as fb

###EJERCICIO 1 PARCIAL 2021
'''
a = 0
alfa = 2*sp.pi/3
x = sp.Symbol('x')
y = sp.Symbol('y')
z = sp.Symbol('z')
m1 = cm.mth_z(a*sp.pi/2,0,0,0)
m2 = cm.mth_y(sp.pi - alfa,0,0,0)
quat = fb.matriz_a_cuaternio(m1@m2)
vector = sp.Quaternion(0,x,y,z)
print(quat.mul(vector).mul(sq.conjugado_cuaternio(quat)))
q2 = sp.Quaternion(0.91085, 0.06403, -0.37728, -0.15459)

print(q2.mul(vector).mul(sq.conjugado_cuaternio(q2)))
'''

#Ej practicas
'''
q1 = sq.quaternion_simbolico_normalizado(axis=[0,0,1], angle=15*sp.pi/180)
q2 = sq.quaternion_simbolico_normalizado(axis=[1,0,0], angle=25*sp.pi/180)
q3 = sq.quaternion_simbolico_normalizado(axis=[0,1,0], angle=60*sp.pi/180)
a2 = sq.tras_rot_moviles(q3, [3,3,3], [0,6,0])
a1 = sq.tras_rot_moviles(q2, [a2.args[1],a2.args[2],a2.args[3]], [-3,3,7])
a0 = sq.tras_rot_moviles(q1, [a1.args[1],a1.args[2],a1.args[3]], [4,4,0])
print(a0)
a2 = sq.tras_rot_moviles(q3, [0,0,0], [0,6,0])
a1 = sq.tras_rot_moviles(q2, [a2.args[1], a2.args[2], a2.args[3]], [-3,3,7])
a0 = sq.tras_rot_moviles(q1, [a1.args[1], a1.args[2], a1.args[3]], [4,4,0])
print(a0)
a1 = sq.tras_rot_moviles(q2, [0,0,0], [-3,3,7])
a0 = sq.tras_rot_moviles(q1, [a1.args[1], a1.args[2], a1.args[3]], [4,4,0])
print(a0)
'''

#Ej 1 Jun 2022
'''
q2 = sq.quaternion_simbolico_normalizado(axis=[1,2,3],angle=30*sp.pi/180)

m2 = fb.cuaternio_a_matriz_rot(q2)
m2 = sp.Matrix([[0.8756, -0.3817, 0.2959,0], [0.4200, 0.9043, -0.0763,0], [-0.2383, 0.1911, 0.9522,0],[0,0,0,1]])
m2_0 = sp.Matrix([[-0.182727351487519, 0.744993875689897, 0.641579056404227,1], 
           [-0.0507145931441733, -0.658879887168082, 0.750612989984513,1], 
           [0.981918048052039, 0.104598068120959, 0.158008515202915,1],[0,0,0,1]])

m1 = m2.inv()@m2_0.inv()
q1 = fb.matriz_a_cuaternio(m1)
sol = sq.tras_rot_moviles(q1, [-0.366,-0.183,-1.683],[-0.749,-0.191,-1.55])
print(sol)

'''