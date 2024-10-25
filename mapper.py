#!/usr/bin/env python
import sys

# Bandera para saltar el encabezado (si es necesario)
header = True

# Función mapper para emitir CUPS y la potencia contratada
for line in sys.stdin:
    # Eliminar espacios en blanco y separar los campos
    line = line.strip()

    # Ignorar el encabezado en la primera línea
    if header:
        header = False
        continue

    # Dividir la línea por punto y coma
    fields = line.split(";")

    # Verificar que la línea tenga 3 campos (CUPS, PERIODO, POTENCIA)
    if len(fields) == 3:
        cups = fields[0]
        potencia = fields[2].replace(',', '.')  # Reemplazar coma por punto decimal

        try:
            # Emitir la clave (CUPS) y el valor (potencia contratada)
            print cups + "\t" + str(float(potencia))
        except ValueError:
            # En caso de error de conversión de potencia, saltar la línea
            continue
