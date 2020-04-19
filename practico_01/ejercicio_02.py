# Implementar la función maximo, que reciba tres números y devuelva el maximo
# de ellos. Usar función built-in max

# Escribir utilizando tres  IFs y comparaciones encadenadas
# Referencia: https://docs.python.org/3/reference/expressions.html#comparisons


def maximo(a: float, b: float, c: float) -> float:
    if b < a > c:
        return a
    if a < b > c:
        return b
    if a < c > b:
        return c

    raise Exception


# NO MODIFICAR
assert maximo(1, 10, 5) == 10
assert maximo(4, 9, 18) == 18
assert maximo(24, 9, 18) == 24


# Modificar la función para que tome 4 parámetros en lugar de 3, utilizar el
# built-in max


def maximo(a: float, b: float, c: float, d: float) -> float:
    return max(a, b, c, d)


# NO MODIFICAR
assert maximo(1, 10, 5, -5) == 10
assert maximo(4, 9, 18, 6) == 18
assert maximo(24, 9, 18, 20) == 24
assert maximo(24, 9, 18, 30) == 30


# Modificar la función para que tome una cantidad arbitraria de parámetros
# Referencia:
# https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists


def maximo(*args) -> float:
    return max(args)


# NO MODIFICAR
assert maximo(1, 10, 5, -5) == 10
assert maximo(4, 9, 18, 6) == 18
assert maximo(24, 9, 18, 20) == 24
assert maximo(24, 9, 18, 30) == 30


# CHALLENGE OPCIONAL: Re-Escribir la función de forma tal que tome una cantidad
# arbitraria de parámetros y que sea recursiva


def maximo(*args) -> float:
    primero, *resto = args

    if resto == []:
        return primero

    return max(primero, maximo(*resto))


# NO MODIFICAR
assert maximo(1, 10, 5, -5) == 10
assert maximo(4, 9, 18, 6) == 18
assert maximo(24, 9, 18, 20) == 24
assert maximo(24, 9, 18, 30) == 30
