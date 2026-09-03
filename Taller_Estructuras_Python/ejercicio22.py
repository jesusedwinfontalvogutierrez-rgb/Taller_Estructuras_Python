# Ejercicio 22: Crear una lista de tuplas con nombres y edades, mostrar solo mayores de edad
personas = [("Juan", 15), ("Laura", 22), ("Pedro", 17), ("Diana", 19)]
print("Personas mayores de edad:")
for nombre, edad in personas:
    if edad >= 18:
        print(f"- {nombre} ({edad} años)")
