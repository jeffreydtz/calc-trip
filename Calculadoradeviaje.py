def inicializacion():
    bandera = 0
    gastos = 0
    print("Calculadora de viaje")
    cant_llevada = int(input("Cuanto dinero llevo: "))
    while (bandera != -1):
        bandera = int(input("ingrese su gasto, de ser el ultimo ingrese -1: "))
        if bandera != -1:
            gastos += bandera
    deberia = cant_llevada - gastos
    hay = int(input("Cuanto dinero hay: "))
    print("lo que deberia haber es ", deberia, " y lo que hay es ", hay, " la diferencia es de ", deberia - hay)


inicializacion()
