from arbol_listas import crear_arbol, insertar_izquierda, insertar_derecha, imprimir_arbol
from utilidades_arbol import inorden, preorden, postorden, buscar, altura, nivel_por_nivel

if __name__ == "__main__":
    # Construimos un árbol de ejemplo
    raiz = crear_arbol(10)
    insertar_izquierda(raiz, 5)
    insertar_derecha(raiz, 15)
    insertar_izquierda(raiz[1], 3)
    insertar_derecha(raiz[1], 7)

    # Salidas
    print("Impresión del árbol:")
    imprimir_arbol(raiz)

    print("Inorden:", inorden(raiz))
    print("Preorden:", preorden(raiz))
    print("Postorden:", postorden(raiz))

    print("Buscar 7:", buscar(raiz, 7))
    print("Altura:", altura(raiz))
    print("Por niveles:", nivel_por_nivel(raiz))
