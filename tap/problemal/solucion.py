# -*- coding: utf-8 -*-

import collections
import itertools

Arbol = collections.namedtuple('Arbol', 'raiz')
Nodo = collections.namedtuple('Nodo', 'diametro tira_izq tira_der')


def puede_colocar_tira(info_tiras):
    diametro_mayor, _ = info_tiras[0]
    tira_luces = info_tiras[1:]
    arbol = crear_arbol_pelotitas(4)
    print(dump_tree(arbol))


def crear_arbol_pelotitas(diametro):
    nodo_raiz = next(crear_arbol_nodos(diametro))
    return Arbol(nodo_raiz)


def crear_arbol_nodos(diametro):
    nodo_izq = None
    nodo_der = None
    if diametro >= 3:
        nodo_izq = next(crear_arbol_nodos(diametro - 1))
        nodo_der = next(crear_arbol_nodos(diametro - 2))
    nodo_raiz = Nodo(diametro, nodo_izq, nodo_der)
    yield nodo_raiz


def dump_tree(arbol):
    dumpster = []

    if isinstance(arbol, Arbol):
        dumpster.append(dump_tree(arbol.raiz.tira_izq))
        dumpster.append(arbol.raiz.diametro)
        dumpster.append(dump_tree(arbol.raiz.tira_der))
    elif isinstance(arbol, Nodo):
        if arbol.tira_izq is not None:
            dumpster.append(arbol.tira_izq.diametro)

        dumpster.append(arbol.diametro)

        if arbol.tira_der is not None:
            dumpster.append(arbol.tira_der.diametro)
    return dumpster
