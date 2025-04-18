# import random

# 1
# print("\n Numeros enteros de 0 a 100: ")
# for i in range(101):
#    print(f"numero {i}")

# 2
# numero = int(input("Ingresa un numero entero: "))
# num = abs(numero)

# if num == 0:
#    contador = 1
# else:
#    contador = 0
#    while num > 0:
#        num = num // 10
#        contador += 1

# print(f"El numero {numero} tiene {contador} digitos")

# 3
# print("Programa para sumar los valores comprendidos entre el numero de inicio y numero de cierre \n")
# num_i = int(input("Ingresa el numero de inicio: "))
# num_c = int(input("Ingresa el numero de cierre: "))
# contador = 0

# if num_i >= num_c:
#    print(f"No hay valores comprendidos entre {num_i} y {num_c}")

# else:
#    for numero in range(num_i+1, num_c):
#        contador += numero

# print(
#    f"La suma de los valores comprendidos entre {num_i} y {num_c} es: {contador}")


# 4
# contador = 0

# while True:
#    numero = int(input("Ingresa un numero entero numero (0 para salir): "))

#    if numero == 0:
#        break

#    contador += numero

# print(contador)


# 5
# print("Juego: Adivina el numero")

# numero_secreto = random.randint(0, 9)
# intentos = 0

# while True:
#    numero = int(input("Elige un numero del 0 al 9: "))
#    if numero < 0 or numero > 9:
#        print("El numero debe ser entre 0 y 9. Vuelve a intentarlo")
#        break
#    intentos += 1

#    if numero == numero_secreto:
#        print(
#            f"Correcto! el numero era '{numero_secreto}' y te tomo '{intentos}' intentos")
#        break
#    elif numero > numero_secreto:
#        print("mas bajo")
#    else:
#        print("mas alto")

# 6
# for i in range(100, 0, -2):
#    print(f"numero: {i}")

# 7
# suma = 0

# while True:
#    numero = int(input("Ingresa un numero entero positivo: "))

#    if numero < 0:
#        print("El numero debe ser mayor a 0")

#    for num in range(0, numero+1):
#        suma += num
#    print(f"La suma de los numeros entre 0 y {numero} es: {suma}")


# 8
# cant_numeros = 10
# par = 0
# impar = 0
# positivo = 0
# negativo = 0

# for i in range(cant_numeros):
#    numeros = int(input(f"Ingresa un numero {i+1} / {cant_numeros}: "))

#    if numeros % 2 == 0:
#        par += 1
#    else:
#        impar += 1

#    if numeros > 0:
#        positivo += 1
#    elif numeros < 0:
#        negativo += 1
# print(f"pares {par}")
# print(f"impar {impar}")
# print(f"positivo {positivo}")
# print(f"negativo {negativo}")

# 9
# CANT_NUMEROS = 5
# acumulador = 0
# for i in range(CANT_NUMEROS):
#    numero = int(input(f"Ingresa un numero {i+1} / {CANT_NUMEROS}: "))
#    acumulador += numero

# media = acumulador / CANT_NUMEROS
# print(media)

# 10
# num = int(input("Ingresa un numero de 2 o mas digitos: "))
# invertido = 0

# while num > 0:
#    digit = num % 10
#    invertido = invertido * 10 + digit
#    num //= 10

# print(f"el numero ivertido es {invertido} ")
