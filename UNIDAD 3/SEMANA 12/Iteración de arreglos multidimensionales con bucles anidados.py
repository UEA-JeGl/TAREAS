import random

# Definir parámetros de la matriz
ciudades = ["CiudadA", "CiudadB", "CiudadC", "CiudadD", "CiudadE"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4  # Número de semanas registradas

# Crear la matriz 3D con temperaturas aleatorias entre 10 y 40 grados
matriz_temperaturas = [[[random.randint(10, 40) for _ in dias] for _ in range(semanas)] for _ in ciudades]

# Mostrar las temperaturas registradas
def mostrar_temperaturas():
    for i, ciudad in enumerate(ciudades):
        print(f"Temperaturas en {ciudad}:")
        for semana in range(semanas):
            print(f"  Semana {semana + 1}: {matriz_temperaturas[i][semana]}")
        print()

# Calcular y mostrar el promedio de temperaturas por ciudad y semana
def calcular_promedios():
    for i, ciudad in enumerate(ciudades):
        print(f"Promedios de temperatura en {ciudad}:")
        for semana in range(semanas):
            promedio = sum(matriz_temperaturas[i][semana]) / len(dias)
            print(f"  Semana {semana + 1}: Promedio = {promedio:.2f}°C")
        print()

# Llamar a las funciones para mostrar resultados
mostrar_temperaturas()
calcular_promedios()

