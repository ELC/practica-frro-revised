# Implementar la función operacion, donde:
# - Si multiplicar es True: devolver la multiplicación entre a y b.
# - Si multiplicar es False: devolver la division entre a y b.
# - Si multiplicar es False y b es cero: devolver "Operación no válida".

from typing import Union


# Escribir utilizando un sólo return - No utilizar ANDs ni ORs

def operacion(a: float, b: float, multiplicar: bool) -> Union[float, str]:
    return a * b if multiplicar else 'Operación no válida' if b == 0 else a / b

# NO MODIFICAR
assert operacion(1, 1, True) == 1
assert operacion(1, 1, False) == 1
assert operacion(25, 5, True) == 125
assert operacion(25, 5, False) == 5
assert operacion(0, 5, True) == 0
assert operacion(0, 5, False) == 0
assert operacion(1, 0, True) == 0
assert operacion(1, 0, False) == "Operación no válida"


# Re-Escribir utilizando múltiples return

def operacion(a: float, b: float, multiplicar: bool) -> Union[float, str]:
    if multiplicar:
        return a * b
    if b == 0:
        return "Operación no válida"
    return a / b


# NO MODIFICAR
assert operacion(1, 1, True) == 1
assert operacion(1, 1, False) == 1
assert operacion(25, 5, True) == 125
assert operacion(25, 5, False) == 5
assert operacion(0, 5, True) == 0
assert operacion(0, 5, False) == 0
assert operacion(1, 0, True) == 0
assert operacion(1, 0, False) == "Operación no válida"
