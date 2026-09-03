# BONUS (RETO): Programa tipo menú interactivo
def menu():
    lista = []
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar elemento\n2. Mostrar lista\n3. Eliminar elemento\n4. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            lista.append(input("Elemento a agregar: "))
        elif opcion == "2":
            print("Lista:", lista)
        elif opcion == "3":
            elem = input("Elemento a eliminar: ")
            if elem in lista: lista.remove(elem)
        elif opcion == "4":
            break
menu()
