'''
1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza 
esa función para calcular y mostrar en pantalla el factorial de todos los números 
enteros entre 1 y el número que indique el usuario 
'''

print("\nEjercicio 1\n")

def calcular_factorial(numero):
    if numero == 1:
        return numero
    else:
        return numero * calcular_factorial(numero-1)

numero = int(input("Ingresar número: "))
print(f"El valor del Factorial para la posición {numero} " \
    f"es: {calcular_factorial(numero)}")



'''
2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la 
posición indicada. Posteriormente, muestra la serie completa hasta la posición que 
el usuario especifique. 
'''

print("\n\nEjercicio 2\n")

def calcular_fibonacci(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return calcular_fibonacci(numero-1) + calcular_fibonacci(numero-2)

numero = int(input("Ingresar número: "))
print(f"El valor de la serie Fibonacci para la posición {numero} " \
    f"es: {calcular_fibonacci(numero)}")



'''
3) Crea una función recursiva que calcule la potencia de un número base elevado a 
un exponente, utilizando la fórmula n^m = n * n^(m-1). Prueba esta función en un 
algoritmo general. 
'''

print("\n\nEjercicio 3\n")

def calcular_potencia(n, m):
    if m == 1:
        return n
    else:
        return n * calcular_potencia(n, m-1)

n = int(input("Ingresar número: "))
m = int(input("Ingresar exponente: "))
print(f"El número {n} elevado a {m} es: {calcular_potencia(n,m)}")



'''
4) Crear una función recursiva en Python que reciba un número entero positivo en 
base decimal y devuelva su representación en binario como una cadena de texto. 
Cuando representamos un número en binario, lo expresamos usando solamente ceros 
(0) y unos (1), en base 2. Para convertir un número decimal a binario, se puede 
seguir este procedimiento:
1. Dividir el número por 2. 
2. Guardar el resto (0 o 1). 
3. Repetir el proceso con el cociente hasta que llegue a 0. 
4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario. 

Ejemplo: 
Convertir el número 10 a binario: 
10 ÷ 2 = 5     resto: 0   
5 ÷ 2 = 2     resto: 1   
2 ÷ 2 = 1     resto: 0   
1 ÷ 2 = 0     resto: 1   
Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es 
"1010". 
'''

print("\n\nEjercicio 4\n")

def decimal_a_binario(numero):
    if numero in [0, 1]:
        return str(numero)
    else:
        numero_nuevo = numero // 2
        resto = numero % 2
        return decimal_a_binario(numero_nuevo) + str(resto)

numero = int(input("Ingresar número: "))
print(f"El numero decimal {numero} convertido a binario " \
    f"es: {decimal_a_binario(numero)}")



'''
5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o 
False si no lo es.

Requisitos: 
La solución debe ser recursiva. 
No se debe usar [::-1] ni la función reversed(). 
'''

print("\n\nEjercicio 5\n")

def es_palindromo(palabra):
    retorno = None
    if palabra[0] == palabra[-1]:
        retorno = True
    else:
        retorno = False
    if len(palabra) in [1,2]:
        return retorno
    else:
        return retorno and es_palindromo(palabra[1:-1])

palabra = input("Ingresar palabra: ")
print(f"Es la palabra '{palabra}' un palindromo?: {es_palindromo(palabra)}")



'''
6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
número entero positivo y devuelva la suma de todos sus dígitos.

Restricciones: 
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.

Ejemplos: 
suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
suma_digitos(9)      → 9 
suma_digitos(305)    → 8   (3 + 0 + 5) 
'''

print("\n\nEjercicio 6\n")

def suma_digitos(n):
    numero_digito = str(n)[0]
    if len(str(n)) == 1:
        return int(numero_digito)
    else:
        return int(numero_digito) + suma_digitos(str(n)[1:])

numero = int(input("Ingresar número: "))
print(f"Suma de los digitos de {numero}: {suma_digitos(numero)}")



'''
7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca 
n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta 
llegar al último nivel con un solo bloque. 

Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en 
el nivel más bajo y devuelva el total de bloques que necesita para construir toda 
la pirámide. 

Ejemplos: 
contar_bloques(1)   → 1         (1) 
contar_bloques(2)   → 3         (2 + 1) 
contar_bloques(4)   → 10        (4 + 3 + 2 + 1) 
'''

print("\n\nEjercicio 7\n")

def contar_bloques(n):
    if (n == 1):
        return n
    else:
        return n + contar_bloques(n-1)

numero = int(input("Ingresar numero: "))
print(f"Cantidad de bloques totales cuando el nivel más bajo " \
    f"mide {numero}: {contar_bloques(numero)}")



'''
8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba 
un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas 
veces aparece ese dígito dentro del número. 
Ejemplos:
contar_digito(12233421, 2)   → 3
contar_digito(5555, 5)       → 4
contar_digito(123456, 7)     → 0
'''

print("\n\nEjercicio 8\n")

def contar_digito(numero, digito):
    numero_digito = str(numero)[0]
    retorno = None
    if numero_digito == str(digito):
        retorno = 1
    else:
        retorno = 0
    if len(str(numero)) == 1:
        return retorno
    else:
        return retorno + contar_digito(str(numero)[1:], digito)

numero = int(input("Ingresar numero: "))
digito = int(input("Ingresar dígito: "))
print(f"Cantidad de veces que se repite {digito} en "\
    f"{numero}: {contar_digito(numero, digito)}")