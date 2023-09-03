"""Obtiene un producto"""


def get_product(**datos: dict[str, str]):
    """Obtiene un producto

    Args:
        **datos (dict[str, str]): datos del producto
    """
    print(datos["id"], datos["name"])


get_product(id="id", name="iPhone", desc="Esto es un iPhone")
