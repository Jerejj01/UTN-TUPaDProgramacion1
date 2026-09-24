# Ejercicio 1
precios_frutas = {
    "Banana" : 1200,
    "Ananá" : 2500,
    "Melón" : 3000,
    "Uva" : 1450
}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300


# Ejercicio 2
precios_frutas = {
    "Banana" : 1200,
    "Ananá" : 2500,
    "Melón" : 3000,
    "Uva" : 1450,
    "Naranja" : 1200,
    "Manzana" : 1500,
    "Pera" : 2300
}

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800


# Ejercicio 3
precios_furtas = {
    'Banana': 1330,
    'Ananá': 2500,
    'Melón': 2800,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1700,
    'Pera': 2300
    }

frutas = list(precios_furtas.keys())


# Ejercicio 4
contactos = {}

for c in range(1, 6):
    agregar_contactos = input("Ingrese su contacto: ")
    while True:
        if not agregar_contactos.isalpha():
            agregar_contactos = input("Error, Ingrese correctamente su contacto: ")
        else:
            break
    numero_contacto = input("Ingrese su número: ")
    while True:
        if not numero_contacto.isdigit():
            numero_contacto = input("Error, Ingrese correctamente su número: ")
        else:
            break
    numero_contacto = int(numero_contacto)

    contactos[agregar_contactos] = numero_contacto

menu = ""
while menu != "2":
    menu = input("""
---------------
1. Ver contacto
2. Salir
---------------
""")
    while True:
        if menu not in ("1", "2"):
            menu = input("""
Error, ingrse correctamente la opción
---------------
1. Ver contacto
2. Salir
---------------
""")
        else:
            break
    if menu == "1":
        pedir_contacto = input("Ingrese el contacto que quiera ver el numero: ")
        while True:
            if not pedir_contacto.isalpha():
                pedir_contacto = input("Error, ingrese correctamente el nombre del contacto: ")
            else:
                break
        if pedir_contacto in contactos:
            print()
            print(f"El numero de {pedir_contacto} es: {contactos[pedir_contacto]}")
        else:
            print()
            print("El contacto ingresado no existe.")


# Ejercicio 5
frase = input("Ingrese su frase: ")

frase = frase.split()

palabras_unicas = set(frase)

recuento = {}

for i in frase:
    recuento[i] = recuento.get(i, 0) + 1

print(palabras_unicas)
print(recuento)


# Ejercicio 6
alumnos = {}

for nombres in range(1,4):
    nombres_alumnos = input("Ingrese el nombre del alumno: ")
    while True:
        if not nombres_alumnos.isalpha():
            nombres_alumnos = input("Error, ingrese correctamente el nombre del alumno: ")
        else:
            break
    notas_alumno = []
    for notas in range(1, 4):
        notas_alumnos = input(f"Ingrese la nota n°{notas}: ")
        while not notas_alumnos.isdigit() or int(notas_alumnos) not in range(1, 11):
            notas_alumnos = input("Error, ingrese un número entre 1 y 10: ")
        notas_alumno.append(int(notas_alumnos))
    alumnos[nombres_alumnos] = tuple(notas_alumno)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es de {promedio}")


# Ejercicio 7
parcial_1 = {101, 102, 103, 104}
parcial_2 = {103, 104, 105, 106}

aprobaron_ambos_parciales = parcial_1.intersection(parcial_2)

aprobo_solo_uno_de_los_dos = parcial_1.symmetric_difference(parcial_2)

estudiantes_aprobaron_al_menos_un_parcial = parcial_1.union(parcial_2)

print(f"""
Los alumnos que aprobaron ambos parciales son: {aprobaron_ambos_parciales}.
Los alumnos que aprobaron solo uno de los dos parciales son: {aprobo_solo_uno_de_los_dos}.
Los alumnos que aprobaron al menos un parcial son: {estudiantes_aprobaron_al_menos_un_parcial}.""")


# Ejercicio 8
productos_y_stock = {
    "gomitas" : 20,
    "papitas" : 10,
    "gaseosa" : 15,
    "agua" : 30
}

menu = ""

while menu != "2":
    menu = input("""
---------------------------------
1. Consultar stock y cargar (si no existe se cargara el producto)
2. Salir
---------------------------------

""")
    while True:
        if not menu in ("1", "2"):
            menu = input("""
Error, cargue correctamente el valor que desee.
---------------------------------
1. Consultar stock y cargar (si no existe se cargara el producto)
2. Salir
---------------------------------

""")
        else:
            break
    if menu == "1":
        producto = input("Ingrese el producto deseado: ")
        while True:
            if not producto.isalpha():
                producto = input("Error. Ingrese correctamente el producto: ")
            else:
                break

        if producto in productos_y_stock:
            print(f"El stock del {producto} es de: {productos_y_stock[producto]}")
            menu_cargar_stock = input("Desea cargar stock? S/N ")
            menu_cargar_stock = menu_cargar_stock.upper()
            while True:
                if not menu_cargar_stock in ("S", "N"):
                    menu_cargar_stock = input("Error, elija correctamente la opción. S/N ")
                    menu_cargar_stock = menu_cargar_stock.upper()
                else:
                    break
            if menu_cargar_stock == "S":
                carga = input("Ingrese la cantidad repuesta: ")
                while True:
                    if not carga.isdigit():
                        carga = input("Error, ingrese correctamente la cantidad repuesta: ")
                    else:
                        break
                carga = int(carga)
                productos_y_stock[producto] += carga
                print(f"El nuevo stock de {producto} es de: {productos_y_stock[producto]}")
            else:
                pass
        else:
            ingreso_stock_nuevo = input("Ingrese la cantidad de stock inicial del producto: ")
            while True:
                if not ingreso_stock_nuevo.isdigit():
                    ingreso_stock_nuevo = input("Error, ingrese correctamente la cantidad incial de stock del producto nuevo: ")
                else:
                    break
            ingreso_stock_nuevo = int(ingreso_stock_nuevo)
            productos_y_stock[producto] = ingreso_stock_nuevo
            print(f"Ya quedo registrado el nuevo producto ({producto}) y su stock inicial es de: {productos_y_stock[producto]}")


# Ejercicio 9
agenda = {
    ("lunes", "10:00") : "Reunion",
    ("martes", "15:00") : "Clase de inglés"
}

menu = ""

while menu != "2":
    menu = input("""
1. Consultar agenda
2. Salir
""")
    while True:
        if menu not in ("1", "2"):
            menu = input("""
Error, ingrese correctamente la opción deseada.
1. Consultar agenda
2. Salir
""")
        else:
            break

    if menu == "1":
        consultar_dia = input("Ingrese el día deseado: ")
        consultar_hora = input("Ingrese la hora deseada: ")

        if (consultar_dia, consultar_hora) in agenda:
            evento = agenda[(consultar_dia, consultar_hora)]
            print(f"El {consultar_dia} a las {consultar_hora} usted tiene: {evento}")

        else:
            print("Usted no tiene nada agendado para esa fecha en ese horario.")


# Ejercicio 10
diccionario_original = {
    "Argentina" : "Buenos Aires",
    "Chile" : "Santiago"
}
diccionario_invertido = {}

for pais, capital in diccionario_original.items():
    diccionario_invertido[capital] = pais

print(diccionario_invertido)
