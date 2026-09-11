#Ejercicio 1
print("¡Hola Mundo!")

#Ejercicio 2
nombre = input("Ingrese su nombre:")

print(f"¡Hola {nombre}!")

#Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Ejercicio 4
radio = float(input("Ingrese el radio de su círculo: "))
pi = 3.14

print(f"El area de su círculo es {pi * radio ** 2} y su perimetro es {2 * pi * radio}")

#Ejercicio 5
segundos = int(input("Ingresa una cantidad de segundo: "))
horas = round(segundos / 3600, 2)

print(f"Esto equivale a {horas} horas")

#Ejercicio 6
num = int(input("Indica un numero y te digo su tabla de multiplicar: "))

print(f"1x{num}={num*1}")
print(f"2x{num}={num*2}")
print(f"3x{num}={num*3}")
print(f"4x{num}={num*4}")
print(f"5x{num}={num*5}")
print(f"6x{num}={num*6}")
print(f"7x{num}={num*7}")
print(f"8x{num}={num*8}")
print(f"9x{num}={num*9}")
print(f"10x{num}={num*10}")

#Ejercicio 7
num_1 = int(input("Primer número: "))
num_2 = int(input("Segundo número: "))

if num_1 != 0 and num_2 != 0:
    print(f"{num_1} + {num_2} = {num_1 + num_2}")
    print(f"{num_1} - {num_2} = {num_1 - num_2}")
    print(f"{num_1} x {num_2} = {num_1 * num_2}")
    print(f"{num_1} ÷ {num_2} = {num_1 / num_2}")
else:
    print("Seleccione un numero distinto a 0")

#Ejercicio 8
peso = float(input("Indique su peso: "))
altura = float(input("Indique su altura: "))
imc = peso / (altura ** 2)

print(f"Su índice de masa corporal es de {imc}")

#Ejercicio 9
celsius = float(input("Indique una temperatura en grados Celsius: "))
fahrenheit = (9/5)*celsius + 32

print(f"El equivalente en grados Fahrenheit es de {fahrenheit}°F")

#Ejercicio 10
num_1 = int(input("Primer número: "))
num_2 = int(input("Segundo número: "))
num_3 = int(input("Tercer número: "))

promedio = round((num_1 + num_2 + num_3) / 3, 2)

print(f"El promedio de estos número es de {promedio}")