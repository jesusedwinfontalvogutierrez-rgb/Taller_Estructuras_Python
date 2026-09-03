# Ejercicio 6: Contar cuántos números son pares en una lista
numeros = [10, 25, 30, 42, 50, 7]
pares = sum(1 for n in numeros if n % 2 == 0)
print("Cantidad de números pares:", pares)
