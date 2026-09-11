#ejercicio 1
lista_multiplos_4 = list(range(0, 101, 4))

print(lista_multiplos_4)

#ejercicio 2
lista = ["Perro", "Gato", "Caballo", "Pez", "Pájaro"]

penultimo_elemento = lista[-2]

print(penultimo_elemento)

#ejercicio 3
lista = []
lista.append("python")
lista.append("java")
lista.append("javascript")

print(lista)

#ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"

print(animales)

#ejercicio 5
# El programa crea una lista de numeros, busca el valor maximo
# con max(), lo elimina de la lista con remove(), y luego
# imprime la lista sin ese elemento maximo.
# En este caso, el maximo es 22, asi que la lista resultante
# seria: [8, 15, 3, 7]

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

#ejercicio 6
lista = list(range(10, 31, 5))

print(lista[:2])

#ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "corolla"
autos[2] = "hilux"

print(autos)

#ejercicio 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

#ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente
compras[0].remove("pan")

# d) Imprimir la lista resultante
print(compras)

#ejercicio 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)
