#!/usr/bin/env python
import sys

# Diccionario para almacenar la suma de potencias por CUPS
sums = {}

# Leer las líneas de entrada
for line in sys.stdin:
    line = line.strip()
    cups, potencia = line.split("\t")  # Separar clave y valor

    # Convertir la potencia a float
    try:
        potencia = float(potencia)
    except ValueError:
        continue  # Si hay un error, saltar la línea

    # Sumar potencias por cada CUPS
    if cups in sums:
        sums[cups] += potencia
    else:
        sums[cups] = potencia

# Imprimir los resultados
for cups, total_potencia in sums.items():
    print cups + "\t" + str(total_potencia)

