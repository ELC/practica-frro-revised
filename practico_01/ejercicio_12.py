# Implementar una funcion tiene_pares que tome una lista y devuelva True si
# tiene pares y False si no tiene


from typing import Iterable


def tiene_pares(numeros: Iterable[int]) -> bool:
    for numero in numeros:
        if numero % 2 == 0:
            return True
    return False


# NO MODIFICAR
assert tiene_pares([1, 3, 5]) is False
assert tiene_pares([1, 3, 5, 6]) is True
assert tiene_pares([1, 3, 5, 600]) is True


# Re-Escribir utilizando for-else con dos return y un break
# Referencia:
# https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops


def tiene_pares(numeros: Iterable[int]) -> bool:
    for numero in numeros:
        if numero % 2 == 0:
            break
    else:
        return False

    return True


# NO MODIFICAR
assert tiene_pares([1, 3, 5]) is False
assert tiene_pares([1, 3, 5, 6]) is True
assert tiene_pares([1, 3, 5, 600]) is True

# Re-Escribir utilizando any, sin utilizar bucles
# Referencia:
# https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops


def tiene_pares(numeros: Iterable[int]) -> bool:
    return any(numero % 2 == 0 for numero in numeros)


# NO MODIFICAR
assert tiene_pares([1, 3, 5]) is False
assert tiene_pares([1, 3, 5, 6]) is True
assert tiene_pares([1, 3, 5, 600]) is True
