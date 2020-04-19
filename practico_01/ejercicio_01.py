# Implementar una función maximo() que tome como argumento dos números 
# y devuelva el mayor de ellos.


def maximo(a: float, b: float) -> float:
    if a > b:
        return a
    return b

# NO MODIFICAR
assert maximo(10, 5) == 10
assert maximo(9, 18) == 18


# Re-escribir la función utilizando el built-in max
# Referencia: https://docs.python.org/3/library/functions.html#max

def maximo(a: float, b: float) -> float:
    return max(a, b)

# NO MODIFICAR
assert maximo(10, 5) == 10
assert maximo(9, 18) == 18


# CHALLENGE OPCIONAL: Re-escribir la función utilizando el operador ternario
# Referencia: https://docs.python.org/3/reference/expressions.html#conditional-expressions

def maximo(a: float, b: float) -> float:
    return a if a > b else b

# NO MODIFICAR
assert maximo(10, 5) == 10
assert maximo(9, 18) == 18
