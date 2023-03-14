import numpy as np
import sympy as sp

def mth_x(alfa, x, y, z):
    'Define una MTH con matriz de rotación sobre eje x'
    return sp.Matrix([[1, 0, 0, x],[0, sp.cos(alfa), -sp.sin(alfa), y],[0, sp.sin(alfa), sp.cos(alfa), z],[0, 0, 0, 1]])
    

def mth_y(alfa, x, y, z):
    'Define una MTH con matriz de rotación sobre eje x'
    return sp.Matrix([[sp.cos(alfa), 0, sp.sin(alfa), x],[0, 1, 0, y],[-sp.sin(alfa), 0, sp.cos(alfa), z],[0, 0, 0, 1]])

def mth_z(alfa, x, y, z):
    'Define una MTH con matriz de rotación sobre eje x'
    return sp.Matrix([[sp.cos(alfa), -sp.sin(alfa), 0, x],[sp.sin(alfa), sp.cos(alfa), 0, y],[0, 0, 1, z],[0, 0, 0, 1]])





