'''
🔹 Ejercicio 1 — Sistema de becas estudiantiles

Enunciado
La universidad desea automatizar la postulación a becas. El programa 
debe pedir al usuario:
1.	Nombre y apellido.
2.	Edad (validada).
3.	Promedio general (0–10, validado).
4.	Ingresos familiares mensuales (validado).

Condiciones:
•	Si el promedio es menor a 6 → automáticamente rechazado.
•	Si el promedio es 6 o más:
    o	Si los ingresos familiares < $300.000 → beca completa.
    o	Si los ingresos entre $300.000 y $600.000 → media beca.
    o	Si los ingresos > $600.000 → rechazado.

Ejemplo de salida
✔ Juan Pérez, 20 años
Promedio: 8.2
Ingresos: $250000
Resultado: Beca completa
'''

print("Ejercicio 1\n")
nombre = input("Ingresar nombre: ")
apellido = input("Ingresar apellido: ")
edad = int(input("Edad: "))

if (edad >= 16):
    promedio = float(input("Ingresar promedio general (0–10): "))
    if (promedio >= 0 and promedio <= 10):
        ingresos = float(input("Ingresar ingresos familiares " \
        "mensuales: "))
        print(f"\n{nombre} {apellido}, {edad} años")
        print(f"Promedio: {promedio}")
        print(f"Ingresos: ${ingresos}")
        
        if promedio < 6 or ingresos > 600000:
            print("Beca Rechazada")
        elif ingresos < 300000:
            print("Beca completa")
        elif ingresos <= 600000:
            print("Media beca")
    else:
        print("Promedio no válido")
else:
    print("Edad no válida")



'''
🔹 Ejercicio 2 — Gestión de turnos hospitalarios

Enunciado
Un hospital quiere organizar turnos según el tipo de paciente. El 
sistema debe pedir:
1.	Nombre completo.
2.	DNI (validado).
3.	Edad.
4.	Obra social (sí/no).
5.	Prioridad médica: (1 = emergencia, 2 = urgente, 3 = control).

Reglas:
•	Si prioridad = 1 → asignar inmediatamente a guardia (fin del 
    programa).
•	Si prioridad = 2 →
    o	Si tiene obra social → turno en menos de 24 hs.
    o	Si no tiene obra social → turno en 48 hs.
•	Si prioridad = 3 →
    o	Si edad > 65 → turno preferencial en 72 hs.
    o	Caso contrario → turno normal en 7 días.

Ejemplo de salida
✔ Paciente: María Gómez
DNI: 30123456
Edad: 70
Prioridad: 3
Turno asignado: Preferencial en 72 hs
'''

print("\nEjercicio 2\n")
nombre = input("Ingresar nombre: ")
apellido = input("Ingresar apellido: ")
dni = int(input("Ingresar DNI: "))
turno = ""

if (len(str(dni)) == 8):
    edad = int(input("Ingresar edad: "))
    obra_social = input("¿Tiene obra social? (S/N): ").upper().strip()
    if (obra_social == "S" or obra_social == "N"):
        prioridad = int(input("Ingresar prioridad médica (1 = " \
            "emergencia, 2 = urgente, 3 = control): "))
        if (prioridad >= 1 and prioridad <= 3):
            if (prioridad == 1):
                Turno = "En menos de 24 hs"
            elif (prioridad == 2):
                if (obra_social == "S"):
                    turno = "En menos de 24hs"
                elif (obra_social == "N"):
                    turno = "En 48hs"
            elif (prioridad == 3):
                if (edad > 65):
                    turno = "Preferencial en 72hs"
                else:
                    turno = "Normal en 7 días"
            print(f"\nPaciente: {nombre}")
            print(f"DNI: {dni}")
            print(f"Edad: {edad}")
            print(f"Prioridad: {prioridad}")
            print(f"Turno asignado: {turno}")
        else:
            print("Prioridad médica inválida")
    else:
        print("Obra social inválida")
else:
    print("DNI inválido")



'''
🔹 Ejercicio 3 — Evaluación de crédito bancario

Enunciado
Un banco necesita evaluar créditos personales. El sistema pedirá:
1.	Nombre y apellido.
2.	CUIT (validado).
3.	Ingresos mensuales.
4.	Antigüedad laboral (en años).
5.	Historial crediticio: bueno / regular / malo.

Condiciones:
•	Si historial = malo → rechazo inmediato.
•	Si ingresos < $200.000 → rechazo.
•	Si ingresos ≥ $200.000 y antigüedad < 2 años → solo puede pedir 
    hasta $500.000.
•	Si ingresos ≥ $200.000 y antigüedad ≥ 2 años:
    o	Historial regular → hasta $1.000.000.
    o	Historial bueno → hasta $3.000.000.

Ejemplo de salida
✔ Cliente: Pedro Sánchez
CUIT: 20-30233444-9
Ingresos: $280000
Antigüedad: 3 años
Historial: bueno
Monto aprobado: $3,000,000
'''

print("\nEjercicio 3\n")
nombre = input("Ingresar nombre: ")
apellido = input("Ingresar apellido: ")
cuit = int(input("Ingresar CUIT sin guiones ni espacios: "))
monto = ""

if (len(str(cuit)) == 11):
    ingresos = float(input("Ingresar ingresos mensuales: "))
    antiguedad = int(input("Ingresar antigüedad laboral (en años): "))
    if (antiguedad >= 0):
        historial = input("Ingresar historial crediticio (bueno / " \
            "regular / malo): ").strip().lower()
        if (historial in ["bueno", "regular", "malo"]):
            if (ingresos < 200000 or historial == "malo"):
                monto = "Rechazado"
            else:
                monto = "aprobado: "
                if (ingresos >= 200000):
                    if (antiguedad < 2):
                        monto += "$500000"
                    elif (antiguedad >= 2):
                        if (historial == "regular"):
                            monto += "$1000000"
                        elif (historial == "bueno"):
                            monto += "$3000000"
            print(f"\nCliente: {nombre}")
            print(f"CUIT: {str(cuit)[0:2]}-{str(cuit)[2:10]}"\
                f"-{str(cuit)[10:]}")
            print(f"Ingresos: ${ingresos}")
            print(f"Antigüedad: {antiguedad} años")
            print(f"Historial: {historial}")
            print(f"Monto {monto}")
        else:
            print("Historial crediticio inválido")
    else:
        print("Antigüedad inválida")
else:
    print("CUIT inválido")