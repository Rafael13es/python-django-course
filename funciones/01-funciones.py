"""Functions"""


def hola(nombre: str, apellido: str = "Feliz"):
    """Print name

    Parameters
    ----------
    nombre : str
        name
    apellido : str
        lastname
    """
    print("Hola Mundo!")
    print(f"Bienvenido {nombre} {apellido}")


hola("Nicolas", "Schurmann")
hola("Chanchito")

hola(apellido="Schurmann", nombre="Wolfgang")
