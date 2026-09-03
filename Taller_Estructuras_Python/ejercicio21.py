# Ejercicio 21: Crear un diccionario con 3 estudiantes y sus notas, luego mostrar el promedio
estudiantes = {"Ana": 4.5, "Luis": 3.8, "Camilo": 4.2}
promedio = sum(estudiantes.values()) / len(estudiantes)
print("Promedio general de los estudiantes:", round(promedio, 2))
