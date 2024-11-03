#Filtrar y Agrupar Palabras por Longitud y Frecuencia
# Lista de palabras

palabras = ['Python', 'Ejercicio!', 'Desafío', 'Código', 'Listas', 'Filt*rar', 'Grupo', 'Computación', 'Avanzado']

# Filtrar palabras que solo contienen letras
palabras_filtradas = list(filter(lambda palabra: palabra.isalpha(), palabras))

# Función para agrupar por longitud y contar frecuencia
def agrupar_por_longitud(palabras):
    agrupadas = {}
    for palabra in palabras:
        longitud = len(palabra)
        if longitud not in agrupadas:
            agrupadas[longitud] = []
        agrupadas[longitud].append(palabra)
    # Calcular frecuencia de palabras por longitud
    frecuencias = {longitud: len(palabras) for longitud, palabras in agrupadas.items()}
    return agrupadas, frecuencias

# Ejecutar función de agrupamiento y frecuencia
agrupadas, frecuencias = agrupar_por_longitud(palabras_filtradas)

print("Palabras agrupadas por longitud:", agrupadas)
print("Frecuencia por longitud:", frecuencias)
