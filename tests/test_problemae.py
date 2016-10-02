# -*- coding: utf-8 -*-

from __future__ import absolute_import

from tap.problemae.solucion import puede_hallar_secuencia


class TestProblemaE:
    def test_puede_hallar_secuencia(self):
        assert puede_hallar_secuencia(
            [(3, 2), (3, 1), (2, 1)]
        ) == 'S'

        assert puede_hallar_secuencia(
            [(2, 2), (3, 3), (1, 1)]
        ) == 'N'

        assert puede_hallar_secuencia(
            [(2, 3), (2, 1), (3, 1)]
        ) == 'S'

        assert puede_hallar_secuencia(
            [(2, 3), (3, 1), (1, 1)]
        ) == 'S'

        assert puede_hallar_secuencia(
            [(2, 3), (3, 1), (1, 2)]
        ) == 'N'

        assert puede_hallar_secuencia(
            [(2, 3, 1), (3, 1, 2), (2, 1, 3)]
        ) == 'S'
