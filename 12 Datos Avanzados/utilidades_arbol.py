"""
Módulo de utilidades: recorridos, búsqueda y análisis.
"""


def inorden(arbol, resultado=None):
    """Recorrido inorden: izq → raíz → der."""
    if resultado is None:
        resultado = []
    if arbol is not None:
        inorden(arbol[1], resultado)
        resultado.append(arbol[0])
        inorden(arbol[2], resultado)
    return resultado


def preorden(arbol, resultado=None):
    """Recorrido preorden: raíz → izq → der."""
    if resultado is None:
        resultado = []
    if arbol is not None:
        resultado.append(arbol[0])
        preorden(arbol[1], resultado)
        preorden(arbol[2], resultado)
    return resultado


def postorden(arbol, resultado=None):
    """Recorrido postorden: izq → der → raíz."""
    if resultado is None:
        resultado = []
    if arbol is not None:
        postorden(arbol[1], resultado)
        postorden(arbol[2], resultado)
        resultado.append(arbol[0])
    return resultado


def buscar(arbol, valor):
    """Retorna True si 'valor' existe en el árbol, False en caso contrario."""
    if arbol is None:
        return False
    if arbol[0] == valor:
        return True
    return buscar(arbol[1], valor) or buscar(arbol[2], valor)


def altura(arbol):
    """Retorna la altura máxima del árbol."""
    if arbol is None:
        return 0
    return 1 + max(altura(arbol[1]), altura(arbol[2]))


def nivel_por_nivel(arbol):
    """Recorrido por niveles (BFS)."""
    if arbol is None:
        return []
    cola, resultado = [arbol], []
    while cola:
        nodo = cola.pop(0)
        resultado.append(nodo[0])
        if nodo[1]:
            cola.append(nodo[1])
        if nodo[2]:
            cola.append(nodo[2])
    return resultado
