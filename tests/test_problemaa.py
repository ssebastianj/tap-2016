# -*- coding: utf-8 -*-

from __future__ import absolute_import

from tap.problemaa.solucion import puede_empacar


class TestProblemaA(object):
    def test_puede_empacar(self):
        assert puede_empacar('remera') == 'S'
        assert puede_empacar('camisa') == 'N'
        assert puede_empacar('buey') == 'S'
        assert puede_empacar('i') == 'N'
        assert puede_empacar('abuelo') == 'S'
        assert puede_empacar('estenoporquetienelai') == 'N'