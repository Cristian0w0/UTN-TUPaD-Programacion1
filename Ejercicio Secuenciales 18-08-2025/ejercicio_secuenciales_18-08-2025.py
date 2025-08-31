'''
Calculadora de propinas en un restaurante 
Un restaurante quiere ayudar a sus clientes a calcular cuánto dejar de 
propina según el monto de la cuenta. El programa debe: 
✓ Pedir al usuario el monto total de la cuenta. 
✓ Calcular la propina sugerida al 10%. 
✓ Calcular la propina sugerida al 15%. 
✓ Calcular el total a pagar en ambos casos (cuenta + propina). 
✓ Mostrar todos los resultados en pantalla.
'''

monto = float(input("Ingrese el monto de la cuenta: "))

propina_10 = monto * 0.10
propina_15 = monto * 0.15
total_10 = monto + propina_10
total_15 = monto + propina_15

print(f"Propina sugerida (10%): {propina_10}")
print("Total a pagar (10%):", total_10)
print(f"Propina sugerida (15%): {propina_15}")
print("Total a pagar (15%):", total_15)