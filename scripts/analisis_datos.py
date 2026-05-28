# analisis_datos.py
# Trabajo Practico - Organizacion Empresarial
# TUPaD UTN 2026
# Escenario B - Analisis de Ventas
# Autor: Persona B
# Jira: TO2-15

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------------------
# PASO 1: Cargar el dataset
# Leemos el archivo CSV guardado en la carpeta /datos
# usando ruta relativa para garantizar reproducibilidad
# --------------------------------------------------
df = pd.read_csv("datos/ventas.csv")

print("Dataset cargado correctamente")
print("Primeras filas:")
print(df.head())
print()

# Convertimos la fecha a formato datetime
df["sales_date"] = pd.to_datetime(df["sales_date"])

# --------------------------------------------------
# PASO 2: Calcular los indicadores pedidos
# --------------------------------------------------

# Ventas totales: sumamos todos los montos del año
ventas_totales = df["sales_amount"].sum()
print(f"Ventas totales del año: ${ventas_totales:,.2f}")

# Producto mas vendido: agrupamos por producto y sumamos cantidades
ventas_por_producto = df.groupby("producto")["cantidad"].sum()
producto_mas_vendido = ventas_por_producto.idxmax()
print(f"Producto mas vendido: {producto_mas_vendido}")
print()
print("Ventas por producto:")
print(ventas_por_producto.sort_values(ascending=False))
print()

# Ventas por mes: agrupamos por mes y sumamos los montos
df["mes"] = df["sales_date"].dt.to_period("M")
ventas_por_mes = df.groupby("mes")["sales_amount"].sum()
print("Ventas por mes:")
print(ventas_por_mes)


# --------------------------------------------------
# PASO 3: Generar el grafico de evolucion de ventas
# Usamos un grafico de barras para ver como variaron
# las ventas a lo largo de los 12 meses del año 2024
# --------------------------------------------------
plt.figure(figsize=(12, 6))

ventas_por_mes.plot(kind="bar", color="steelblue")

plt.title("Evolucion de Ventas por Mes - 2024")
plt.xlabel("Mes")
plt.ylabel("Monto total de ventas ($)")
plt.xticks(rotation=45)

# Agregamos el valor encima de cada barra
# para que sea mas facil de leer el grafico
for i, valor in enumerate(ventas_por_mes):
    plt.text(i, valor + 500, f"${valor:,.0f}", ha="center", fontsize=7)

plt.tight_layout()
plt.savefig("resultados/grafico_ventas.png")
plt.show()
print("Grafico guardado en resultados/grafico_ventas.png")

# --------------------------------------------------
# PASO 4: Guardar un resumen con los resultados
# --------------------------------------------------
resumen = f"""RESUMEN DE ANALISIS DE VENTAS - 2024
=====================================
Dataset fuente: sales_sample_2024.csv
Registros analizados: {len(df)}

Ventas totales del año:  ${ventas_totales:,.2f}
Producto mas vendido:    {producto_mas_vendido}
Mes con mas ventas:      {ventas_por_mes.idxmax()} (${ventas_por_mes.max():,.2f})
Mes con menos ventas:    {ventas_por_mes.idxmin()} (${ventas_por_mes.min():,.2f})
"""

with open("resultados/resumen.txt", "w") as f:
    f.write(resumen)

print("Resumen guardado en resultados/resumen.txt")
print()
print(resumen)
