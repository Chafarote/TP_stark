from data_stark import lista_personajes
from funciones_stark import *

"""
Nombre: Gabriel Gomez
DNI: 38942983
"""

while True:
    match menu_stark_00():
        case "a":
            mostrar_nombres(lista_personajes)
        case "b":
            nombre_altura_y_superheroe(lista_personajes)
        case "c":
            superheroe_mas_alto(lista_personajes)
        case "d":
            superheroe_mas_bajo(lista_personajes)
        case "e":
            promedio_altura_superheroes(lista_personajes)
        case "f":
            identidad_superheroe_max_min(lista_personajes)
        case "g":
            superheroe_mas_menos_pesado(lista_personajes)
        case "h":
            match menu_stark_01():
                case "a":
                    mostrar_heroes_genero_masculino(lista_personajes)
                case "b":
                    mostrar_heroes_genero_femenino(lista_personajes)
                case "c":
                    mostrar_heroe_alto_masculino(lista_personajes)
                case "d":
                    mostrar_heroe_alto_femenino(lista_personajes)
                case "e":
                    mostrar_heroe_bajo_masculino(lista_personajes)
                case "f":
                    mostrar_heroe_bajo_femenino(lista_personajes)
                case "g":
                    mostrar_altura_promedio_masculino(lista_personajes)
                case "h":
                    mostrar_altura_promedio_femenino(lista_personajes)
                case "i":
                    informar_nombre_superheroes_puntos_anteriores(lista_personajes)
                case "j":
                    mostrar_cantidad_superheroes_color_ojos(lista_personajes)
                case "k":
                    mostrar_cantidad_superheroes_color_pelo(lista_personajes)
                case "l":
                    mostrar_cantidad_superheroes_inteligencia(lista_personajes)
                case "m":
                    mostrar_heroes_agrupados("color_ojos", lista_personajes)
                case "n":
                    mostrar_heroes_agrupados("color_pelo", lista_personajes)
                case "o":
                    mostrar_heroes_agrupados("inteligencia", lista_personajes)
        case _:
            break








