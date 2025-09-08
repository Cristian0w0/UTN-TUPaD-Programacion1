'''
Ejercicio 1: Bucle for para números pares
1. Escribe un bucle for que imprima los números pares del 2 al 20 
(inclusive).
2. Usa un condicional o el paso del rango para lograrlo.

• ¿Cómo modificarías el código para imprimir solo impares?
-Cambiaría el inicio del rango de 2 a 1
• ¿Qué pasa si el rango fuera de 2 a 20 con paso 3?
-Imprimiría los elementos [2, 5, 8, 11, 14, 17, 20]
'''

print("Ejercicio 1\n")
for i in range(2, 21, 2):
	print(i)



'''
Ejercicio 2: Bucle while con suma acumulativa
1. Pide al usuario que ingrese números hasta que la suma supere 100.
2. Imprime la suma total al final.

• ¿Qué ocurre si el primer número ingresado es mayor que 100?
-No entraríamos al bucle
• ¿Cómo evitarías errores si el usuario ingresa texto?
-Hago que num pida un String y valido con el metodo isdigit() que sea 
un número
'''

print("\nEjercicio 2\n")
suma = 0
while (suma <= 100):
	num = int(input("Ingrese un número entero: "))
	suma += num
print(f"Suma = {suma}")



'''
Ejercicio 3: Filtrar palabras por letra inicial
1. Dada una lista de palabras (ej: ["apple", "banana", "avocado"]), 
imprime solo las que empiezan con "a".

• ¿Cómo harías que la comparación sea case-insensitive (ej: "Apple" 
también se cuente)?
-En la validación usaría un método que regrese toda la palabra en 
minusculas y luego la compare
• ¿Qué método de strings es útil para esto?
-lower() --> if (i.lower().startswith("a")):
'''

print("\nEjercicio 3\n")
lista_palabras = ["apple", "banana", "avocado"]
for i in lista_palabras:
	if (i.startswith("a")):
		print(i)



'''
Ejercicio 4: Tabla de multiplicar del 7
1. Imprime la tabla de multiplicar del 7 (desde 7x1=7 hasta 7x10=70).

• ¿Cómo adaptarías el código para que el usuario elija la tabla?
-Pediría ingresar un número entero antes del bucle que defina la tabla
• ¿Qué estructura usarías para almacenar los resultados?
-Un array porque todos los datos son del mismo tipo y están ordenados
'''

print("\nEjercicio 4\n")
for i in range(1, 11):
	print(f"7 x {i} = {7 * i}")



'''
Ejercicio 5: Contador de vocales
1. Pide al usuario una cadena de texto.
2. Cuenta y muestra cuántas vocales (a, e, i, o, u) contiene.

• ¿Cómo manejarías las vocales acentuadas (á, é)?
-Agregaría un condicional que las considere como vocales sin tílde
• ¿Qué estructura de datos te ayudaría a optimizar el código?
-Un diccionario, que tenga como llave la vocal y como valor la cantidad 
de esa vocal
'''

print("\nEjercicio 5\n")
texto = input("Ingresar una cadena de texto: ")
cantidad_vocales = [0, 0, 0, 0, 0]
vocales = ["a","e","i","o","u"]

for i in texto:
	if (i.lower() in vocales):
		letra_posicion = vocales.index(i)
		cantidad_vocales[letra_posicion] += 1
print("Cantidades:")
for i in vocales:
	print(f"{i}: {cantidad_vocales[vocales.index(i)]}")



'''
Ejercicio 6: Números repetidos en una lista
1. Dada una lista (ej: [3, 1, 3, 5, 1]), crea una nueva lista con los 
números que aparecen más de una vez (en este caso: [3, 1]).

• ¿Por qué es importante mantener el orden de aparición?
-Para evitar iteraciones innecesarias en bucles, cortando el bucle 
interno a la segunda aparición de un elemento
• ¿Cómo resolverías esto sin usar estructuras adicionales?
-Utilizando un set para evitar duplicados
'''

print("\nEjercicio 6\n")
lista_inicial = [3, 1, 3, 5, 1]
lista_final = []
for i in lista_inicial:
    contador = 0
    for j in lista_inicial:
        if (i == j):
            contador += 1
    if (contador >= 2 and not i in lista_final):
        lista_final.append(i)
print(lista_final)



'''
Ejercicio 7: FizzBuzz
1. Imprime números del 1 al 100, pero:
o Para múltiplos de 3 → "Fizz".
o Para múltiplos de 5 → "Buzz".
o Para múltiplos de ambos → "FizzBuzz".
• ¿Por qué el orden de los condicionales es crucial aquí?
-Porque para múltiplos de 3 y 5 necesito concatenar siempre primero 
Fizz y luego Buzz
• ¿Cómo extenderías el juego a otros números (ej: 7 → "Bazz")?
-Agregaría un tercer condicional validando que el número sea múltiplo 
de 7
'''

print("\nEjercicio 7\n")
for i in range(1, 101):
    texto = ""
    if (i % 3 == 0):
        texto += "Fizz"
    if (i % 5 == 0):
        texto += "Buzz"
    print(f"{i}: {texto}")



'''
Ejercicio 8: Frecuencia de palabras
1. Dada una cadena (ej: "hola hola mundo"), devuelve un diccionario con 
la frecuencia de cada palabra (ej: {"hola": 2, "mundo": 1}).

• ¿Cómo ignorarías signos de puntuación (ej: "hola," vs "hola")?
-Usaría el método replace() para cambiarlos por espacios
• ¿Qué método de strings ayuda a separar palabras?
-split()
'''

print("\nEjercicio 8\n")
texto = "hola, hola mundo"
diccionario = {}
for i in texto.split():
    contador = 0
    for j in texto.split():
        if (i == j):
            contador += 1
    if (not i in diccionario):
        diccionario[i] = contador
print(diccionario)



'''
Ejercicio 9: Filtrar consonantes
1. Dada una cadena, crea una nueva cadena que solo contenga sus 
consonantes (ej: "Hola" → "Hl").

• ¿Cómo manejarías las mayúsculas/minúsculas?
-Transformo la letra del loop en mayúscula/minúscula antes de la 
validación
• ¿Qué estructura usarías para definir las consonantes?
-Un array
'''

print("\nEjercicio 9\n")
texto_inicial = "Hola"
texto_final = ""
for i in texto_inicial:
    if (not i.lower() in ["a", "e", "i", "o", "u"]):
        texto_final += i



'''
Ejercicio 10: Números primos
1. Pide al usuario un número entero positivo.
2. Imprime todos los números primos menores o iguales a ese número.

• ¿Cómo optimizarías la verificación de primos?
-Podría inicial el programa con una validación en caso del número ser 
menor o igual a 2, de no serlo podría iterar solo los números impares.
Tambien podria implementar alguna librería con métodos útiles
• ¿Qué ventaja tiene usar range(2, int(n**0.5) + 1)?
-Reduce la cantidad de iteraciones necesarias para saber si el número 
es primo o no
'''

print("\nEjercicio 10\n")
num = int(input("Ingresar un número entero positivo: "))
print("Numeros primos: ")
for i in range(1, num+1):
    divisores = 0
    for j in range(1, i+1):
        if (i % j == 0):
            divisores += 1
    if (divisores == 2):
        print(i)



'''
Bonus:
• Diagrama de flujo: Elige un ejercicio y dibuja su diagrama de flujo.
-Ejercicio 3

• Reto extra: Modifica un ejercicio para usar break o continue.
'''

print("\nReto extra, Ejercicio 6 con Break\n")
lista_inicial = [3, 1, 3, 5, 1]
lista_final = []
for i in lista_inicial:
    contador = 0
    for j in lista_inicial:
        if (i == j):
            contador += 1
            if (contador == 2):
                break
    if (contador == 2 and not i in lista_final):
        lista_final.append(i)
print(lista_final)