# -*- coding: utf-8 -*-

from __future__ import absolute_import

from tap.problemal.solucion import (
    crear_arbol_pelotas,
    crear_arbol_luces,
    puede_colocar_tira
)


class TestProblemaL(object):
    def test_crear_arbol_pelotitas_diametro_4(self):
        nodo_raiz = crear_arbol_pelotas(4)
        assert nodo_raiz.diametro == 4

        nodo_izq_1 = nodo_raiz.nodo_izq
        nodo_der_1 = nodo_raiz.nodo_der
        assert nodo_izq_1.diametro == 3
        assert nodo_der_1.diametro == 2

        nodo_izq_2 = nodo_izq_1.nodo_izq
        nodo_der_2 = nodo_izq_1.nodo_der
        assert nodo_izq_2.diametro == 2
        assert nodo_der_2.diametro == 1

    def test_crear_arbol_luces_1(self):
        tira_luces = (1, 3, 4, 2)

        nodo_raiz = crear_arbol_luces(tira_luces)
        assert nodo_raiz.diametro == 4

        nodo_izq_1 = nodo_raiz.nodo_izq
        nodo_der_1 = nodo_raiz.nodo_der
        assert nodo_izq_1.diametro == 3
        assert nodo_der_1.diametro == 2

        nodo_der_2 = nodo_izq_1.nodo_der
        assert nodo_der_2.diametro == 1

    def test_crear_arbol_luces_2(self):
        tira_luces = (5,)

        nodo_raiz = crear_arbol_luces(tira_luces)
        assert nodo_raiz.diametro == 5
        assert nodo_raiz.nodo_izq is None
        assert nodo_raiz.nodo_der is None

    def test_crear_arbol_luces_3(self):
        tira_luces = (3, 5)

        nodo_raiz = crear_arbol_luces(tira_luces)
        assert nodo_raiz.diametro == 5

        nodo_der = nodo_raiz.nodo_der
        assert nodo_der.diametro == 3

    def test_crear_arbol_luces_4(self):
        tira_luces = (5, 4)

        nodo_raiz = crear_arbol_luces(tira_luces)
        assert nodo_raiz.diametro == 5

        nodo_izq = nodo_raiz.nodo_izq
        assert nodo_izq.diametro == 4

    def test_puede_colocar_tira(self):
        assert puede_colocar_tira(
            [(3, 0), tuple()]
        ) == 'S'

        assert puede_colocar_tira(
            [(3, 2), (2, 3)]
        ) == 'S'

        assert puede_colocar_tira(
            [(4, 4), (1, 3, 4, 2)]
        ) == 'S'

        assert puede_colocar_tira(
            [(5, 2), (3, 5)]
        ) == 'S'

        assert puede_colocar_tira(
            [(4, 2), (4, 1)]
        ) == 'N'

        assert puede_colocar_tira(
            [(6, 3), (2, 3, 2)]
        ) == 'N'

        assert puede_colocar_tira(
            [(8, 4), (2, 3, 3, 1)]
        ) == 'N'

        assert puede_colocar_tira(
            [(10, 10), (2, 3, 4, 5, 6, 8, 7, 5, 3, 1)]
        ) == 'S'
