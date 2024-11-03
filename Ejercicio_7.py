#Clasificar Números por Divisibilidad y Obtener Promedios
# Lista de números enteros
numeros = [12, 25, 30, 45, 60, 72, 85, 90, 100]

# Función para clasificar y calcular promedios
def clasificar_por_divisibilidad(numeros):
    divisibles_por_2 = [n for n in numeros if n % 2 == 0 and n % 3 != 0]
    divisibles_por_3 = [n for n in numeros if n % 3 == 0 and n % 2 != 0]
    divisibles_por_ambos = [n for n in numeros if n % 2 == 0 and n % 3 == 0]
    
    promedios = {
        'Divisibles por 2': sum(divisibles_por_2) / len(divisibles_por_2) if divisibles_por_2 else 0,
        'Divisibles por 3': sum(divisibles_por_3) / len(divisibles_por_3) if divisibles_por_3 else 0,
        'Divisibles por ambos': sum(divisibles_por_ambos) / len(divisibles_por_ambos) if divisibles_por_ambos else 0
    }
    
    return divisibles_por_2, divisibles_por_3, divisibles_por_ambos, promedios

# Ejecutar función de clasificación y promedio
div_2, div_3, div_ambos, promedios = clasificar_por_divisibilidad(numeros)

print("Divisibles por 2:", div_2)
print("Divisibles por 3:", div_3)
print("Divisibles por ambos:", div_ambos)
print("Promedios:", promedios)
