# -*- coding: utf-8 -*-

from __future__ import absolute_import

from tap.problemaf.solucion import cantidad_veces


class TestProblemaF(object):
    def test_cantidad_de_veces_dr(self):
        assert cantidad_veces(
            [
                'RAMIRO',
                'AUGUSTO',
                'JOAQUIN',
                'JACINTO',
                'NICOLAS',
                'ALEJANDRO',
                'DIJKSTRA',
                'KAJITA',
                'MCDONALD',
                'SCHRODINGER'
            ]
        ) == 4

        assert cantidad_veces(
            [
                'MELANIE',
                'DAMIAN',
                'RAMIRO',
                'AUGUSTO',
                'JOAQUIN',
                'JACINTO',
                'NICOLAS',
                'ALEJANDRO',
                'DIJKSTRA',
                'KAJITA',
                'MCDONALD',
                'SCHRODINGER'
            ]
        ) == 5

        assert cantidad_veces(
            [
                'DDD',
                'RRR',
                'DRDR',
                'RDRD'
            ]
        ) == 5

        assert cantidad_veces(
            [
                'ABCEFG',
                'HIJKLM',
                'NOPQST',
                'UVWXYZ'
            ]
        ) == 0