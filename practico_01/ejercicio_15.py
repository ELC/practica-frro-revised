# Esta guia muestra uno de los patrones avanzados de programación para evitar
# el uso de variables globales. El método descripto se llama closure y consiste
# en vincular una función con datos que persistan luego de la ejecución, sin
# recurrir a variables globales. Esto se hace mediante la declaración de una
# función dentro de otra y permite comportamiento que sería imposible lograr de
# otra manera

# Implementar una función generar_pares que devuelva una función que cada vez
# que sea invocada devuelva el número par siguiente al devuelto la última vez
# que fue invocada. Hint: Se deben usar closures y el modificador nonlocal

from typing import Iterator, Callable


def generar_pares(initial: int= 0) -> Callable[[], int]:
    next_number = initial - 2

    def helper():
        nonlocal next_number 
        next_number += 2
        return next_number

    return helper

# NO MODIFICAR
generador_pares = generar_pares(0)
assert generador_pares() == 0
assert generador_pares() == 2
assert generador_pares() == 4


# Este tipo de comportamiento puede escrbirse como una co-rutina (cuando se 
# cumplen ciertas condiciones), las co-rutinas en Python son llamadas funciones
# generadoras y se caracterizan por utilizar el yield en lugar del return.
# Referencia: https://docs.python.org/3/howto/functional.html?highlight=generator#generators


# Re-Escribir utilizando Generadores

def generar_pares(initial: int=0) -> Iterator[int]:
    last_number = initial
    yield last_number

    while True:
        last_number += 2
        yield last_number

# NO MODIFICAR
generador_pares = generar_pares()
assert next(generador_pares) == 0
assert next(generador_pares) == 2
assert next(generador_pares) == 4

# CHALLENGE OPCIONAL: Re-Escribir utilizando send para saltear numeros

def generar_pares(initial: int=0) -> Iterator[int]:
    last_number = initial
    yield last_number

    while True:
        last_number += 2
        aux = yield last_number
        if aux:
            last_number = aux - 2

# NO MODIFICAR
generador_pares = generar_pares()
assert next(generador_pares) == 0
assert next(generador_pares) == 2
assert next(generador_pares) == 4
assert generador_pares.send(10) == 10
assert next(generador_pares) == 12
assert next(generador_pares) == 14
assert next(generador_pares) == 16

# CHALLENGE OPCIONAL: Re-Escribir utilizando Generadores delegados (yield from)

def generar_pares_delegados(initial: int=0) -> Iterator[int]:
    yield from generar_pares(0)

# NO MODIFICAR
generador_pares = generar_pares()
assert next(generador_pares) == 0
assert next(generador_pares) == 2
assert next(generador_pares) == 4
assert generador_pares.send(10) == 10
assert next(generador_pares) == 12
assert next(generador_pares) == 14
assert next(generador_pares) == 16
