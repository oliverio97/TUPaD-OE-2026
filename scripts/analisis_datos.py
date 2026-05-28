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
