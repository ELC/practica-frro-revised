# Implementar la función es_primo(numero), que devuelva un booleano en base a
# si numero es primo o no.


def es_primo(numero: int) -> bool:
    if numero <= 1:
         return False

    return all(numero % i != 0 for i in range(2, numero))

# NO MODIFICAR
assert es_primo(2) == True
assert es_primo(6) == False
assert es_primo(100) == False
assert es_primo(1) == False
