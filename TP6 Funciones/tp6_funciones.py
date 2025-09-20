def isfloat(num: str):
    return num.replace(".", "", 1).isdigit

'''
1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.
'''

print("\nEjercicio 1\n")

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()



'''
2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá 
devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
'''

print("\n\nEjercicio 2\n")

def saludar_usuario(nombre:str):
    return (f"Hola {nombre}!")

nombre = input("Ingresar nombre: ")

if (nombre != ""):
    saludo = saludar_usuario(nombre)
    print(saludo)
else:
    print("Datos inválidos")



'''
3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
dir los datos al usuario y llamar a esta función con los valores in
gresados.
'''

print("\n\nEjercicio 3\n")

def informacion_personal(nombre:str, apellido:str, edad:int, 
                        residencia:str):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en " \
        f"{residencia}.")

nombre = input("Ingresar nombre: ")
apellido = input("Ingresar apellido: ")
edad = input("Ingresar edad: ")
residencia = input("Ingresar residencia: ")

if (edad.isdigit() and not "" in (nombre, apellido, residencia)):
    edad = int(edad)
    informacion_personal(nombre, apellido, edad, residencia)
else:
    print("Datos inválidos")



'''
4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
dio como parámetro y devuelva el área del círculo. calcular_peri
metro_circulo(radio) que reciba el radio como parámetro y devuel
va el perímetro del círculo. Solicitar el radio al usuario y llamar am
bas funciones para mostrar los resultados.
'''

print("\n\nEjercicio 4\n")

import math

def calcular_area_circulo(radio:float):
    return (math.pi * (radio ** 2))

def calcular_perimetro_circulo(radio:float):
    return (2 * math.pi * radio)

radio = input("Ingresar radio: ")

if (isfloat(radio)):
    radio = float(radio)
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"Área: {area}")
    print(f"Perímetro: {perimetro}")
else:
    print("Datos inválidos")



'''
5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mos
trar el resultado usando esta función.
'''

print("\n\nEjercicio 5\n")

def segundos_a_horas(segundos:int):
    return (segundos / 3600)

segundos = input("Ingresar segundos: ")

if (segundos.isdigit()):
    segundos = int(segundos)
    horas = segundos_a_horas(segundos)
    print(f"Horas: {horas}")
else:
    print("Datos inválidos")



'''
6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la fun
ción.
'''

print("\n\nEjercicio 6\n")

def tabla_multiplicar(numero:int):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")

numero = input("Ingresar un número entero: ")

if (numero.isdigit()):
    numero = int(numero)
    tabla_multiplicar(numero)
else:
    print("Datos inválidos")



'''
7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resulta
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
sultados de forma clara.
'''

print("\n\nEjercicio 7\n")

def operaciones_basicas(a:float, b:float):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)

a = input("Ingresar el primer número: ")
b = input("Ingresar el segundo número: ")

if (isfloat(a) and isfloat(b)):
    a = float(a)
    b = float(b)
    tupla = operaciones_basicas(a, b)
    print("Tupla con operaciones básicas:")
    print(f"Suma: {tupla[0]}")
    print(f"Resta: {tupla[1]}")
    print(f"Multiplicación: {tupla[2]}")
    print(f"División: {tupla[3]}")
else:
    print("Datos inválidos")



'''
8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
ción para mostrar el resultado con dos decimales.
'''

print("\n\nEjercicio 8\n")

peso = input("Ingresar peso en kilogramos: ")
altura = input("Ingresar altura en metros: ")

def calcular_imc(peso:float, altura:float):
    print(f"ICM: {round(peso / (altura ** 2), 2)}")

if (isfloat(peso) and isfloat(altura)):
    peso = float(peso)
    altura = float(altura)
    calcular_imc(peso, altura)
else:
    print("Datos inválidos")



'''
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
'''

print("\n\nEjercicio 9\n")

celsius = input("Ingresar temperatura en grados Celsius: ")

def celsius_a_fahrenheit(celsius:float):
    return ((celsius * (9/5)) + 32)

if (isfloat(celsius)):
    celsius = float(celsius)
    print(f"Grados Fahrenheit: {celsius_a_fahrenheit(celsius)}")
else:
    print("Datos inválidos")



'''
10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
'''

print("\n\nEjercicio 10\n")

a = input("Ingresar primer número: ")
b = input("Ingresar segundo número: ")
c = input("Ingresar tercer número: ")

def calcular_promedio(a:float, b:float, c:float):
    return ((a + b + c) / 3)

if (isfloat(a) and isfloat(b) and isfloat(c)):
    a = float(a)
    b = float(b)
    c = float(c)
    print(f"Promedio: {calcular_promedio(a, b, c)}")
else:
    print("Datos inválidos")