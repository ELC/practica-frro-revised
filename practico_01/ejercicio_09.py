# Implementar las funciones superposicion_x(), que tomen dos listas y 
# devuelva un booleano en base a si tienen al menos 1 elemento en común.

from typing import Any, Iterable


# Implementar utilizando bucles anidados.

def superposicion(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    for elem in lista_1:
        for elem_ in lista_2:
            if elem == elem_:
                return True
    return False

# NO MODIFICAR
test_list = [1, "hello", 35.20]
assert superposicion(test_list, (2, "world", 35.20)) == True
assert superposicion(test_list, (2, "world", 30.85)) == False


# Re-Escribir utilizando un sólo bucle y el operador in

def superposicion(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    return any(elem in lista_2 for elem in lista_1)

# NO MODIFICAR
test_list = [1, "hello", 35.20]
assert superposicion(test_list, (2, "world", 35.20)) == True
assert superposicion(test_list, (2, "world", 30.85)) == False


# Re-Escribir utilizando sin bucles, el operador in y la funcion built-in any
# Referencia: https://docs.python.org/3/library/functions.html#any

def superposicion(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    return any(elem in lista_2 for elem in lista_1)

# NO MODIFICAR
test_list = [1, "hello", 35.20]
assert superposicion(test_list, (2, "world", 35.20)) == True
assert superposicion(test_list, (2, "world", 30.85)) == False


# Re-Escribir utilizando conjuntos (sets)
# Referencia: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset

def superposicion(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    return len(set(lista_1) & set(lista_2)) != 0

# NO MODIFICAR
test_list = [1, "hello", 35.20]
assert superposicion(test_list, (2, "world", 35.20)) == True
assert superposicion(test_list, (2, "world", 30.85)) == False
