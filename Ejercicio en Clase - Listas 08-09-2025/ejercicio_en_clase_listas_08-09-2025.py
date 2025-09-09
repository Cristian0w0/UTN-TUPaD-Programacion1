'''
Bingo 
1. Generá un cartón 5x5 con números aleatorios entre 1 y 50, sin 
repetirse. 
2. Mostrá el cartón al jugador en forma de matriz. 
3. El programa debe sortear números al azar entre 1 y 50, uno por uno. 
4. Cada vez que salga un número: 
    o Si está en el cartón, reemplazarlo por un 0.
    o Si no está, avisar que no aparece. 
    o Mostrar el cartón actualizado después de cada sorteo. 
5. El juego termina cuando el cartón completo queda en 0 (¡Bingo!).

Desafío extra: Validar cuando haya una línea completa (una fila llena 
de ceros) y mostrar el mensaje "¡Línea!". 
'''

import random

numeros = []
for i in range(1, 51):
    numeros.append(i)
random.shuffle(numeros)

carton = [[0 for _ in range(5)] for _ in range (5)]

print("Cartón: ")
for i in range(5):
    for j in range(5):
        carton[i][j] = numeros.pop(0)
        if (len(str(carton[i][j])) == 1):
            print("0", end="")
        print(carton[i][j], end=" ")
    print("")

for i in carton:
    numeros += i
random.shuffle(numeros)

completo = False
for i in range(1, 51):
    contador_ceros = 0
    num = numeros.pop(0)
    print(f"\nSorteo {i}: {num}")
    for j in range(len(carton)):
        linea_ceros = 0
        for k in range(len(carton[j])):
            if (carton[j][k] == 0):
                contador_ceros += 1
                linea_ceros += 1
            elif (num == carton[j][k] and num != -1):
                carton[j][k] = 0
                contador_ceros += 1
                linea_ceros += 1
                num = -1
            if (len(str(carton[j][k])) == 1):
                print("0", end="")
            print(carton[j][k], end=" ")
        if (linea_ceros == 5):
            print("¡Línea!")
        else:
            print("")
    if (contador_ceros == 25):
        completo = True
        break
    if (num != -1):
        print(f"No se encuentra el valor {num}")
print("\nCartón completo")