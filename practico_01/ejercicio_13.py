# PARTE 1
# Escribir una función que tome una lista de números, los eleve al cubo,
# y devuelva la suma de los elementos pares

from typing import Iterable

# Escribir utilizando dos bucles for, uno para elevar al cubo y otro para
# separar los pares


def suma_cubo_pares(numeros: Iterable[int]) -> int:
    cubos = []
    for numero in numeros:
        cubos.append(numero ** 3)

    suma_pares = 0
    for numero in cubos:
        if numero % 2 == 0:
            suma_pares += numero

    return suma_pares


# NO MODIFICAR
assert suma_cubo_pares([1, 2, 3, 4, 5, 6]) == 288


# Re-Escribir utilizando comprension de listas (debe resolverse en 1 línea)
# y la función built-in sum

# Referencia:
# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

# Referencia: https://docs.python.org/3/library/functions.html#sum


def suma_cubo_pares(numeros: Iterable[int]) -> int:
    return sum([numero ** 3 for numero in numeros if numero ** 3 % 2 == 0])


# NO MODIFICAR
assert suma_cubo_pares([1, 2, 3, 4, 5, 6]) == 288


# Re-Escribir utilizando expresiones generadoras (debe resolverse en 1 línea)
# y la función built-in sum. Nota: Sólo deberían cambiarse 2 caracteres de la
# solución anterior
# Referencia:
# https://docs.python.org/3/reference/expressions.html#generator-expressions


def suma_cubo_pares(numeros: Iterable[int]) -> int:
    return sum(numero ** 3 for numero in numeros if numero ** 3 % 2 == 0)


# NO MODIFICAR
assert suma_cubo_pares([1, 2, 3, 4, 5, 6]) == 288


# PARTE 2
# A continuación se introduce el concepto de Lambdas (Funciones anónimas),
# Escribir las funciones lambdas que corresponda en cada línea
# Referencia: https://docs.python.org/3/reference/expressions.html#lambda

numeros = [1, 2, 3, 4, 5, 6]


# Escribir una función lambda que eleve los elementos al cubo

numeros_al_cubo = list(map(lambda x: x ** 3, numeros))


# Escribir una función lambda que permita filtrar todos los elementos pares

numeros_al_cubo_pares = list(filter(lambda x: x % 2 == 0, numeros_al_cubo))


# Escribir una función Lambda que sume todos los elementos

from functools import reduce

suma_numeros_al_cubo_pares = reduce(lambda x, y: x + y, numeros_al_cubo_pares)


# Escribir una función Lambda que permita ordenar los elementos de la numeros
# en base a si son pares o impares

numeros_ordenada = sorted(numeros, key=lambda x: x % 2 == 0)

# NO MODIFICAR
assert numeros_al_cubo == [1, 8, 27, 64, 125, 216]
assert numeros_al_cubo_pares == [8, 64, 216]
assert suma_numeros_al_cubo_pares == 288
assert numeros_ordenada == [1, 3, 5, 2, 4, 6]
