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

phi1, phi2, phi3, phi4,l1,l2,l3 = sp.symbols('phi_1 phi_2 phi_3 phi_4 l1 l2 l3')
alpha1, alpha2, alpha3 = sp.symbols('alpha_1 alpha_2 alpha_3')
omega1, omega2, omega3 = sp.symbols('omega_1 omega_2 omega_3')

m1 = sp.Matrix([[-0.7405, 0.5611, -0.3696, 1062.88],
                [0.4837, 0.8271, 0.2869, 656.154],
                [0.4664, 0.0332, -0.8839, 275.605],
                [0,0,0,1]])
sol = m1*sp.Matrix([0,0,-85,1])

m2 = cm.mth_z(phi1,0,0,0)
m3 = cm.mth_y(0,0,1,0)
m4 = cm.mth_z(-phi3,0,0,0)
m5 = cm.mth_y(0,0.5,0,0)
m6 = cm.mth_z(phi4,0,0,0)
m7 = cm.mth_y(0,0.5,0,0)
sol = mm.multiplica_por_la_derecha(4,m2,m3,m4,m5,m6,m7)
sp.pprint(sp.simplify(sol))
a = sp.solve([sp.sin(phi1)+0.5*sp.sin(-phi3)-1.166, sp.cos(phi1)-0.5*sp.cos(-phi3)-0.7], [phi1,phi3])
print(a)