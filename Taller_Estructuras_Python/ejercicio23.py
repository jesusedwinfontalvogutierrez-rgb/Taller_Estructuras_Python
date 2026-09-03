# Ejercicio 23: Diccionario con nombres y listas de notas. Promedio por estudiante.
notas_estudiantes = {"Kenia": [4.5, 5.0, 4.8], "Jesus": [4.0, 4.2, 4.5], "Mateo": [3.0, 3.5, 4.0]}
for estudiante, notas in notas_estudiantes.items():
    prom = sum(notas) / len(notas)
    print(f"Estudiante: {estudiante} | Promedio: {prom:.2f}")
