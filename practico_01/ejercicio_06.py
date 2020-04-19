# Implementar la función numeros_al_final(), que mueve todos los 
# elementos numéricos de lista al final de esta. Devuelve la lista.

from typing import Iterable, Union


def numeros_al_final(lista: Iterable[Union[float, str]]) -> Iterable[Union[float, str]]:
    numeros = [elem for elem in lista if type(elem) in [int, float]]
    letras = [elem for elem in lista if type(elem) == str]
    return letras + numeros

# NO MODIFICAR
assert numeros_al_final([3, 'a', 1, 'b', 10, 'j']) == ['a', 'b', 'j', 3, 1, 10]


# CHALLENGE OPCIONAL 2: Resolver utilizando sorted con una custom key
# Referencia: https://docs.python.org/3/library/functions.html#sorted

def numeros_al_final(lista: Iterable[Union[float, str]]) -> Iterable[Union[float, str]]:
    return sorted(lista, key=lambda x: type(x) != str)

# NO MODIFICAR
assert numeros_al_final([3, 'a', 1, 'b', 10, 'j']) == ['a', 'b', 'j', 3, 1, 10]