#Clasificar Fracciones por Valor y Agrupar por Intervalos
from fractions import Fraction

# Lista de fracciones (numerador, denominador)
fracciones = [(1, 2), (3, 4), (1, 3), (5, 6), (7, 8), (1, 4), (2, 3), (3, 5)]

# Función para clasificar fracciones por intervalo
def agrupar_por_valor(fracciones, intervalo=0.5):
    fracciones_valores = [Fraction(num, den) for num, den in fracciones]
    agrupados = {}
    for fraccion in fracciones_valores:
        valor = float(fraccion)
        rango_min = int(valor // intervalo) * intervalo
        rango_max = rango_min + intervalo
        rango = f"{rango_min}-{rango_max}"
        if rango not in agrupados:
            agrupados[rango] = []
        agrupados[rango].append(fraccion)
    return agrupados

# Ejecutar agrupación por valor
fracciones_agrupadas = agrupar_por_valor(fracciones)

print("Fracciones agrupadas por valor:", fracciones_agrupadas)
