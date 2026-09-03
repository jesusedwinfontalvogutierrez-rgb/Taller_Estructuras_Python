# Ejercicio 25: Programa de gestión de productos
tienda = {"Manzana": 1500, "Leche": 3800, "Pan": 2000}
print("--- PRODUCTOS EN TIENDA ---")
for producto, precio in tienda.items():
    print(f"- {producto}: ${precio}")
