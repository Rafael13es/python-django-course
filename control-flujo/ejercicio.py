n1 = None
while True:
    if not n1:
        n1 = int(input("Ingrese el primer número de la operación: "))

    op = int(
        input(
            """
        *****CALCULADORA*****
        Ingrese el numero de la operacion que desea realizar
        1. Suma
        2. Resta
        3. Multiplicacion
        4. Division
        5. Salir

        Opcion: """
        )
    )

    if op == 1:
        n2 = int(input("Ingrese el segundo número de la operación: "))
        result = n1 + n2
        print(f"La suma de {n1} + {n2} = {result}")
    elif op == 2:
        n2 = int(input("Ingrese el segundo número de la operación: "))
        result = n1 - n2
        print(f"La resta de {n1} - {n2} = {result}")
    elif op == 3:
        n2 = int(input("Ingrese el segundo número de la operación: "))
        result = n1 * n2
        print(f"La multiplicación de {n1} * {n2} = {result}")
    elif op == 4:
        n2 = int(input("Ingrese el segundo número de la operación: "))
        result = n1 / n2
        print(f"La división de {n1} / {n2} = {result}")
    else:
        break

    n1 = result
