#Ejercicio 1
for num in range(0, 101):
    print(num)

#Ejercicio 2
num = int(input("Decime un numero entrero: "))

if num >= 0:
    contador = len(str(num))
    print(f"La cantidad de digitos que tiene tu número es de: {contador}")
else:
    print("Seleccione un número entero, por favor.")

#Ejercicio 3
val_1 = int(input("Seleccione su primer valor: "))
val_2 = int(input("Seleccione su segundo valor: "))
suma = 0
if val_1 >= 0 and val_2 >= 0:
    for i in range(val_1 +1 , val_2):
        suma += i
        pass
    print(f"La suma que comprende estos dos valores da: {suma}")
else:
    print("Seleccione numeros enteros, por favor.")

#Ejercicio 4
num = int(input("Ingrese un número (detenerse con 0): "))
suma = 0

while num != 0:
    if num > 0:
        suma += num
    else:
        print("Ingrese un número entero, por favor.")
    num = int(input("Ingrese otro número (deterse con 0): "))

print(f"La suma total de estos numeros es de: {suma}")

#Ejercicio 5
import random
interfaz = input("¿Queres jugar un juego de adivinar el numero? (s/n): ").lower()

if interfaz in ("s", "n"):
    if interfaz == "s":
        intentos = 1
        num_aleatorio = random.randint(0, 9)
        num_jugador = int(input("Decime un número del 0 al 9: "))
        while num_jugador != num_aleatorio:
            num_jugador = int(input("Numero equivocado, intetalo otra vez: "))
            intentos += 1
        print(f"¡Muy bien el número aleatorio era el {num_aleatorio}!")
        print(f"¡Lo lograste en {intentos} intentos!")
    else:
        print("En otra ocación será")
else:
    print("Ingrese un valor correcto.")

#Ejercicio 6
for num in range(100, -2, -2):
    print(num)

#Ejercicio 7
num = int(input("Ingrese un número entero: "))
suma = 0

if num > 0:
    for total in range(0, num +1):
        suma += total

    print(f"La suma total dedes el 0 hasta el numero que eligio es de: {suma}")
else:
    print("Seleccione un numero entero.")

#Ejercicio 8
num_pares = 0
num_impares = 0
num_positivo = 0
num_negativo = 0

for i in range(0, 100):
    num = int(input("Decime un número: "))
    if num >= 0:
        num_positivo += 1
    elif num < 0:
        num_negativo += 1

    if num % 2 == 0:
        num_impares += 1
    else:
        num_pares += 1

print(f"""Los números positivos son: {num_positivo}
Los números negativos son: {num_negativo}
Los números impares son: {num_impares}
Los números pares son: {num_pares}""")

#Ejercicio 9
from statistics import mean

promedio = []
for i in range(0, 100):
    num = int(input("Ingresa números enteros: "))
    
    promedio.append(num)

media = mean(promedio)

print(f"La media de los números dados es de: {media}")

#Ejercicio 10
numero = input("Ingresa un número y te lo doy vuelta: ")
numero_inv = []

for i in numero:
    numero_inv.insert(0,i)

num_junto = "".join(numero_inv)
print(num_junto)