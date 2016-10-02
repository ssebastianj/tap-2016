# -*- coding: utf-8 -*-


def puede_hallar_secuencia(transiciones):
    app_objetivo = 1
    resto_aplicaciones = set(range(1, len(transiciones) + 1))
    resto_aplicaciones.remove(app_objetivo)

    trans_from_obj = set(transiciones[app_objetivo - 1])
    can_make_minimum_steps = not (resto_aplicaciones ^ trans_from_obj)
    can_make_first_steps = (
        can_make_minimum_steps or app_objetivo in trans_from_obj
    )

    resto_transiciones = list(transiciones)
    del resto_transiciones[app_objetivo - 1]

    columnas = (set(col) for col in zip(*resto_transiciones))

    can_make_last_steps = any(
        len(col) == 1 and col.pop() == app_objetivo
        for col in columnas
    )

    there_is_a_seq = can_make_first_steps and can_make_last_steps

    return 'S' if there_is_a_seq else 'N'
