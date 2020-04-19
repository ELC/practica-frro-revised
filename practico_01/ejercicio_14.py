# Se tiene un programa que lee diferentes listas de una tabla en una base de
# datos y se quieren combinar estas listas para que luego puedan crearse
# los objetos de la capa de negocio.

# Implementar una función combinar que tome estas listas y devuelva una tupla
# de tuplas con los componentes correspondientes.

from typing import Any, List, Tuple

nombre_articulos = ["ventana", "lámpara", "shampoo"]
precio_articulos = [100.48, 16.42, 5.20]


# Resolver utilizando un bucle for


def combinar(nombres: List[str], precios: List[float]) -> Tuple[Any]:
    articulos = []

    for i in range(len(nombres)):
        articulo = (nombres[i], precios[i])
        articulos.append(articulo)

    return tuple(articulos)


# NO MODIFICAR
respuesta = (
    ("ventana", 100.48),
    ("lámpara", 16.42),
    ("shampoo", 5.2),
)

assert combinar(nombre_articulos, precio_articulos) == respuesta


# Re-Escribir utilizando enumerate y agregando un nuevo componente
# Referencia: https://docs.python.org/3/library/functions.html#enumerate

id_articulos = [6852, 1459, 3578]


def combinar(nombres: List[str], precios: List[float], ids: List[int]) -> Tuple[Any]:
    articulos = []

    for i, nombre in enumerate(nombres):
        articulo = (nombre, precios[i], ids[i])
        articulos.append(articulo)

    return tuple(articulos)


# NO MODIFICAR
respuesta = (
    ("ventana", 100.48, 6852),
    ("lámpara", 16.42, 1459),
    ("shampoo", 5.2, 3578),
)

assert combinar(nombre_articulos, precio_articulos, id_articulos) == respuesta


# Re-Escribir utilizando zip
# Referencia: https://docs.python.org/3/library/functions.html#zip

id_articulos = [6852, 1459, 3578]


def combinar(nombres: List[str], precios: List[float], ids: List[int]) -> Tuple[Any]:
    articulos = []

    for nombre, precio, id_ in zip(nombres, precios, ids):
        articulo = (nombre, precio, id_)
        articulos.append(articulo)

    return tuple(articulos)


# NO MODIFICAR
respuesta = (
    ("ventana", 100.48, 6852),
    ("lámpara", 16.42, 1459),
    ("shampoo", 5.2, 3578),
)

assert combinar(nombre_articulos, precio_articulos, id_articulos) == respuesta


# Re-Escribir utilizando zip y una cantidad arbitraria de componentes
# Referencia:
# https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists

id_articulos = [6852, 1459, 3578]
categoria_articulos = ["hogar", "libreria", "perfumeria"]
importado_articulos = [True, False, True]


def combinar(*args) -> Tuple[Any]:
    articulos = []

    for articulo in zip(*args):
        articulos.append(articulo)

    return tuple(articulos)


# NO MODIFICAR
respuesta = (
    ("ventana", 100.48, 6852, "hogar", True),
    ("lámpara", 16.42, 1459, "libreria", False),
    ("shampoo", 5.2, 3578, "perfumeria", True),
)

componentes = [
    nombre_articulos,
    precio_articulos,
    id_articulos,
    categoria_articulos,
    importado_articulos,
]

assert combinar(*componentes) == respuesta
