from arbol_listas import crear_arbol, insertar_izquierda, insertar_derecha, imprimir_arbol
from utilidades_arbol import inorden, preorden, postorden, buscar, altura, nivel_por_nivel


def menu():
    print("\nOpciones:")
    print("1. Insertar nodo")
    print("2. Imprimir árbol")
    print("3. Recorridos (inorden, preorden, postorden)")
    print("4. Buscar un valor")
    print("5. Altura del árbol")
    print("6. Recorrido por niveles")
    print("0. Salir")


def buscar_nodo(arbol, valor):
    """Busca el nodo con ese valor y lo retorna (referencia)."""
    if arbol is None:
        return None
    if arbol[0] == valor:
        return arbol
    izquierdo = buscar_nodo(arbol[1], valor)
    if izquierdo:
        return izquierdo
    return buscar_nodo(arbol[2], valor)


if __name__ == "__main__":
    raiz = None

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            valor = int(input("Ingrese el valor a insertar: "))
            if raiz is None:
                raiz = crear_arbol(valor)
                print("Raíz creada.")
            else:
                padre = int(input("Ingrese el valor del nodo padre: "))
                direccion = input(
                    "¿Insertar a la izquierda (i) o derecha (d)?: ").lower()
                nodo_padre = buscar_nodo(raiz, padre)
                if nodo_padre:
                    if direccion == "i":
                        insertar_izquierda(nodo_padre, valor)
                        print(f"{valor} insertado a la izquierda de {padre}.")
                    elif direccion == "d":
                        insertar_derecha(nodo_padre, valor)
                        print(f"{valor} insertado a la derecha de {padre}.")
                    else:
                        print("Dirección inválida.")
                else:
                    print("Nodo padre no encontrado.")

        elif opcion == "2":
            if raiz:
                imprimir_arbol(raiz)
            else:
                print("El árbol está vacío.")

        elif opcion == "3":
            if raiz:
                print("Inorden:", inorden(raiz))
                print("Preorden:", preorden(raiz))
                print("Postorden:", postorden(raiz))
            else:
                print("El árbol está vacío.")

        elif opcion == "4":
            valor = int(input("Valor a buscar: "))
            encontrado = buscar(raiz, valor)
            print(f"Resultado: {'Sí' if encontrado else 'No'}")

        elif opcion == "5":
            print("Altura del árbol:", altura(raiz))

        elif opcion == "6":
            print("Recorrido por niveles:", nivel_por_nivel(raiz))

        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
