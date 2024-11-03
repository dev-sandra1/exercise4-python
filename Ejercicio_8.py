#Calcular Suma de Dígitos y Agrupar por Suma
# Lista de números enteros
numeros = [15, 23, 45, 54, 76, 89, 100, 123, 250]

# Función para calcular suma de dígitos y agrupar
def agrupar_por_suma_de_digitos(numeros):
    agrupados = {}
    for num in numeros:
        suma_digitos = sum(int(digito) for digito in str(num))
        if suma_digitos not in agrupados:
            agrupados[suma_digitos] = []
        agrupados[suma_digitos].append(num)
    return agrupados

# Ejecutar agrupación por suma de dígitos
agrupados_por_suma = agrupar_por_suma_de_digitos(numeros)

print("Números agrupados por suma de dígitos:", agrupados_por_suma)
