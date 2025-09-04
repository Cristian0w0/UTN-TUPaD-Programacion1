'''
Calcular la patente de un auto con formato ABC123 dado un aumento 
numérico
'''

def main():
    patente_inicial = input("Ingresar patente: ").upper()
    aumento = int(input("Ingresar aumento de patente: "))
    validar_datos(patente_inicial, aumento)
    if validar_datos:
        valor_inicial = calcular_valor_inicial(patente_inicial)
        valor_final = valor_inicial + aumento
        if (0 <= valor_final <= 2775999):
            patente_final = calcular_patente_final(valor_final)
            print(f"Patente final: {patente_final}")
        else:
            print("Patente final inválida")

#Validar datos
def validar_datos(patente_inicial:str, aumento:int):
    if (len(patente_inicial) == 6):
        for i in range(0,6):
            if (0 <= i <= 2 and not patente_inicial[i].isalpha() 
            or (3 <= i <= 5) and not patente_inicial[i].isnumeric()):
                print("Patente no válida")
                return False
    else:
        print("Patente no válida")
        return False
    if (0 <= aumento <= 2775999):
        return True

#Calcular valor inicial de patente
def calcular_valor_inicial(patente_inicial:str):
    valor_inicial = 0
    letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N",
            "O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i in range(0,6,1):
        j = 5-i
        if (0 <= i <= 2):
            valor_inicial += letras.index(patente_inicial[i]) * \
            (10 ** (j))
        elif (3 <= i <= 5):
            valor_inicial += int(patente_inicial[i]) * (10 ** (j))
    return valor_inicial


#Calcular patente con aumento
def calcular_patente_final(valor_final:int):
    patente_final = ""
    valor_letra1 = 0
    valor_letra2 = 0
    valor_letra3 = 0
    while True:
        if valor_final >= 100000 and valor_letra1 == 0:
            valor_letra1 = valor_final // 100000
            if (valor_letra1 > 25):
                valor_letra1 -= valor_letra1 - 25
            valor_final -= valor_letra1 * 100000
        elif valor_final >= 10000 and valor_letra2 == 0:
            valor_letra2 = valor_final // 10000
            if (valor_letra2 > 25):
                valor_letra2 -= valor_letra2 - 25
            valor_final -= valor_letra2 * 10000
        elif valor_final >= 1000 and valor_letra3 == 0:
            valor_letra3 = valor_final // 1000
            if (valor_letra3 > 25):
                valor_letra3 -= valor_letra3 - 25
            valor_final -= valor_letra3 * 1000
        else:
            break
    letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N",
            "O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    patente_final += letras[valor_letra1]
    patente_final += letras[valor_letra2]
    patente_final += letras[valor_letra3]
    patente_final += str(valor_final)
    return patente_final

main()