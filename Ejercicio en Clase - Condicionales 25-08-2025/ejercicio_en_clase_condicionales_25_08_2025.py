fecha = str(input("Ingresar fecha actual en formato \"día DD/MM: "))

dia_semana:str = fecha.split(" ")[0].capitalize()
if (dia_semana == "Miercoles"):
    dia_semana = "Miércoles"
dia_mes:int = int(fecha.split(" ")[1].split("/")[0])
mes:int = int(fecha.split(" ")[1].split("/")[1])

dia_semana_valido = False
dia_mes_valido = False
mes_valido = False

if (dia_semana == "Lunes"):
    dia_semana_valido = True
elif (dia_semana == "Martes"):
    dia_semana_valido = True
elif (dia_semana == "Miércoles"):
    dia_semana_valido = True
elif (dia_semana == "Jueves"):
    dia_semana_valido = True
elif (dia_semana == "Viernes"):
    dia_semana_valido = True

if (dia_mes <= 31 and dia_mes >= 1):
    dia_mes_valido = True

if (mes <= 12 and dia_mes >= 1):
    mes_valido = True

examen:str = "F"
aprobados:int = 0
desaprobados:int = 0
asistencia:float = 0
alumnos_nuevo_ciclo:int = 0
arancel:float = 0.0

if (dia_semana_valido == True and dia_mes_valido == True and 
mes_valido == True):
    if (dia_semana in ["Lunes", "Martes", "Miércoles"]):
        if (dia_semana == "Lunes"):
            examen = input("Indicar si hubo examen en nivel inicial " \
            "(V/F): ").upper()
        elif (dia_semana == "Martes"):
            examen = input("Indicar si hubo examen en nivel " \
            "intermedio (V/F): ").upper()
        elif (dia_semana == "Miércoles"):
            examen = input("Indicar si hubo examen en nivel " \
            "avanzado (V/F): ").upper()
        if (examen == "V"):
            aprobados = int(input("Ingresar cantidad de alumnos " \
            "aprobados: "))
            desaprobados = int(input("Ingresar cantidad de alumnos " \
            "desaprobados: "))
            print(f"Porcentaje de aprobados = " \
            f"{aprobados * 100 / (aprobados + desaprobados)}%")
    elif (dia_semana == "Jueves"):
        asistencia = float(input("Ingresar porcentaje de asistencia: "))
        if (asistencia > 50):
            print("Asistió la mayoría")
        else:
            print("No asistió la mayoría")
    elif (dia_semana == "Viernes"):
        if (dia_mes == 1 and (mes == 1 or mes == 7)):
            print("Comienzo de nuevo ciclo")
            alumnos_nuevo_ciclo = int(input("Ingresar cantidad de " \
            "alumnos del nuevo ciclo: "))
            arancel = float(input("Ingresar el arancel: "))
            print(f"Ingreso total en $: {alumnos_nuevo_ciclo 
            * arancel}")
else:
    print("Fecha no válida")