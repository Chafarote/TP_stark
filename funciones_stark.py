
# Desafio #00 --------------------------------------------------------------------

def menu_stark_00()-> None:
    print("--------Eliga el dato que desee obtener--------")
    print("-----------------------------------------------")
    print("a) Nombre de cada superheroe")
    print("b) Nombre de cada superheroe junto a su altura")
    print("c) Superheroe mas alto")
    print("d) Superheroe mas bajo")
    print("e) Altura promedio de los superheroes")
    print("f) Identidad del superheroe mas alto y mas bajo")
    print("g) Superheroe mas y menos pesado")
    print("h) Menu desafio 01")
    print("")
    return input("Ingrese una opcion: ")

def mostrar_nombres(lista:list)->None:
    """muestra todos los nombres de los superheroes

    Args:
        lista (list): Ingresa la lista con superheroes
    """
    mostrar_elemento(lista, "nombre")

def mostrar_elemento(lista:list, parametro:str)->None:
    """recorre la lista y muestra un dato de cada diccionario pasandole la key

    Args:
        lista (list): se pasa la lista a recorrer
        parametro (str): se pasa la key del elemento que se quiera mostrar
    """
    for elemento in lista:
        print(elemento[parametro])

def mapear_lista(procesadora, lista:list)->list:
    """genera una lista con los datos especificos que se le pida

    Args:
        procesadora (_type_): funcion para elegir los datos a devolver
        lista (list): lista original con todos los datos

    Returns:
        list: retorna una lista solo con los datos deseados
    """
    lista_retorno = []
    for elemento in lista:
        lista_retorno.append(procesadora(elemento))
    return lista_retorno

def mostrar_lista_tuplas(lista:list)->None:
    """muestra los elementos de una lista de tuplas

    Args:
        lista (list): lista con tuplas
    """
    for tupla in lista:
        for elemento in tupla:
            print(f"{elemento:24}", end="")
        print("")

def nombre_altura_y_superheroe(lista:list)->None:
    """muestra solo el nombre y la altura de los superheroes

    Args:
        lista (list): lista con todos los superheroes
    """
    print("Nombre                                 Altura")
    mostrar_lista_tuplas(mapear_lista(lambda heroe: (heroe["nombre"], float(heroe["altura"])), lista))

def maximo_elemento_lista(key:str, dato_a_retornar:str, lista:list)->dict:
    """busca el maximo de un elemento en una lista de diccionarios

    Args:
        key (str): key con la cual se busca comparar entre elementos
        dato_a_retornar (str): key del dato que se quiere retornar
        lista (list): lista con todos los elementos

    Returns:
        dict: retorna el dato deseado
    """
    flag = True
    for elemento in lista:
        if flag == True or float(elemento[key]) > maximo:
            maximo = float(elemento[key])
            retorno = elemento[dato_a_retornar]
            flag = False
    return retorno

def minimo_elemento_lista(key:str, dato_a_retornar:str, lista:list)->dict:
    """busca el minimo de un elemento en una lista de diccionarios

    Args:
        key (str): key con la cual se busca comparar entre elementos
        dato_a_retornar (str): key del dato que se quiere retornar
        lista (list): lista con todos los elementos

    Returns:
        dict: retorna el dato deseado
    """
    flag = True
    for elemento in lista:
        if flag == True or float(elemento[key]) < minimo:
            minimo = float(elemento[key])
            retorno = elemento[dato_a_retornar]
            flag = False
    return retorno

def superheroe_mas_alto(lista:list)->None:
    """muestra el nombre del superheroe mas alto

    Args:
        lista (list): lista con todos los superheroes
    """
    print(f"El superheroe mas alto es: {maximo_elemento_lista("altura", "nombre", lista)}")

def superheroe_mas_bajo(lista:list)->None:
    """muestra el nombre del superheroe mas bajo

    Args:
        lista (list): lista con todos los superheroes
    """
    print(f"El superheroe mas bajo es: {minimo_elemento_lista("altura", "nombre", lista)}")

def acumular_elemento_en_lista(key:str, lista:list)->float:
    """acumula los elementos de una key en una lista

    Args:
        key (str): key del elemento que se quiera guardar
        lista (list): lista con todos los elementos 

    Returns:
        float: retorna un dato flotante
    """
    lista_aux = []
    for elemento in lista:
            lista_aux.append(float(elemento[key]))
    return lista_aux

def promedio_elementos_lista(lista:list)->float:
    """hace el promedio de todos los elemtos de una lista

    Args:
        lista (list): lista con todos los enteros/flotantes

    Returns:
        float: retorna el promedio
    """
    tam = len(lista)
    acumulador = 0
    for elemento in lista:
        acumulador += elemento
    return acumulador / tam

def promedio_altura_superheroes(lista:list)->None:
    """muestra el promedio de altura de los superheroes

    Args:
        lista (list): lista con todos los superheroes
    """
    print(f"El promedio de altura de los superheroes es: {promedio_elementos_lista(acumular_elemento_en_lista("altura", lista))}")

def identidad_superheroe_max_min(lista:list):
    """muestra la identidad del heroe mas alto y el mas bajo

    Args:
        lista (list): lista con todos los superheroes
    """
    print(f"La identidad del superheroe mas alto es: {maximo_elemento_lista("altura", "identidad", lista)}")
    print(f"La identidad del superheroe mas bajo es: {minimo_elemento_lista("altura", "identidad", lista)}")

def superheroe_mas_menos_pesado(lista:list):
    """muestra el nombre del superheroe mas y menos pesado

    Args:
        lista (list): lista con todos los superheroes
    """
    print(f"El superheroe mas pesado es {maximo_elemento_lista("peso", "nombre", lista)} y el menos pesado es {minimo_elemento_lista("peso", "nombre", lista)}")

# Desafio #01 --------------------------------------------------------------------

def menu_stark_01():
    print("-----------Eliga el dato que quiere obtener del desafio 01-----------")
    print("---------------------------------------------------------------------")
    print("a) Nommbre de cada superheroe de genero masculino")
    print("b) Nombre de cada superheroe de genero femenino")
    print("c) Nombre del superheroe mas alto de genero masculino")
    print("d) Nombre del superheroe mas alto de genero femenino")
    print("e) Nombre del superheroe mas bajo de genero masculino")
    print("f) Nombre del superheroe mas bajo de genero femenino")
    print("g) Altura promedio de los superheroes de genero masculino")
    print("h) Altura promedio de los superheroes de genero femenino")
    print("i) Nombre del superheroe asociado a cada uno de los puntos anteriores")
    print("j) Determinar cuantos superheroes tienen cada tipo de color de ojos")
    print("k) Determinar cuantos superheroes tienen cada tipo de color de pelo")
    print("l) Determinar cuantos superheroes tienen cada tipo de inteligencia")
    print("m) Listar todos los superheroes agrupados por color de ojos")
    print("n) Listar todos los superheroes agrupados por color de pelo")
    print("o) Listar todos los superheroes agrupados por tipo de inteligencia")
    print("")
    return input("Ingrese una opcion: ")

def filtrar_lista(filtradora, lista:list)->list:
    """filtra los elementos deseados de una lista

    Args:
        filtradora (_type_): funcion para comparar los elementos que se quiera filtrar
        lista (list): lista con todos los datos

    Returns:
        list: retorna una lista nueva solo con los datos que coinciden 
    """
    lista_retorno = []
    for elemento in lista:
        if filtradora(elemento):
            lista_retorno.append(elemento)
    return lista_retorno

def mostrar_heroes_genero_masculino(lista:list)->None:
    """muestra solo a los heroes de genero masculino

    Args:
        lista (list): lista con todos los superheroes
    """ 
    mostrar_elemento(filtrar_lista(lambda heroe: heroe["genero"] == "M", lista), "nombre")

def mostrar_heroes_genero_femenino(lista:list)->None:
    """muestra solo a los heroes de genero femenino

    Args:
        lista (list): lista con todos los superheroes
    """
    mostrar_elemento(filtrar_lista(lambda heroe: heroe["genero"] == "F", lista), "nombre")

def mostrar_heroe_alto_masculino(lista:list)->None:
    """muestra el nombre del superheroe masculino mas alto

    Args:
        lista (list): lista con todos los superheroes
    """
    print(f"El superheroe mas alto del genero masculino es: {maximo_elemento_lista("altura", "nombre", filtrar_lista(lambda heroe: heroe["genero"] == "M", lista))}")

def mostrar_heroe_alto_femenino(lista:list)->None:
    """muestra el nombre del superheroe femenino mas alto

    Args:
        lista (list): lista con todos los superheroes
    """
    print(f"El superheroe mas alto del genero femenino es: {maximo_elemento_lista("altura", "nombre", filtrar_lista(lambda heroe: heroe["genero"] == "F", lista))}")

def mostrar_heroe_bajo_masculino(lista:list)->None:
    """muestra el nombre del superheroe masculino mas bajo

    Args:
        lista (list): lista con todos los superheroes
    """
    print(f"El superheroe mas bajo del genero masculino es: {minimo_elemento_lista("altura", "nombre", filtrar_lista(lambda heroe: heroe["genero"] == "M", lista))}")

def mostrar_heroe_bajo_femenino(lista:list):
    """muestra el nombre del superheroe femenino mas bajo

    Args:
        lista (list): lista con todos los superheroes
    """
    print(f"El superheroe mas bajo del genero femenino es: {minimo_elemento_lista("altura", "nombre", filtrar_lista(lambda heroe: heroe["genero"] == "F", lista))}")

def mostrar_altura_promedio_masculino(lista:list)->None:
    """muestra el promedio de altura de los superheroes de genero masculino

    Args:
        lista (list): lista con todos los superheroes
    """
    print(f"La altura promedio de los superheroes de genero masculino es: {promedio_elementos_lista(acumular_elemento_en_lista("altura", filtrar_lista(lambda heroe: heroe["genero"] == "M", lista)))}")

def mostrar_altura_promedio_femenino(lista:list)->None:
    """muestra el promedio de altura de los superheroes de genero femenino

    Args:
        lista (list): lista con todos los superheroes
    """
    print(f"La altura promedio de los superheroes de genero femenino es: {promedio_elementos_lista(acumular_elemento_en_lista("altura", filtrar_lista(lambda heroe: heroe["genero"] == "F", lista)))}")

def informar_nombre_superheroes_puntos_anteriores(lista:list):
    """muestra los nombres de los superheroes mas altos y bajos de cada genero 

    Args:
        lista (list): lista con todos los superheroes
    """
    mostrar_heroe_alto_masculino(lista)
    mostrar_heroe_alto_femenino(lista)
    mostrar_heroe_bajo_masculino(lista)
    mostrar_heroe_bajo_femenino(lista)

def listar_dato_repetido(key:str, lista:list)->list:
    """lista los datos de una key sin repetirlos

    Args:
        key (str): key a comparar   
        lista (list): lista con todos los datos

    Returns:
        list: retorna una lista con los datos sin repetirse
    """
    lista_aux = []
    for elemento in lista:
            lista_aux.append(elemento[key])
    lista_aux = set(lista_aux)
    return list(lista_aux)

def contador_dato_repetido_lista(key:str, lista:list)->list:
    """lista la cantidad de veces que aparece un dato en una lista

    Args:
        key (str): key de los datos que se quieran contabilizar
        lista (list): lista con todos los elementos

    Returns:
        list: retorna una lista de tuplas que contienen el dato y la cantidad de veces que se repitieron
    """
    lista_contadora = []
    datos_repetidos = listar_dato_repetido(key, lista)
    for dato in datos_repetidos:
        contador = 0
        for elemento in lista:
            if elemento[key] == dato:
                contador += 1
        if dato == "":
            dato = "No tiene"
        lista_contadora.append((dato, contador))
    return lista_contadora

def mostrar_cantidad_superheroes_color_ojos(lista:list)->None:
    """muestra la cantidad de superheroes con el mismo color de ojos

    Args:
        lista (list): lista con todos los superheroes
    """
    print("Color de ojos                              Cantidad")
    mostrar_lista_tuplas(contador_dato_repetido_lista("color_ojos", lista))

def mostrar_cantidad_superheroes_color_pelo(lista:list)->None:
    """muestra la cantidad de superheroes con el mismo color de pelo

    Args:
        lista (list): lista con todos los superheroes
    """
    print("Color de pelo                              Cantidad")
    mostrar_lista_tuplas(contador_dato_repetido_lista("color_pelo", lista))

def mostrar_cantidad_superheroes_inteligencia(lista:list)->None:
    """muestra la cantidad de superheroes con el mismo tipo de inteligencia

    Args:
        lista (list): lista con todos los superheroes
    """
    print("Tipo de inteligencia                          Cantidad")
    mostrar_lista_tuplas(contador_dato_repetido_lista("inteligencia", lista))

def mostrar_heroes_agrupados(key:str, lista:list):
    """muestra los superheroes agrupados un mismo dato

    Args:
        key (str): key del dato con el que se busca la coincidencia
        lista (list): lista con todos los superheroes
    """
    datos_repetidos = listar_dato_repetido(key, lista)
    for dato in datos_repetidos:
        if dato == "":
            agrupacion = "No tiene"
        else:
            agrupacion = dato
        print(f"Heroes agrupados por: {agrupacion}")
        mostrar_elemento(filtrar_lista(lambda heroe: heroe[key] == dato, lista), "nombre")




