# -*- coding: utf-8 -*-

from __future__ import absolute_import

from tap.problemak.solucion import diferencia_hojas


class TestProblemaK:
    def test_diferencia_de_hojas(self):
        assert diferencia_hojas(
            [
                (2, 1, 2),
                (5, 3),
                (1, 2)
            ]
        ) == 2

        assert diferencia_hojas(
            [
                (6, 2, 3),
                (1, 6, 4, 3, 2, 2),
                (1, 2),
                (2, 3),
                (3, 4),
                (3, 5),
                (5, 6)
            ]
        ) == -1
