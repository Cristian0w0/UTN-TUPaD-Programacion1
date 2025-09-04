'''
1) Crea un programa que imprima en pantalla todos los números enteros 
desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, 
mostrando un número por línea.
'''

print("Ejercicio 1\n")
for i in range(0,101):
    print(i)



'''
2) Desarrolla un programa que solicite al usuario un número entero y 
determine la cantidad de dígitos que contiene. 
'''

print("\nEjercicio 2\n")
num = int(input("Ingresar un número entero: "))
digitos = 1
while (num < -9 or num > 9):
    digitos += 1
    num -= num % 10
    num = int(num / 10)
print(f"Digitos: {digitos}")



'''
3) Escribe un programa que sume todos los números enteros comprendidos 
entre dos valores dados por el usuario, excluyendo esos dos valores. 
'''

print("\nEjercicio 3\n")
num_A = int(input("Ingresar un número entero: "))
num_B = int(input("Ingresar otro número entero: "))
suma = 0
if (num_A > num_B):
    for i in range(num_B+1, num_A):
        suma += i
elif (num_A < num_B):
    for i in range(num_A+1, num_B):
        suma += i
print(f"Suma: {suma}")



'''
4) Elabora un programa que permita al usuario ingresar números enteros y 
los sume en secuencia. El programa debe detenerse y mostrar el total 
acumulado cuando el usuario ingrese un 0. 
'''

print("\nEjercicio 4\n")
suma = 0
while True:
    num = int(input("Ingresar un número entero distinto de 0: "))
    if (num == 0):
        break
    suma += num
print(f"Suma: {suma}")



'''
5) Crea un juego en el que el usuario deba adivinar un número aleatorio 
entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron 
necesarios para acertar el número. 
'''

import random
print("\nEjercicio 5\n")
intentos = 0
num_rand = random.randint(0,9)
while True:
    num = int(input("Ingresar un número entero: "))
    intentos += 1
    if (num == num_rand):
        print(f"Adivinaste en {intentos} intentos")
        break
    else:
        print("Vuelve a intentar")



'''
6) Desarrolla un programa que imprima en pantalla todos los números 
pares comprendidos entre 0 y 100, en orden decreciente. 
'''

print("\nEjercicio 6\n")
for i in range(100,-1,-2):
    print(i)



'''
7) Crea un programa que calcule la suma de todos los números 
comprendidos entre 0 y un número entero positivo indicado por el 
usuario. 
'''

print("\nEjercicio 7\n")
num = int(input("Ingresar un número entero positivo: "))
suma = 0
if (num > 0):
    for i in range(0, num+1):
        suma += i
    print(f"Suma: {suma}")
else:
    print("No es entero positivo")



'''
8) Escribe un programa que permita al usuario ingresar 100 números 
enteros. Luego, el programa debe indicar cuántos de estos números son 
pares, cuántos son impares, cuántos son negativos y cuántos son 
positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo 
cambio).
'''

print("\nEjercicio 8\n")
positivos = 0
negativos = 0
pares = 0
impares = 0

for i in range(100):
    num = int(input("Ingresar un número entero: "))
    if (num > 0):
        positivos += 1
    elif (num < 0):
        negativos += 1
    if (num % 2) == 0:
        pares += 1
    else:
        impares += 1

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")



'''
9) Elabora un programa que permita al usuario ingresar 100 números 
enteros y luego calcule la media de esos valores. (Nota: puedes probar 
el programa con una cantidad menor, pero debe poder procesar 100 números 
cambiando solo un valor).
'''

print("\nEjercicio 9\n")
suma = 0
for i in range(100):
    num = int(input("Ingresar un número entero: "))
    suma += num
print(f"Media: {suma / 100}")



'''
10) Escribe un programa que invierta el orden de los dígitos de un 
número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el 
programa debe mostrar 745.
'''

print("\nEjercicio 10\n")
numero_inicial = int(input("Ingresar un número entero: "))
numero_invertido = 0

for i in range (0, len(str(numero_inicial))):
    j = len(str(numero_inicial)) - 1
    numero_invertido += (numero_inicial % 10) * (10 ** j)
    numero_inicial -=  numero_inicial % 10
    numero_inicial = int(numero_inicial / 10)

print(f"Número invertido: {numero_invertido}")