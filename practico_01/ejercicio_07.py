# Implementar la función mitad(), que devuelve la mitad de palabra.
# Si la longitud es impar, redondear hacia arriba.


# Escribir la función sin utilizar bucles y usando Slices de listas
# Referencia: https://docs.python.org/3/tutorial/introduction.html#lists

def mitad(palabra: str) -> str:
    mitad_ = len(palabra) // 2
    if len(palabra) % 2 == 0:
        return palabra[:mitad_]
    return palabra[:mitad_ + 1]

# NO MODIFICAR
assert mitad("hello") == "hel"
assert mitad("Moon") == "Mo"
assert mitad("") == ""
