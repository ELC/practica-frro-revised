# Implementar la función es_vocal, que reciba un carácter y # devuelva un 
# booleano en base a si letra es una vocal o no.


# Escribir utilizando un if para cada posibilidad con la función lower()
# Referencia: https://docs.python.org/3/library/stdtypes.html#string-methods

def es_vocal(letra: str) -> bool:
    letra = letra.lower()
    if letra == "a":
        return True
    if letra == "e":
        return True
    if letra == "i":
        return True
    if letra == "o":
        return True
    return letra == "u"

# NO MODIFICAR
assert es_vocal('a') == True
assert es_vocal('b') == False
assert es_vocal('A') == True


# Re-escribir la función utilizando un sólo IF y el operador IN
# Referencia: https://docs.python.org/3/reference/expressions.html#membership-test-operations

def es_vocal(letra: str) -> bool:
    return letra.lower() in "aeiou"

# NO MODIFICAR
assert es_vocal('a') == True
assert es_vocal('b') == False
assert es_vocal('A') == True


# Re-escribir la función utilizando el operador IN pero sin utilizar IF

def es_vocal(letra: str) -> bool:
    return letra.lower() in "aeiou"

# NO MODIFICAR
assert es_vocal('a') == True
assert es_vocal('b') == False
assert es_vocal('A') == True
