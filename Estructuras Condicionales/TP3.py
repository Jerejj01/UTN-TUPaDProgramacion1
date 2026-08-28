#Ejercicio 1
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")

#Ejercicio 2
nota = float(input("Ingrese la nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3
numeros = int(input("Ingrese un número: "))

if numeros % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio 4
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Es un niño")
elif edad >= 12 and edad < 18:
    print("Es un adolescente")
elif edad >= 18 and edad < 30:
    print("Es un adulto joven")
else: 
    edad >= 30
    print("Es un adulto")

#Ejercicio 5
contrasenia = input("Ingrese su contraseña: ")
letras = len(contrasenia)

if letras >= 8 and letras <= 14:
    print("Ha ingresado una contraseña correcta")
    
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print("Lista:", numeros_aleatorios)
print("Moda:", moda)
print("Mediana:", mediana)
print("Media:", media)

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar el sesgo con los criterios dados")

#Ejercicio 7
frase_o_palabra = input("Ingrese una frase o palabra: ")
vocales = "a", "e", "i", "o", "u", "A", "E", "I", "O", "U"

if frase_o_palabra.endswith(vocales):
    print(f"{frase_o_palabra}!")
else:
    print(frase_o_palabra)

#Ejercicio 8
nombre = input("Ingrese su nombre: ")

print("1- Nombre en MAYÚSCULAS")
print("2- Nombre en minúsculas")
print("3- Nombre con la primera letra Mayúscula")

numero = (input("Ingrese la opción que desee: "))

if numero == "1":
    print(f"{nombre.upper()}")
elif numero == "2":
    print(f"{nombre.lower()}")
elif numero == "3":
    print(f"{nombre.title()}")
elif numero != "1" and numero != "2" and numero != "3":
    print("Seleccione una opción correcta")
else:
    pass

#Ejercicio 9
magnitud_terremoto = float(input("Dime una magnitud de un terremoto: "))

if magnitud_terremoto < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud_terremoto < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud_terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud_terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud_terremoto < 7:
    print("Muy fuerte (puede causar daños significativos)")
elif magnitud_terremoto >= 7:
    print("Extremo (puede causar graves daños a gran escala)")

#Ejercicio 10
hemisferio = input("En que hemisfeio se encuentra (N/S): ").upper()
mes = int(input("Que mes del año es (1-12): "))
dia = int(input("Que día del año es: "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
elif (mes == 3 and dia >= 21) or (mes in [3, 4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
else:
    estacion_norte = "Otoño"

if hemisferio == "N":
    estacion = estacion_norte
elif hemisferio == "S":
    equivalencias = {
        "Invierno" : "Verano",
        "Primavera" : "Otoño",
        "Verano" : "Invierno",
        "Otoño" : "Primavera"
    }
    estacion = equivalencias[estacion_norte]
else:
    estacion = "Hemisferio invalido"

print(f"Se encuentra en: {estacion}")