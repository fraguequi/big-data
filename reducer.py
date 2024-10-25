#!/usr/bin/env python
import sys

current_cups = None
current_sum = 0.0

# Reducer para sumar potencias por CUPS
for line in sys.stdin:
    # Eliminar espacios en blanco
    line = line.strip()

    # Separar el CUPS y la potencia
    fields = line.split("\t")
    if len(fields) != 2:
        continue

    cups = fields[0]
    try:
        potencia = float(fields[1])
    except ValueError:
        # Ignorar si la potencia no es un número
        continue

    # Si cambiamos de CUPS, imprimimos el CUPS anterior y su suma
    if current_cups == cups:
        current_sum += potencia
    else:
        if current_cups:
            # Imprimir el resultado para el CUPS anterior
            print(current_cups + "\t" + str(current_sum))

        # Actualizar para el nuevo CUPS
        current_cups = cups
        current_sum = potencia

# Imprimir la última entrada
if current_cups:
    print(current_cups + "\t" + str(current_sum))

