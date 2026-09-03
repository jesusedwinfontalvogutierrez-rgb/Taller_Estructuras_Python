# Ejercicio 8: Leer 5 números del usuario y guardarlos en una lista
lista_usuario = []
for i in range(5):
    num = int(input(f"Ingrese el número {i+1}: "))
    lista_usuario.append(num)
print("Números ingresados por el usuario:", lista_usuario)
