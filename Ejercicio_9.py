#Agrupación y Filtrado de Fechas por Mes
from datetime import datetime

# Lista de fechas en formato de cadena
fechas = ["2024-01-15", "2024-01-20", "2024-02-05", "2024-02-15", "2024-03-10", "2024-03-25", "2024-01-28"]

# Convertir a objetos datetime y agrupar por mes y año
def agrupar_por_mes(fechas):
    fechas_dt = [datetime.strptime(fecha, "%Y-%m-%d") for fecha in fechas]
    agrupados = {}
    for fecha in fechas_dt:
        mes_año = (fecha.year, fecha.month)
        if mes_año not in agrupados:
            agrupados[mes_año] = []
        agrupados[mes_año].append(fecha)
    
    # Filtrar meses con más de dos fechas
    meses_con_mas_de_dos_fechas = {k: v for k, v in agrupados.items() if len(v) > 2}
    return meses_con_mas_de_dos_fechas

# Ejecutar agrupamiento y filtrado
fechas_filtradas = agrupar_por_mes(fechas)

print("Meses con más de dos fechas:", fechas_filtradas)
