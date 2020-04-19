# Implementar la función es_primo(numero), que devuelva un booleano en base a
# si numero es primo o no.


def es_primo(numero: int) -> bool:
    if numero <= 1:
         return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True

# NO MODIFICAR
assert es_primo(2) == True
assert es_primo(6) == False
assert es_primo(100) == False
assert es_primo(1) == False
