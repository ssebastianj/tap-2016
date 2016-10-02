# -*- coding: utf-8 -*-

import collections
import operator

Play = collections.namedtuple('Play', 'hojas_comidas puede_continuar posicion_actual')
bosque = []


class Arbol(object):
    def __init__(self, arbol_izq, arbol_der, cantidad_hojas):
        self.cantidad_hojas = cantidad_hojas
        self.arbol_izq = arbol_izq
        self.arbol_der = arbol_der

    def comer_hojas(self):
        hojas_por_comer = self.cantidad_hojas
        self.cantidad_hojas = 0
        return hojas_por_comer


def diferencia_hojas(info_juego):
    global bosque
    _, mabel_en_arbol, pacifica_en_arbol = info_juego[0]
    bosque = crear_bosque(info_juego[1:])

    # Juega Mabel
    mabel_cantidad_hojas = bosque[mabel_en_arbol - 1].comer_hojas()

    # Juega Pacifica
    pacifica_cantidad_hojas = bosque[pacifica_en_arbol - 1].comer_hojas()

    mabel_puede_continuar = True
    pacifica_puede_continuar = True
    while mabel_puede_continuar and pacifica_puede_continuar:
        # Juega Mabel
        mabel_play = ejecutar_turno_jugador(mabel_en_arbol)
        mabel_cantidad_hojas += mabel_play.hojas_comidas
        mabel_en_arbol = mabel_play.posicion_actual
        mabel_puede_continuar = mabel_play.puede_continuar

        # Juega Pacifica
        pacifica_play = ejecutar_turno_jugador(pacifica_en_arbol)
        pacifica_cantidad_hojas += pacifica_play.hojas_comidas
        pacifica_en_arbol = pacifica_play.posicion_actual
        pacifica_puede_continuar = pacifica_play.puede_continuar

    return mabel_cantidad_hojas - pacifica_cantidad_hojas


def obtener_arbol_en_posicion(posicion):
    global bosque
    return bosque[posicion - 1]


def ejecutar_turno_jugador(posicion_actual_koala):
    global bosque
    cantidad_hojas_comidas = 0
    puede_continuar_jugando = True

    # Obtener próximo árbol a moverse
    proximo_arbol = obtener_proximo_arbol(posicion_actual_koala)
    posicion_actual_koala = bosque.index(proximo_arbol) + 1

    # Comer hojas
    cantidad_hojas_comidas += comer_hojas(proximo_arbol)

    if not cantidad_hojas_comidas:
        puede_continuar_jugando = False
    return Play(cantidad_hojas_comidas, puede_continuar_jugando, posicion_actual_koala)


def obtener_proximo_arbol(posicion_actual_koala):
    arbol_izq = obtener_arbol_en_posicion(posicion_actual_koala).arbol_izq
    arbol_der = obtener_arbol_en_posicion(posicion_actual_koala).arbol_der

    if arbol_izq is None:
        proximo_arbol = arbol_der
    elif arbol_der is None:
        proximo_arbol = arbol_izq
    else:
        proximo_arbol = max(
            obtener_arbol_en_posicion(posicion_actual_koala).arbol_izq,
            obtener_arbol_en_posicion(posicion_actual_koala).arbol_der,
            key=operator.attrgetter('cantidad_hojas')
        )
    return proximo_arbol


def comer_hojas(arbol):
    posicion_actual_koala = bosque.index(arbol) + 1
    cantidad_hojas_comidas = bosque[posicion_actual_koala - 1].comer_hojas()
    return cantidad_hojas_comidas


def crear_bosque(info_arboles):
    bosque = [Arbol(None, None, cant_hojas) for cant_hojas in info_arboles[0]]

    for cuerda in info_arboles[1:]:
        cuerda_arbol_izq, cuerda_arbol_der = cuerda

        bosque_arbol_izq = bosque[cuerda_arbol_izq - 1]
        bosque_arbol_der = bosque[cuerda_arbol_der - 1]

        bosque_arbol_izq.arbol_der = bosque_arbol_der
        bosque_arbol_der.arbol_izq = bosque_arbol_izq
    return bosque
