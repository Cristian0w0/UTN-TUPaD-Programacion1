'''
1) Crea una variable llamada "numero1" y asígnale un número entero de 
tu elección.
'''
print("Ejercicio 1")
numero1 = 8
print(numero1)
print("")

'''
2) No borres la variable número uno y crea una variable llamada 
"numero2" asignándole un número decimal de tu elección.
'''
print("Ejercicio 2")
numero2 = 2.6
print(numero2)
print("")

'''
3) Crear una variable llamada "suma" y almacena la suma de "numero1" y 
"numero2".
'''
print("Ejercicio 3")
suma = numero1 + numero2
print(suma)
print("")

'''
4) Ahora crear tres variables más sin borrar lo que tienes. Una para 
resta, otra para multiplicación y otra para división. Imprime estas 
variables.
'''
print("Ejercicio 4")
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print(resta)
print(multiplicacion)
print(division)
print("")

'''
5) Crea una variable llamada "nombre" y asígnale tu nombre como valor.
'''
print("Ejercicio 5")
nombre = "Cristian"
print(nombre)
print("")

'''
6) Crea una variable llamada "precio" y asígnale un valor decimal que 
represente el precio de un artículo ficticio.
'''
print("Ejercicio 6")
precio = 141.3
print(precio)
print("")

'''
7) Ahora, sin borrar la variable anterior, crea una variable llamada 
"descuento" y asígnale un valor decimal que represente el descuento 
aplicado al artículo. Por ejemplo, si le quieres aplicar un 25% de 
descuento, dale un valor de 0,25. El valor 1 equivaldría al 100% y el 
valor 0 al 0%.
'''
print("Ejercicio 7")
descuento = 0.32
print(descuento)
print("")

'''
8) Ahora, intenta calcular el precio final aplicando el descuento al 
precio original y almacena el resultado en una variable llamada 
"precio_final". Para ello vas a tener que aplicar la lógica de 
matemáticas.
'''
print("Ejercicio 8")
precio_final = precio * (1 - descuento)
print(precio_final)
print("")

'''
9) Crea una variable llamada "cadena" y asignale un texto, una frase, 
lo que quieras de tu elección. Qué sea un string.
'''
print("Ejercicio 9")
cadena = "Mi primer programa"
print(cadena)
print("")

'''
10) Sin borrar la variable "cadena", crea una nueva variable llamada 
"longitud". En ella, vas a almacenar la longitud en caracteres de la 
cadena utilizando una de las funciones de Python.
'''
print("Ejercicio 10")
longitud = len(cadena)
print(longitud)
print("")

'''
11) Crea otra vez la variable llamada "precio" y dale un valor decimal, 
el que sea y conviértelo en número entero. Lo puedes hacer en la misma 
variable o en otra, da lo mismo.
'''
print("Ejercicio 11")
precio = 51.2
precio = int(precio)
print(precio)
print("")

'''
12) Crea dos variables. Una se va a llamar "nombre" y la segunda 
"apellido" concaténalas en una tercera variable llamada 
"nombre_completo", el nombre y el apellido con un espacio entre medio. 
Puedes usar libremente la forma de concatenación que quieras.
'''
print("Ejercicio 12")
nombre = "Cristian"
apellido = "Rodriguez"
nombre_completo = f"{nombre} {apellido}"
print(nombre_completo)
print("")

'''
13) Escribe tu edad en una variable. Increméntala en 5 y luego 
disminúyela en 10.
'''
print("Ejercicio 13")
edad = 25
edad = edad + 5
edad = edad - 10
print(edad)
print("")

'''
14) Crea una variable llamada "altura" que contenga con decimales, tu 
altura en metros y centímetros. Por ejemplo: 1.83.  Multiplícala por 4 
y luego divídela en 3.
'''
print("Ejercicio 14")
altura = 1.79
resultado_altura = (altura * 4) / 3
print(resultado_altura)
print("")

'''
15) Crea una variable que contenga tu nombre completamente en 
mayúsculas. Después transfórmalo todo en minúsculas con algún método o 
función de Python. 
'''
print("Ejercicio 15")
nombre_mayus = "CRISTIAN"
nombre_minus = nombre_mayus.lower()
print(nombre_minus)
print("")

'''
16) Por último, con la variable con el nombre en mayúsculas, aplica un 
método parecido para que se transforme todo en minúsculas excepto la primera letra. 
'''
print("Ejercicio 16")
nombre_capitalizado = nombre_mayus.capitalize()
print(nombre_capitalizado)
print("")