'''
Calcular la patente de un auto con formato ABC123 dado un aumento 
numérico
'''

def main():
    patente_inicial = input("Ingresar patente: ").upper()
    aumento = int(input("Ingresar aumento de patente " \
    "(max 17575999): "))
    if validar_datos(patente_inicial, aumento):
        valor_inicial = calcular_valor_inicial(patente_inicial)
        valor_final = valor_inicial + aumento
        if (0 <= valor_final <= 17575999):
            patente_final = calcular_patente_final(valor_final)
            print(f"Patente final: {patente_final}")
        else:
            print("Patente final inválida, demasiado aumento")

#Validar datos
def validar_datos(patente_inicial:str, aumento:int):
    if (len(patente_inicial) == 6):
        for i in range(0,6):
            if (0 <= i <= 2 and not patente_inicial[i].isalpha() 
            or (3 <= i <= 5) and not patente_inicial[i].isnumeric()):
                print("Patente inválida")
                return False
    else:
        print("Patente inválida")
        return False
    if (0 <= aumento <= 17575999):
        return True
    else:
        print("Aumento inválido")
        return False

#Calcular valor inicial de patente
def calcular_valor_inicial(patente_inicial:str):
    valor_inicial = 0
    letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N",
            "O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    valor_inicial += letras.index(patente_inicial[0]) * 676000
    valor_inicial += letras.index(patente_inicial[1]) * 26000
    valor_inicial += letras.index(patente_inicial[2]) * 1000
    valor_inicial += int(patente_inicial[3]) * 100
    valor_inicial += int(patente_inicial[4]) * 10
    valor_inicial += int(patente_inicial[5])
    return valor_inicial


#Calcular patente con aumento
def calcular_patente_final(valor_final:int):
    patente_final = ""
    valor_letra1 = 0
    valor_letra2 = 0
    valor_letra3 = 0

    if (valor_final >= 676000):
        valor_letra1 = valor_final // 676000
        valor_final -= valor_letra1 * 676000
    if (valor_final >= 26000):
        valor_letra2 = valor_final // 26000
        valor_final -= valor_letra2 * 26000
    if (valor_final >= 1000):
        valor_letra3 = valor_final // 1000
        valor_final -= valor_letra3 * 1000

    letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N",
            "O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    patente_final += letras[valor_letra1]
    patente_final += letras[valor_letra2]
    patente_final += letras[valor_letra3]
    patente_final += str(valor_final)
    return patente_final

main()