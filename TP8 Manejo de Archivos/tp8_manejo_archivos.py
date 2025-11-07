'''
1) Crear archivo inicial con productos: Crear un archivo de texto llamado 
productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad
'''

print("\nEjercicio 1\n")

path_archivo = "producto.txt"
codificacion = "utf-8-sig"

cabecera_lista = ["Nombre", "Precio", "Cantidad"]
productos_lista = [["Lapicera", 120.5, 30], 
                    ["Lapiz", 80.75, 55],
                    ["Pluma", 230.0, 10]]

with open(path_archivo, "w", encoding=codificacion, newline="") as productos_archivo:
    productos_archivo.write(",".join(cabecera_lista) + "\n")
    for producto_lista in productos_lista:
        producto_linea = ",".join([str(producto_atributo) for producto_atributo in producto_lista])
        productos_archivo.write(producto_linea + "\n")

print("Archivo 'productos.txt' creado")



'''
2) Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
línea, la procese con .strip() y .split(","), y muestre los productos en el 
siguiente formato: 
'''

print("\n\nEjercicio 2\n")

def isfloat(numero:str):
    try:
        float(numero)
        return True
    except ValueError:
        return False

print("Leyendo y mostrando productos...\n")

with open(path_archivo, "r", encoding=codificacion, newline="") as productos_archivo:
    cabecera_lista = next(productos_archivo).strip().split(",")
    productos_lista = productos_archivo.readlines()
    for producto_linea in productos_lista:
        producto_lista = producto_linea.strip().split(",")
        for i in range(len(cabecera_lista)):
            print(f"{cabecera_lista[i]}: {producto_lista[i]}", end="")
            if i < len(cabecera_lista):
                print(" | ", end="")
        print("")



'''
3) Agregar productos desde teclado: Modificar el programa para que luego de 
mostrar los productos, le pida al usuario que ingrese un nuevo producto (nombre, 
precio, cantidad) y lo agregue al archivo sin borrar el contenido existente. 
'''

print("\n\nEjercicio 3\n")

producto_nombre = input("Ingresar nombre de producto: ")
producto_precio = float(input("Ingresar precio de producto: "))
producto_cantidad = int(input("Ingresar cantidad de producto: "))

with open(path_archivo, "a", encoding=codificacion, newline="") as productos_archivo:
    producto_linea = ",".join([producto_nombre, 
                            str(producto_precio), 
                            str(producto_cantidad)])
    productos_archivo.write(producto_linea + "\n")

print("\nProducto agregado")



'''
4) Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los 
datos en una lista llamada productos, donde cada elemento sea un diccionario con 
claves: nombre, precio, cantidad. 
'''

print("\n\nEjercicio 4\n")

print("Cargando productos a diccionario...\n")

productos_lista_de_dicts = []

with open(path_archivo, "r", encoding=codificacion, newline="") as productos_archivo:
    cabecera_lista = next(productos_archivo).strip().split(",")
    productos_lista = productos_archivo.readlines()
    for producto_linea in productos_lista:
        producto_lista = producto_linea.strip().split(",")
        producto_nombre = producto_lista[0]
        producto_precio = float(producto_lista[1])
        producto_cantidad = int(producto_lista[2])
        producto_lista = [producto_nombre, producto_precio, producto_cantidad]
        productos_lista_de_dicts.append(dict(zip(cabecera_lista, producto_lista)))

print("Lista de diccionarios creada\n")

for producto_dict in productos_lista_de_dicts:
    print(producto_dict)



'''
5) Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus 
datos. Si no existe, mostrar un mensaje de error. 
'''

print("\n\nEjercicio 5\n")

producto_nombre = input("Ingresar nombre de producto: ")

for producto_dict in productos_lista_de_dicts:
    if (producto_nombre == producto_dict["Nombre"]):
        print("\nProducto encontrado")
        print(producto_dict)
    elif (producto_dict == productos_lista_de_dicts[-1]):
        print("\nError: Producto no encontrado")



'''
6) Guardar los productos actualizados: Después de haber leído, buscado o agregado 
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
productos actualizados desde la lista. 
'''

print("\n\nEjercicio 6\n")

print("Actualizamos cantidad de Crayón y sobreescribimos archivo")
productos_lista_de_dicts[3]["Cantidad"] = 75

with open(path_archivo, "w", encoding=codificacion, newline="") as productos_archivo:
    productos_archivo.write(",".join(cabecera_lista) + "\n")
    for producto_dict in productos_lista_de_dicts:
        producto_linea = ",".join([str(producto_atributo) for producto_atributo in producto_dict.values()])
        productos_archivo.write(producto_linea + "\n")

print("\nArchivo actualizado")