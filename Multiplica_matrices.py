import numpy as np
import sympy as sp
import funciones_basicas as fb
#Script básico con dos funciones para multiplicar MTHs por la izquierda o la derecha

def multiplica_por_la_derecha(tamaño_matriz, *matrices):
    'Multiplica tantas matrices como desees por la derecha. INTRODUCIR EN ORDEN DE IZQUIERDA A DERECHA (NATURAL)'
    matriz_salida = np.identity(tamaño_matriz)
    for matriz in matrices:
        matriz_salida = matriz_salida @ matriz
    return fb.simplifica_matriz(matriz_salida)

def multiplica_por_la_izquierda(tamaño_matriz, *matrices):
    'Multiplica tantas matrices como desees por la izquierda. INTRODUCIR EN ORDEN DE IZQUIERDA A DERECHA (NATURAL)'
    matriz_salida = np.identity(tamaño_matriz)
    for matriz in matrices:
        matriz_salida = matriz @ matriz_salida
    return fb.simplifica_matriz(matriz_salida) 

