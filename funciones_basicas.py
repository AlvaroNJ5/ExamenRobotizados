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
    

