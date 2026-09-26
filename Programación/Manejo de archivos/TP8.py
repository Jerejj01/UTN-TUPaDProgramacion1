# Ejercicio 1 - Crear archivo inicial con productos
with open("productos.txt", "w") as archivo:
    archivo.write("Coca-Cola,1500,30\n")
    archivo.write("Papitas,500,20\n")
    archivo.write("Cafe,250,40\n")


# Ejercicio 2 - Leer y mostrar productos
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if linea:
            nombre, precio, cantidad = linea.split(",")
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")


# Ejercicio 3 - Agregar productos desde teclado
print("\n--- Agregar nuevo producto ---")
nombre = input("Nombre: ")
precio = input("Precio: ")
cantidad = input("Cantidad: ")

with open("productos.txt", "a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

print(f"Se agregó '{nombre}' al archivo.")


# Ejercicio 4 - Cargar productos en una lista de diccionarios
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if linea:
            nombre, precio, cantidad = linea.split(",")
            productos.append({"nombre": nombre, "precio": int(precio), "cantidad": int(cantidad)})

print("\n--- Lista de diccionarios ---")
print(productos)


# Ejercicio 5 - Buscar producto por nombre
menu_buscar_producto = ""

while menu_buscar_producto != "2":
    menu_buscar_producto = input("\n1. Buscar datos de productos\n2. Salir\n")
    while menu_buscar_producto not in ("1", "2"):
        menu_buscar_producto = input("\nError, ingrese correctamente la opcion.\n1. Buscar datos de productos\n2. Salir\n")
    if menu_buscar_producto == "1":
        encontrado = False
        nombre_producto = input("Ingrese el nombre del producto: ")
        for i in productos:
            if nombre_producto == i["nombre"]:
                print(f"\nPrecio: {i['precio']} y cantidad: {i['cantidad']}")
                encontrado = True
        if not encontrado:
            print("\nEl producto no se encuentra registrado.")


# Ejercicio 6 - Guardar productos actualizados al archivo
print("\n--- Agregar nuevo producto ---")
nombre = input("Nombre: ")
precio = input("Precio: ")
cantidad = input("Cantidad: ")
productos.append({"nombre": nombre, "precio": int(precio), "cantidad": int(cantidad)})

with open("productos.txt", "w") as archivo:
    for producto in productos:
        archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")

print("Archivo actualizado.")
