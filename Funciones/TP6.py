# EJERCICIO 1
# Función que imprime "Hola Mundo!"
def imprimir_hola_mundo():
    return print("Hola Mundo!")  # Imprime el texto


# EJERCICIO 2
# Función que recibe un nombre y saluda al usuario
def saludar_usurario(nombre):
    return print(f"Hola {nombre}!")  # Imprime un saludo con el nombre


# EJERCICIO 3
# Función que recibe datos personales y los imprime
def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")  # Imprime la información


# EJERCICIO 4
# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    area = 3.14 * radio ** 2  # Fórmula: π * r²
    return area  # Devuelve el área calculada

# Función para calcular el perímetro de un círculo
def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio  # Fórmula: 2 * π * r
    return perimetro  # Devuelve el perímetro calculado


# EJERCICIO 5
# Función que convierte segundos a horas
def segundos_a_horas(segundos):
    transformacion = segundos / 3600  # Dividimos entre 3600 (segundos en una hora)
    return transformacion  # Devuelve el resultado


# EJERCICIO 6
# Función que imprime la tabla de multiplicar de un número
def tabla_multiplicar(numero):
    for n in range(1, 11):  # Repetir del 1 al 10
        print(f"{numero} * {n} = {n * numero}")  # Imprime cada multiplicación


# EJERCICIO 7
# Función que realiza las 4 operaciones básicas entre dos números
def operaciones_basicas(a, b):
    suma = f"{a} + {b} = {a+b}"  # Calcula la suma
    resta = f"{a} - {b} = {a-b}"  # Calcula la resta
    multiplicacion = f"{a} * {b} = {a*b}"  # Calcula la multiplicación
    divicion = f"{a} / {b} = {a/b}"  # Calcula la división
    resultados = f"""
{suma}
{resta}
{multiplicacion}
{divicion}"""  # Agrupa todos los resultados
    return resultados  # Devuelve todos los resultados


# EJERCICIO 8
# Función que calcula el índice de masa corporal (IMC)
def calcular_imc(peso, altura):
    formula_imc = peso / (altura ** 2)  # Fórmula: peso / (altura²)
    return formula_imc  # Devuelve el IMC calculado


# EJERCICIO 9
# Función que convierte grados Celsius a Fahrenheit
def celcius_a_fahrenheit(celsius):
    conversion = (celsius * 1.8) + 32  # Fórmula de conversión
    return conversion  # Devuelve la temperatura convertida


# EJERCICIO 10
# Función que calcula el promedio de 3 números
def calcular_promedio(a, b, c):
    calculo_de_promedio = (a + b + c) / 3  # Suma los tres números y divide entre 3
    return calculo_de_promedio  # Devuelve el promedio
