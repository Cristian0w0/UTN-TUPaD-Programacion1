'''
Un instituto de inglés necesita un programa que le permita, cada día, 
procesar observaciones sobre las clases de ese día. El instituto dicta 
clases a estudiantes de distintos niveles y cada nivel tiene clases en 
un día de la semana diferente: los lunes se dicta nivel inicial, los 
martes el nivel intermedio, los miércoles el nivel avanzado, los jueves 
son para práctica hablada y los viernes se dicta inglés para viajeros. 

Se debe comenzar por solicitar al usuario que ingrese la fecha actual 
en formato “día, DD/MM”, donde [día] es un día de la semana, DD es el 
número de día y MM es el número de mes. Si el usuario ingresa un día de 
la semana inexistente o una fecha cuyo día supere el número 31 o el mes 
supere el número 12, finalizar el programa indicando que se produjo un 
error. Debe permitirse que ingrese el día de la semana en minúsculas o 
mayúsculas indistintamente. Como precondición se tiene que lo ingresado 
por el usuario tendrá la forma <[alfanumérico], [numérico]/[numérico]>.

Una vez indicada la fecha el usuario necesita poder indicar si ese día 
se tomaron los exámenes, pero eso solo si se trata de los niveles 
inicial, intermedio o avanzado, ya que las prácticas habladas y el 
inglés para viajeros no tienen exámenes. Si hubo exámenes, el usuario 
ingresará cuántos alumnos aprobaron y cuantos no, y el programa le 
mostrará el porcentaje de aprobados. 

Si el día fue el correspondiente a práctica hablada, el usuario deberá 
ingresar el porcentaje de asistencia a clase y el programa le indicará 
‘asistió la mayoría’ en caso de que la asistencia sea mayor al 50% o 
‘no asistió la mayoría’ si no es así. 

Si se trata del inglés para viajeros y la fecha actual corresponde al 
día 1 del mes 1 o del mes 7, se deberá imprimir ‘Comienzo de nuevo 
ciclo’ y solicitar al usuario que ingrese la cantidad de alumnos del 
nuevo ciclo y el arancel en $ por cada alumno, para luego imprimir el 
ingreso total en $. 
'''

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