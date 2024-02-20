def calcular_bonos():
    estratos = [1, 2]
    hijos_por_estrato = {1: 0, 2: 0}
    bonos_por_estrato = {1: 20000, 2: 16500}
    bonos_por_hijos = {0: 0, 1: 25000, 2: 30000}
    total_dinero_entregado = {1: 0, 2: 0}
    total_personas_por_estrato = {1: 0, 2: 0}
    total_personas_sin_hijos = 0
    total_personas_con_menos_de_3_hijos = 0
    total_personas_con_mas_de_3_hijos = 0
    total_personas_con_hijos = 0

    while True:
        estrato = int(input("Ingrese el estrato (1 o 2) o 0 para terminar: "))
        if estrato == 0:
            break
        elif estrato not in estratos:
            print("Estrato no válido. Por favor, ingrese 1 o 2.")
            continue

        hijos = int(input("Ingrese la cantidad de hijos (0 a 3 o mas): "))
        if hijos < 0 or hijos > 3:
            #print("Cantidad de hijos no válida. Por favor, ingrese 0 a 3 o mas.")
            continue

        hijos_por_estrato[estrato] += 1
        total_personas_por_estrato[estrato] += 1
        total_personas_con_hijos = total_personas_con_menos_de_3_hijos + total_personas_con_mas_de_3_hijos

        if hijos == 0:
            total_personas_sin_hijos += 1
        elif hijos == 1:
            total_personas_con_menos_de_3_hijos += 1
        elif hijos == 2:
            total_personas_con_menos_de_3_hijos += 1
            total_dinero_entregado[estrato] += bonos_por_hijos[2]
        elif hijos == 3:
            total_personas_con_mas_de_3_hijos += 1
            total_dinero_entregado[estrato] += bonos_por_hijos[2]

        total_dinero_entregado[estrato] += bonos_por_estrato[estrato]

    print("\nResultados:")
    print("Cantidad de personas del estrato 1:", total_personas_por_estrato[1])
    print("Cantidad de personas del estrato 2:", total_personas_por_estrato[2])
    print("Total de personas sin hijos:", total_personas_sin_hijos)
    print("Total de personas con menos de 3 hijos:", total_personas_con_menos_de_3_hijos)
    print("Total de personas con más de 3 hijos:", total_personas_con_mas_de_3_hijos)
    print("Total de personas con hijos:", total_personas_con_mas_de_3_hijos + total_personas_con_menos_de_3_hijos)
    print("Total de dinero entregado por personas que no tienen hijos:", total_dinero_entregado[1])
    print("Total de dinero entregado por personas que tienen hasta dos hijos:", total_dinero_entregado[2])
    print("Total de dinero entregado a personas que tinen 3 o más hijos:", total_dinero_entregado[1] + total_dinero_entregado[2])
    print("Total pagado por los bonos:", total_dinero_entregado[1] + total_dinero_entregado[2])

calcular_bonos()