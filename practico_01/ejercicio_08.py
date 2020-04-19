# Implementar la función es_palindromo(), que devuelva un booleano en base a
# si palabra se lee igual de corrido como al revés. Ejemplos: arenera, radar,
# ojo, oso, salas.


# Escribir la función sin utilizar loops (for/while), sino con slicing.

def es_palindromo(palabra: str) -> bool:
    return palabra == palabra[::-1]

# NO MODIFICAR
assert es_palindromo("amor") == False
assert es_palindromo("radar") == True
assert es_palindromo("") == True