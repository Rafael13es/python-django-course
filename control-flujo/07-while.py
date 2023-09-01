# numero = 1

# while numero < 100:
#     print(numero)
#     numero *= 2

command = ""

while command.lower() != "salir":
    command = input("$ ")
    print(command)
    if command.lower() == "salir":
        break
