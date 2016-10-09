# -*- coding: utf-8 -*-

import collections

Nodo = collections.namedtuple('Nodo', 'diametro nodo_izq nodo_der')


def puede_colocar_tira(info_tiras):
    diametro_mayor, _ = info_tiras[0]
    arbol_pelotitas = crear_arbol_pelotas(diametro_mayor)
    arbol_luces = crear_arbol_luces(info_tiras[1])
    puede_colocar = contiene_arbol(arbol_pelotitas, arbol_luces)
    return 'S' if puede_colocar else 'N'


def crear_arbol_pelotas(diametro):
    gen_arbol_nodos = gen_crear_arbol_pelotas(diametro)
    return next(gen_arbol_nodos)


def gen_crear_arbol_pelotas(diametro):
    nodo_izq = None
    nodo_der = None
    if diametro >= 3:
        nodo_izq = next(gen_crear_arbol_pelotas(diametro - 1))
        nodo_der = next(gen_crear_arbol_pelotas(diametro - 2))
    yield Nodo(diametro, nodo_izq, nodo_der)


def crear_arbol_luces(tira):
    if not tira:
        return None

    nodo_raiz = max(tira)
    nodo_izq = None
    nodo_der = None

    max_index = tira.index(nodo_raiz)
    part_izq = tira[:max_index]
    part_der = tira[max_index + 1:]

    if part_izq and part_der:
        calc_izq = crear_arbol_luces(part_izq)
        calc_der = crear_arbol_luces(part_der)
        if part_izq[-1] > part_der[0]:
            nodo_izq, nodo_der = calc_izq, calc_der
        else:
            nodo_izq, nodo_der = calc_der, calc_izq
    elif part_izq:
        nodo = crear_arbol_luces(part_izq)
        if nodo_raiz - 1 == part_izq[-1]:
            nodo_izq = nodo
        else:
            nodo_der = nodo
    elif part_der:
        nodo = crear_arbol_luces(part_der)
        if nodo_raiz - 2 == part_der[0]:
            nodo_der = nodo
        else:
            nodo_izq = nodo

    return Nodo(nodo_raiz, nodo_izq, nodo_der)


def contiene_arbol(nodo_pelota, nodo_luz):
    if nodo_luz is None:
        return True
    return subarbol(nodo_pelota, nodo_luz)


def subarbol(nodo_pelota, nodo_luz):
    if nodo_pelota is None:
        return False
    elif (nodo_pelota.diametro == nodo_luz.diametro and
          matchtree(nodo_pelota, nodo_luz)):
        return True

    return (subarbol(nodo_pelota.nodo_izq, nodo_luz) or
            subarbol(nodo_pelota.nodo_der, nodo_luz))


def matchtree(nodo_pelota, nodo_luz):
    if nodo_pelota is None and nodo_luz is None:
        return True
    elif nodo_pelota is None or nodo_luz is None:
        return True
    elif nodo_pelota.diametro != nodo_luz.diametro:
        return False
    else:
        return (matchtree(nodo_pelota.nodo_izq, nodo_luz.nodo_izq) and
                matchtree(nodo_pelota.nodo_der, nodo_luz.nodo_der))
