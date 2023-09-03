def quitar_espacios(texto: str):
    new_texto = ""
    for char in texto:
        if char != " ":
            new_texto += char
    return new_texto


def reverse(texto: str):
    new_texto = ""
    for char in texto:
        new_texto = char + new_texto
    return new_texto


def es_palindromo(texto: str):
    texto = quitar_espacios(texto)
    new_texto = reverse(texto)
    return texto.lower() == new_texto.lower()


print("Anita lava la tina", es_palindromo("Anita lava la tina"))
print("Sometamos o matemos", es_palindromo("Sometamos o matemos"))
print("Super palindromo", es_palindromo("Super palindromo"))
