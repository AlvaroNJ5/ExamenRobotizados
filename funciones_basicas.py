import numpy as np
import sympy as sp

def simplifica_matriz(matriz):
    'Metodo para simplificar matrices'
    for i in range(len(matriz)):
        matriz[i] = matriz[i].evalf(4)
        try:
            matriz[i] = round(matriz[i],4)
        except TypeError:
            for a in sp.preorder_traversal(matriz[i]):
                if isinstance(a, sp.Float):
                    matriz[i] = matriz[i].subs(a, round(a,4))   
    return matriz

def simplifica_cuat_simbolico(cuaternion):
    'Metodo para simplificar cuaterniones simbolicos'
    for i in range(len(cuaternion)):
        cuaternion[i] = cuaternion[i].evalf(4)
        try:
            cuaternion[i] = round(cuaternion[i],4)
        except TypeError:
             for a in sp.preorder_traversal(cuaternion[i]):
                if isinstance(a, sp.Float):
                    cuaternion[i] = cuaternion[i].subs(a, round(a,4))  
    return cuaternion
    
def matriz_a_cuaternio(matriz):
    'FUNCIONA A MATRIZ DE UNA MTH'
    q0 = ((matriz[0]+matriz[5]+matriz[10]+1)**(1/2))/2
    if matriz[9]>= matriz[6]:
        q1 = ((matriz[0]-matriz[5]-matriz[10]+1)**(1/2))/2
    else:
        q1 = -((matriz[0]-matriz[5]-matriz[10]+1)**(1/2))/2
    if matriz[2]>=matriz[8]:
        q2 = ((-matriz[0]+matriz[5]-matriz[10]+1)**(1/2))/2
    else:
        q2 = -((-matriz[0]+matriz[5]-matriz[10]+1)**(1/2))/2
    if matriz[4]>=matriz[1]:
        q3 = ((-matriz[0]-matriz[5]+matriz[10]+1)**(1/2))/2
    else:
        q3 = ((-matriz[0]-matriz[5]+matriz[10]+1)**(1/2))/2
    return sp.Quaternion(q0,q1,q2,q3)

def cuaternio_a_matriz_rot(cuaternio):
    'USAR SOLO EN CUATERNIOS SIMBOLICOS'
    q0 = cuaternio.args[0]
    q1 = cuaternio.args[1]
    q2 = cuaternio.args[2]
    q3 = cuaternio.args[3]
    a00 = -q2**2-q3**2+1/2
    a01 = q1*q2-q3*q0
    a02 = q1*q3+q2*q0
    a10 = q1*q2+q3*q0
    a11 = -q1**2-q3**2+1/2
    a12 = q2*q3-q1*q0
    a20 = q1*q3-q2*q0
    a21 = q2*q3+q1*q0
    a22 = -q1**2-q2**2+1/2
    return simplifica_matriz(sp.Matrix([[2*a00,2*a01,2*a02],[2*a10,2*a11,2*a12],[2*a20,2*a21,2*a22]]))
    
