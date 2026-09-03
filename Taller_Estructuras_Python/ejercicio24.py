# Ejercicio 24: Crear una lista de diccionarios y mostrar todos los datos
estudiantes_db = [{"id": 1, "nombre": "Andrés", "carrera": "Sistemas"}, {"id": 2, "nombre": "Sofia", "carrera": "Diseño"}, {"id": 3, "nombre": "Gabriel", "carrera": "Sistemas"}]
print("--- BASE DE DATOS DE ESTUDIANTES ---")
for est in estudiantes_db:
    print(f"ID: {est['id']} | Nombre: {est['nombre']} | Carrera: {est['carrera']}")
