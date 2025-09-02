'''
Ejercicio For

Un grupo de amigos decide organizar un juego de estrategia, para lo 
cual forman dos equipos de 6 integrantes cada uno, donde un integrante 
de cada equipo es el “jefe” y los otros 5 son sus “oficiales”. La regla 
más importante del juego es que sólo se comunicarán mediante un canal 
común, por lo que deben buscar la forma de ocultar el contenido de sus 
mensajes. Uno de los equipos decide utilizar un método antiguo de 
encriptación llamado “la cifra del césar”, que consiste en correr cada 
letra del mensaje –considerando la posición de cada una en el alfabeto– 
una determinada cantidad de lugares. Ejemplo: si el corrimiento es de 2 
lugares, la palabra “ATAQUE” se transforma en “CVCSWG”. Cada día, el 
“jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales.

Escribir un programa que permita encriptar los 5 mensajes. El 
corrimiento (cantidad de lugares que se correrán las letras) será dado 
por el usuario antes de comenzar a encriptar. Los 5 mensajes usarán el 
mismo corrimiento. Nota: si el alfabeto termina antes de poder correr 
la cantidad de lugares necesarios, se vuelve a comenzar desde la letra 
“a”.

Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”.
Utilizando el alfabeto español, de 27 letras, el siguiente cálculo 
matemático permite volver a comenzar por el principio una vez que se 
llegó a la “z”: (índice de la letra a correr+corrimiento)%27 Sólo se 
encriptarán las letras de los mensajes, dejando al resto de caracteres 
sin modificación. 
'''

corrimiento = int(input("Ingresar corrimiento de encriptación: "))
mensaje = input("Ingresar el mensaje a encriptar: ").upper()
alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

if str(mensaje).isalpha():
    for oficial in range(1,6,1):
        mensaje_encriptado = ""
        for letra in mensaje:
            posicion_letra = mensaje.find(letra) + corrimiento
            if posicion_letra >= 27:
                posicion_letra -= 27
            letra_corrida = alfabeto[posicion_letra:posicion_letra+1]
            mensaje_encriptado += letra_corrida
        print(f"Oficial {oficial}: {mensaje_encriptado}")
        corrimiento += corrimiento
else:
    print("Mensaje inválido")



'''
Ejercicio While

Vas a programar un juego clásico contra la computadora: Piedra, papel o 
tijeras.
Reglas:
1. El programa debe mostrar un menú con las opciones:
    o Piedra
    o Papel
    o Tijera
2. El jugador elegirá una opción.
3. La computadora elegirá su jugada al azar.
4. El programa debe comparar ambas jugadas y mostrar quién gana:
    o Piedra vence a Tijera.
    o Tijera vence a Papel.
    o Papel vence a Piedra.
    o Si ambos eligen lo mismo, es empate.

Extra (para hacerlo más divertido):
• Llevar un marcador de cuántas partidas gana el jugador y cuántas gana 
la computadora. 
• El juego termina cuando el jugador elija salir, mostrando el 
resultado final.
'''

import random
opcion_jug = 1
marcador_jug = 0
marcador_pc = 0
while (opcion_jug != 0):
    print("\n--Menu--")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("0. Salir")
    opcion_jug = int(input("\nElegir una opción: "))
    opcion_pc = random.randint(1,3)
    if (opcion_jug == opcion_pc):
        print("Hay empate")
    elif ((opcion_jug == 1 and opcion_pc == 2) or
        (opcion_jug == 2 and opcion_pc == 3) or
        (opcion_jug == 3 and opcion_pc == 1)):
        print("PC Gana")
        marcador_pc += 1
    elif ((opcion_pc == 1 and opcion_jug == 2) or
        (opcion_pc == 2 and opcion_jug == 3) or
        (opcion_pc == 3 and opcion_jug == 1)):
        print("Jugador Gana")
        marcador_jug += 1
    else:
        print(f"\nMarcador jugador: {marcador_jug}")
        print(f"Marcador pc: {marcador_pc}")
        print("Gracias por jugar!")