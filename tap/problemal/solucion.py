# -*- coding: utf-8 -*-

import collections

Nodo = collections.namedtuple('Nodo', 'diametro tira_izq tira_der')


def puede_colocar_tira(info_tiras):
    diametro_mayor, _ = info_tiras[0]
    tira_luces = info_tiras[1:]
    arbol_pelotitas = crear_arbol_nodos(diametro_mayor)
    return 'S'


def crear_arbol_nodos(diametro):
    gen_arbol_nodos = gen_crear_arbol_nodos(diametro)
    return next(gen_arbol_nodos, Nodo(diametro, None, None))


def gen_crear_arbol_nodos(diametro):
    nodo_izq = None
    nodo_der = None
    if diametro >= 3:
        nodo_izq = next(gen_crear_arbol_nodos(diametro - 1))
        nodo_der = next(gen_crear_arbol_nodos(diametro - 2))
    yield Nodo(diametro, nodo_izq, nodo_der)


def dumps_tree(nodo):
    dumpster = []
    if nodo.tira_izq is not None:
        dumpster.append(dumps_tree(nodo.tira_izq))

    dumpster.append(nodo.diametro)

    if nodo.tira_der is not None:
        dumpster.append(dumps_tree(nodo.tira_der))
    return tuple(dumpster)
