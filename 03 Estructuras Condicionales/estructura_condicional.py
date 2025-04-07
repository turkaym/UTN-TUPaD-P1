import random
from statistics import mode, median, mean

"""Ejercicio 1"""
edad_usuario = int(input("Ingresa tu edad: "))

# if edad_usuario >= 18:
#    print(f"Eres mayor de edad. Tines {edad_usuario} años.")
# else:
#    print(f"Eres menor de edad. Tienes {edad_usuario} años.")

"""Ejercicio 2"""

# nota_usuario = float(input("Ingresa tu nota: "))
# mensaje = "Aprobado" if nota_usuario >= 6 else "Desaprobado"
# print(mensaje)

"""Ejercicio 3"""

# solo_pares = int(input("Ingresa un numero par: "))
# if solo_pares % 2 == 0:
#    print(f"El numero {solo_pares} es par")
# else:
#    print(f"El numero {solo_pares} es impar. Por favor ingrese un numero par.")


"""Ejercicio 4"""

# usuario_edad = int(input("Ingresa tu edad: "))

# if usuario_edad < 12:
#    print(f"tienes {usuario_edad}. Eres un niño.")
# elif usuario_edad >= 12 and usuario_edad < 18:
#    print(f"Tienes {usuario_edad}. Eres adolecente.")
# elif usuario_edad >= 18 and usuario_edad < 30:
#    print(f"Tienes {usuario_edad}. Eres adulto joven")
# else:
#    print(f"Tienes {usuario_edad}. Eres adulto mayor")

"""Ejercicio 5"""

# while True:

#    contraseña = input("Ingresa una contraseña de entre 8 y 14 caracteres: ")

#    if 8 <= len(contraseña) <= 14:
#        print("Ha ingresado la contraseña correcta.")
#        break
#    else:
#        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

"""Ejercicio 6"""

# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular medidas estadísticas
# media = mean(numeros_aleatorios)
# mediana = median(numeros_aleatorios)
# moda = mode(numeros_aleatorios)

# Determinar el sesgo
# if media > mediana > moda:
#    sesgo = "positivo (sesgo a la derecha)"
# elif media < mediana < moda:
#    sesgo = "negativo (sesgo a la izquierda)"
# else:
#    sesgo = "no hay sesgo significativo"

# Imprimir resultados
# print(f"Números aleatorios: {numeros_aleatorios}")
# print(f"Media: {media}")
# print(f"Mediana: {mediana}")
# print(f"Moda: {moda}")
# print(f"Sesgo: {sesgo}")

"""Ejercicio 7"""
# frase = input("Ingresa una palabra o frase: ").strip()
# vocales = 'aeiouAEIOU'

# if frase[-1] in vocales:
#    print(f"{frase}!")
# else:
#    print(f"{frase}")

"""Ejercicio 8"""

# nombre_usuario = input("Ingresa tu nombre: ").strip()
# while True:
#    print(
#        """
#    Menu:
#    1. Nombre en mayuscula: PEDRO
#    2. Nombre en minuscula: pedro
#    3. Nombre con la primera letra mayuscula: Pedro
#    0. salir
# """)

#    opcion = input("Ingresa una opcion: ")

#    if opcion == '1':
#        print(nombre_usuario.upper())
#    elif opcion == '2':
#        print(nombre_usuario.lower())
#    elif opcion == '3':
#        print(nombre_usuario.title())
#    elif opcion == '0':
#        print("Hasta luego")
#        break
#    else:
#        print("Opcion no valida")

"""Ejercicio 9"""
# print(
"""
    Menor que 3: "Muy leve" 
    menor que 4: "Leve" 
    menor que 5: "Moderado"
    menor que 6: "Fuerte"
    menor que 7: "Muy Fuerte"
    Mayor o igual que 7: "Extremo"
"""
# )

# terremoto = float(input("Ingresa la magnitud del terremoto: "))

# if terremoto < 0:
#    print("Magnitud invalida")
# elif terremoto < 3:
#    print("Muy leve")
# elif terremoto < 4:
#    print("Leve")
# elif terremoto < 5:
#    print("Moderado")
# elif terremoto < 6:
#    print("Fuerte")
# elif terremoto < 7:
#    print("Muy fuerte")
# else:
#    print("Extremo")


"""Ejercicio 10"""
# hemisterio = input(
#    "Ingresa en que hemisferio te encuentras (n/s): ").strip().lower()
# mes = int(input("Ingresa un numero para el mes actual (1-12) "))
# dia = int(input("Ingresa el dia actual (1-31) "))


# if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
#    if hemisterio == "n":
#        print("invierno")
#    else:
#        print("Verano")
# elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
#    if hemisterio == "n":
#        print("Primavera")
#    else:
#        print("Otoño")
# elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
#    if hemisterio == "n":
#        print("Verano")
#    else:
#        print("Invierno")
# elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
#    if hemisterio == "n":
#        print("Otoño")
#    else:
#        print("Primavera")
