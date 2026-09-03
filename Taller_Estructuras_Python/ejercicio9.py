# Ejercicio 9: Buscar si un número existe en la lista
numeros = [10, 25, 30, 42, 50]
buscado = int(input("Ingrese el número a buscar: "))
if buscado in numeros:
    print(f"El número {buscado} SÍ existe en la lista.")
else:
    print(f"El número {buscado} NO existe en la lista.")
