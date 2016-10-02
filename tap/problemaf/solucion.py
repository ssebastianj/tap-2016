# -*- coding: utf-8 -*-

import itertools


def cantidad_veces(firmantes):
    total_drs = 0
    stack_d = 0
    found_r = False

    for letra in itertools.chain(*firmantes):
        if letra == 'D':
            stack_d += 1
        elif letra == 'R':
            if stack_d:
                stack_d -= 1
                total_drs += 1
            elif found_r:
                break

            found_r = True
        else:
            found_r = False

    return total_drs
