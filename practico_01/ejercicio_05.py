# Implementar la función multiplicar() que devuelva el producto de todos
# los números de una lista. Si la lista está vacia debe devolver 0.
# NO SE DEBEN UTILIZAR BILIOTECAS AUXILIARES (Numpy, math, pandas)

from typing import Iterable


def multiplicar(numeros: Iterable[float]) -> float:
    if not numeros:
        return 0

    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado


# NO MODIFICAR
assert multiplicar([1, 2, 3, 4]) == 24
assert multiplicar([2, 5]) == 10
assert multiplicar([]) == 0
assert multiplicar([1, 2, 3, 0, 4, 5]) == 0
assert multiplicar(range(1, 20)) == 121_645_100_408_832_000


# CHALLENGE OPCIONAL: Implementar utilizando reduce
# Referencia:
# https://docs.python.org/3/reference/expressions.html#membership-test-operations

from functools import reduce


def multiplicar(numeros: Iterable[float]) -> float:
    if not numeros:
        return 0

    return reduce(lambda x, y: x * y, numeros)


# NO MODIFICAR
assert multiplicar([1, 2, 3, 4]) == 24
assert multiplicar([2, 5]) == 10
assert multiplicar([]) == 0
assert multiplicar([1, 2, 3, 0, 4, 5]) == 0
assert multiplicar(range(1, 20)) == 121_645_100_408_832_000
