# Implementar la función sumatoria(N) que Determine la suma de todos los 
# numeros de 1 a N.


# Escribir utilizando un bucle for

def sumatoria(n: int) -> int:
    return sum(range(n + 1))

# NO MODIFICAR
assert sumatoria(1) == 1
assert sumatoria(100) == 5050


# CHALLENGE OPCIONAL: Re-escribir utilizando reduce

from functools import reduce

def sumatoria(n: int) -> int:
    return reduce(lambda x, y: x + y, range(n + 1), 0)

# NO MODIFICAR
assert sumatoria(1) == 1
assert sumatoria(100) == 5050


# CHALLENGE OPCIONAL: Re-Escribir utilizando suma de Gauss
# Referencia: https://es.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF

def sumatoria(n: int) -> int:
    return n * (n + 1) // 2

# NO MODIFICAR
assert sumatoria(1) == 1
assert sumatoria(100) == 5050
