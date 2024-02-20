import pandas as pd

# Crear un dataframe con los datos de los destinos y sus respectivos valores por persona
destinos = pd.DataFrame({
    'nombre': ['guajira', 'cañon del chicamocha', 'llanos orientales'],
    'valor_adulto': [1450000, 1600000, 1200000],
    'valor_niño': [870000, 960000, 720000]
})

# Crear una lista para almacenar las cotizaciones
cotizaciones = []

# Ciclo para ingresar los datos del cliente y los destinos que desea visitar
while True:
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    nro_personas_adultas = int(input("Ingrese el número de personas adultas: "))
    nro_personas_niños = int(input("Ingrese el número de personas niños: "))
    destino = destinos

    # Crear una cotización para cada destino
    for index, destino in destinos.iterrows():
        subtotal_adultos = nro_personas_adultas * destino['valor_adulto']
        subtotal_niños = nro_personas_niños * destino['valor_niño']
        subtotal = subtotal_adultos + subtotal_niños

        cotizacion = {
            'nombre_cliente': nombre_cliente,
            'nombre_destino': destino['nombre'],
            'nro_personas_adultas': nro_personas_adultas,
            'nro_personas_niños': nro_personas_niños,
            'subtotal_adultos': subtotal_adultos,
            'subtotal_niños': subtotal_niños,
            'subtotal': subtotal
        }

        cotizaciones.append(cotizacion)

    # Preguntar si el cliente desea cotizar otro destino
    continuar = input("¿Desea cotizar otro destino? (s/n): ")

    if continuar.lower() != 's':
        break

# Imprimir las cotizaciones
for cotizacion in cotizaciones:
    print(f"Nombre del cliente: {cotizacion['nombre_cliente']}")
    print(f"Nombre del destino: {cotizacion['nombre_destino']}")
    print(f"Número de personas adultas: {cotizacion['nro_personas_adultas']}")
    print(f"Número de personas niños: {cotizacion['nro_personas_niños']}")
    print(f"Subtotal adultos: {cotizacion['subtotal_adultos']}")
    print(f"Subtotal niños: {cotizacion['subtotal_niños']}")
    print(f"Subtotal: {cotizacion['subtotal']}")
    print()

# Calcular el total de personas adultas, niños y el total de dinero de todos los destinos
total_personas_adultas = sum([cotizacion['nro_personas_adultas'] for cotizacion in cotizaciones])
total_personas_niños = sum([cotizacion['nro_personas_niños'] for cotizacion in cotizaciones])
total_dinero = sum([cotizacion['subtotal'] for cotizacion in cotizaciones])

print(f"Total de personas adultas: {total_personas_adultas}")
print(f"Total de personas niños: {total_personas_niños}")
print(f"Total de dinero: {total_dinero}")