import math

'''
1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
'''
print("Ejercicio 1")
print("Hola Mundo!")
print("")
'''

2) Crear un programa que pida al usuario su nombre e imprima por 
pantalla un saludo usando el nombre ingresado. Por ejemplo: si el 
usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola 
Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
realizar la impresión por pantalla. 
'''
print("Ejercicio 2")
nombre = input("Ingresar su nombre: ")
print(f"Hola {nombre}!")
print("")

'''
3) Crear un programa que pida al usuario su nombre, apellido, edad y 
lugar de residencia e imprima por pantalla una oración con los datos 
ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” 
y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas 
print(f…) para realizar la impresión por pantalla. 
'''
print("Ejercicio 3")
nombre = input("Ingresar su nombre: ")
apellido = input("Ingresar su apellido: ")
edad = input("Ingresar su edad: ")
residencia = input("Ingresar su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en \
{residencia}")
print("")

'''
4) Crear un programa que pida al usuario el radio de un círculo e 
imprima por pantalla su área y su perímetro. 
'''
print("Ejercicio 4")
radio = int(input("Ingresar el radio: "))
print(f"Área del círculo: {(radio ** 2) * math.pi}")
print(f"Perímetro del círculo: {2 * radio * math.pi}")
print("")

'''
5) Crear un programa que pida al usuario una cantidad de segundos e 
imprima por pantalla a cuántas horas equivale. 
'''
print("Ejercicio 5")
segundos = int(input("Ingresar cantidad de Segundos: "))
print(f"Cantidad de Horas: {segundos / 3600}")
print("")

'''
6) Crear un programa que pida al usuario un número e imprima por 
pantalla la tabla de multiplicar de dicho número.  
'''
print("Ejercicio 6")
numero = int(input("Ingresar un número: "))
print(f"{numero} * 0 = {numero * 0}")
print(f"{numero} * 1 = {numero * 1}")
print(f"{numero} * 2 = {numero * 2}")
print(f"{numero} * 3 = {numero * 3}")
print(f"{numero} * 4 = {numero * 4}")
print(f"{numero} * 5 = {numero * 5}")
print(f"{numero} * 6 = {numero * 6}")
print(f"{numero} * 7 = {numero * 7}")
print(f"{numero} * 8 = {numero * 8}")
print(f"{numero} * 9 = {numero * 9}")
print(f"{numero} * 10 = {numero * 10}")
print("")

'''
7) Crear un programa que pida al usuario dos números enteros 
distintos del 0 y muestre por pantalla el resultado de sumarlos, 
dividirlos, multiplicarlos y restarlos. 
'''
print("Ejercicio 7")
numero_1 = int(input("Ingresar un número entero distinto de 0: "))
numero_2 = int(input("Ingresar otro número entero distinto de 0: "))
print(f"Suma: {numero_1} + {numero_2} = {numero_1 + numero_2}")
print(f"Suma: {numero_1} - {numero_2} = {numero_1 - numero_2}")
print(f"Suma: {numero_1} * {numero_2} = {numero_1 * numero_2}")
print(f"Suma: {numero_1} / {numero_2} = {numero_1 / numero_2}")
print("")

'''
8) Crear un programa que pida al usuario su altura y su peso e imprima 
por pantalla su índice de masa corporal. Tener en cuenta que el índice 
de masa corporal se calcula del siguiente modo:
IMC = (peso en kg) / (altura en m)^2
'''
print("Ejercicio 8")
altura = float(input("Ingresar su altura en m: "))
peso = float(input("Ingresar su peso en Kg: "))
print(f"Índice de Masa Corporal = {peso / (altura) ** 2}")
print("")

'''
9) Crear un programa que pida al usuario una temperatura en grados 
Celsius e imprima por pantalla su equivalente en grados Fahrenheit. 
Tener en cuenta la siguiente equivalencia: 
Temperatura en Fahrenheit = (9/5) * Temperatura en Celsius + 32
'''
print("Ejercicio 9")
temp_celsius = int(input("Ingresar la temperatura en grados celsius: "))
print(f"Temperatura en grados Fahrenheit = {(9/5) * temp_celsius + 32}")
print("")

'''
10) Crear un programa que pida al usuario 3 números e imprima por 
pantalla el promedio de dichos números.
'''
print("Ejercicio 10")
numero_1 = int(input("Ingresar primer número: "))
numero_2 = int(input("Ingresar segundo número: "))
numero_3 = int(input("Ingresar tercer número: "))
print(f"Promedio = {(numero_1 + numero_2 + numero_3) / 3}")
print("")