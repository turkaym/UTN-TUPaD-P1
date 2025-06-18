# arbol_listas.py
"""
Módulo principal: define la estructura básica del árbol y sus operaciones.
"""


def crear_arbol(valor):
    """
    Crea un nuevo árbol con el valor dado y subárboles vacíos.
    :param valor: dato a almacenar en la raíz del árbol
    :return: lista [valor, None, None]
    """
    return [valor, None, None]


def insertar_izquierda(arbol, valor):
    """
    Inserta un nuevo nodo con 'valor' como hijo izquierdo.
    Si ya había, ese subárbol pasa a ser hijo izquierdo del nuevo nodo.
    """
    if arbol[1] is None:
        arbol[1] = crear_arbol(valor)
    else:
        nuevo = crear_arbol(valor)
        nuevo[1] = arbol[1]
        arbol[1] = nuevo


def insertar_derecha(arbol, valor):
    """
    Inserta un nuevo nodo con 'valor' como hijo derecho.
    Si ya había, ese subárbol pasa a ser hijo derecho del nuevo nodo.
    """
    if arbol[2] is None:
        arbol[2] = crear_arbol(valor)
    else:
        nuevo = crear_arbol(valor)
        nuevo[2] = arbol[2]
        arbol[2] = nuevo


def imprimir_arbol(arbol, nivel=0):
    """
    Imprime el árbol rotado 90° en sentido horario.
    :param nivel: para controlar sangrías según profundidad.
    """
    if arbol is None:
        return
    imprimir_arbol(arbol[2], nivel+1)
    print('    ' * nivel + str(arbol[0]))
    imprimir_arbol(arbol[1], nivel+1)
