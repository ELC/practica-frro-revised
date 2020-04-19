# Python permite funciones de orden superior, es decir, funciones que toman
# otras funciones como parámetros. Esto posibilita una serie de patrones que
# en otros lenguajes son difíciles de implementar y hace sencilla la
# implementación de patrones como el decorador.


# Caso de uso 1: Medir el tiempo de las funciones

# En Python existe la función perf_counter del módulo time de la biblioteca
# estandar que permite medir el tiempo con cierta precisión entre invocaciones

# Para poder utilizar un ejemplo real, se utilizará una función que calcula
# y cuenta las permutaciones (una operación costosa computacionalmente)

from itertools import permutations
from time import perf_counter
from typing import Callable, Sequence, Tuple


# NO MODIFICAR
def calcular_posibilidades(lista: Sequence[int], limite: int) -> int:
    count = 0
    for i in range(limite):
        for _ in permutations(lista, i):
            count += 1
    return count


# NO MODIFICAR
n = 11
limite = 10
lista = list(range(n))
start = perf_counter()
result = calcular_posibilidades(lista, limite)
elapsed = perf_counter() - start
print(f"Tiempo: {elapsed:2.2f} segundos - Enfoque procedural")
assert result == 28671512


# Escribir una función que tome como parámetro una función y devuelva una dupla
# conteniendo en su primer elemento el resultado de la función original  en su
# segundo elemento el tiempo de ejecución.

# La función no debe tomar parámetros y por lo tanto se recomienda usar el ya
# aprendido partial

from functools import partial


def medir_tiempo(func: Callable[[], int]) -> Tuple[int, float]:
    start = perf_counter()
    result = func()
    elapsed = perf_counter() - start
    return result, elapsed


# NO MODIFICAR
result, elapsed = medir_tiempo(partial(calcular_posibilidades, lista, limite))
print(f"Tiempo: {elapsed:2.2f} segundos - Usando Partial")
assert result == 28671512


# Re-Escribir la función utilizando closures de forma tal que la función no
# se requiera utilizar partial. En este caso se debe devolver una función que
# devuelva la tupla y tome una cantidad arbitraria de parámetros


def medir_tiempo(
    func: Callable[[Sequence[int], int], int]
) -> Callable[[Sequence[int], int], Tuple[int, float]]:
    def helper(*args, **kwargs) -> Tuple[int, float]:
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start
        return result, elapsed

    return helper


# NO MODIFICAR
calcular_posibilidades_nueva = medir_tiempo(calcular_posibilidades)
result, elapsed = calcular_posibilidades_nueva(lista, limite)
print(f"Tiempo: {elapsed:2.2f} segundos - Decorador")
assert result == 28671512


# La función anterior cumple con las condiciones necesarias para ser utilizada
# como decorador en Python. Utilizar la sintaxis especial de decoradores (el @)
# y re-definir la función calcular_posibilidades con esta nueva sintaxis.
# Referencia: https://docs.python.org/3/glossary.html#term-decorator


@medir_tiempo
def calcular_posibilidades(lista: Sequence[int], limite: int) -> int:
    count = 0
    for i in range(limite):
        for _ in permutations(lista, i):
            count += 1
    return count


# NO MODIFICAR
result, elapsed = calcular_posibilidades(lista, limite)
print(f"Tiempo: {elapsed:2.2f} segundos - Decorador con sintaxis especial")
assert result == 28671512


# Una caso real de este patrón es para guardar en una memoria cache auxiliar
# resultados de funciones que son muy costosas computacionalmente. A este
# patrón se lo suele denominar memoized

# Escribir una función memoized y utilizarla como decorador junto con medir_
# tiempo para la función calcular posibilidades. Prestar atención a los tiempo
# de ejecución


def memoized(func):
    memo = {}

    def helper(*args):
        if str(args) not in memo:
            memo[str(args)] = func(*args)
        return memo[str(args)]

    return helper


@medir_tiempo
@memoized
def calcular_posibilidades(lista: Sequence[int], limite: int) -> int:
    count = 0
    for i in range(limite):
        for _ in permutations(lista, i):
            count += 1
    return count


# NO MODIFICAR
print()

result, elapsed = calcular_posibilidades(lista, limite)
print(f"Tiempo: {elapsed:2.2f} segundos - Con Memoized - 1ra ejecución")
assert result == 28671512

result, elapsed = calcular_posibilidades(lista, limite)
print(f"Tiempo: {elapsed:2.8f} segundos - Con Memoized - 2da ejecución")
assert result == 28671512

result, elapsed = calcular_posibilidades(lista, limite)
print(f"Tiempo: {elapsed:2.8f} segundos - Con Memoized - 3ra ejecución")
assert result == 28671512


# CHALLENGE OPCIONAL: Esta es otra ocasión donde las funciones recursivas
# tienen ventajas adicionales # ya que al utilizar el patrón memoized, las
# funciones recursivas permiten ejecuciones más rápidas para las llamadas
# sucesivas.


# Escribir una versión recursiva de calcular_posibilidades que utilice la misma
# firma y devuelva también la cantidad de permutaciones


@medir_tiempo
@memoized
def calcular_posibilidades_recursiva(lista: Sequence[int], limite: int) -> int:
    if limite == 0:
        return 0

    count = sum(1 for _ in permutations(lista, limite - 1))

    return count + calcular_posibilidades_recursiva(lista, limite - 1)[0]


# NO MODIFICAR
print()

result, elapsed = calcular_posibilidades_recursiva(lista, limite)
print(f"Tiempo: {elapsed:2.2f} segundos - Recursiva Memoized - 1ra Ejecución")
assert result == 28671512

result, elapsed = calcular_posibilidades_recursiva(lista, limite)
print(f"Tiempo: {elapsed:2.8f} segundos - Recursiva Memoized - 2da Ejecución")
assert result == 28671512

print()

result, elapsed = calcular_posibilidades(lista, limite + 1)
print(f"Tiempo: {elapsed:2.2f} segundos - Bucles Memoized - Parametro + 1")
assert result == 68588312

result, elapsed = calcular_posibilidades_recursiva(lista, limite + 1)
print(f"Tiempo: {elapsed:2.8f} segundos - Recursiva Memoized - Parametro + 1")
assert result == 68588312

print()

result, elapsed = calcular_posibilidades(lista, limite + 2)
print(f"Tiempo: {elapsed:2.2f} segundos - Bucles Memoized - Parametro + 2")
assert result == 108505112

result, elapsed = calcular_posibilidades_recursiva(lista, limite + 2)
print(f"Tiempo: {elapsed:2.8f} segundos - Recursiva Memoized - Parametro + 2")
assert result == 108505112

print()

result, elapsed = calcular_posibilidades(lista, limite - 1)
print(f"Tiempo: {elapsed:2.2f} segundos - Bucles Memoized - Parametro - 1")
assert result == 8713112

result, elapsed = calcular_posibilidades_recursiva(lista, limite - 1)
print(f"Tiempo: {elapsed:2.8f} segundos - Recursiva Memoized - Parametro - 1")
assert result == 8713112

print()

result, elapsed = calcular_posibilidades(lista, limite - 2)
print(f"Tiempo: {elapsed:2.2f} segundos - Bucles Memoized - Parametro - 2")
assert result == 2060312

result, elapsed = calcular_posibilidades_recursiva(lista, limite - 2)
print(f"Tiempo: {elapsed:2.8f} segundos - Recursiva Memoized - Parametro - 2")
assert result == 2060312
