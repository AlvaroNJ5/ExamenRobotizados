import math

def ecuacion_trigonometrica(x):
    return math.sin(x) - 0.5

def derivada_ecuacion(x):
    return math.cos(x)

def newton_raphson(ecuacion, derivada, x0, epsilon, max_iter):
    iteracion = 0
    error = abs(ecuacion(x0))

    while error > epsilon and iteracion < max_iter:
        x1 = x0 - ecuacion(x0) / derivada(x0)
        error = abs(ecuacion(x1))
        x0 = x1
        iteracion += 1

    if error <= epsilon:
        return x0
    else:
        return None

# Ejemplo de uso
x0 = 1.0  # Valor inicial
epsilon = 1e-6  # Tolerancia para el error
max_iter = 100  # Máximo número de iteraciones

solucion = newton_raphson(ecuacion_trigonometrica, derivada_ecuacion, x0, epsilon, max_iter)

if solucion is not None:
    print("La solución aproximada es:", solucion)
else:
    print("No se pudo encontrar una solución.")