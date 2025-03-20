def calcular_temperatura_promedio(temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad durante un período de tiempo.

    :param temperaturas: Diccionario con ciudades como claves y listas de temperaturas semanales como valores.
    :return: Diccionario con la temperatura promedio de cada ciudad.
    """
    promedios = {}
    for ciudad, temps in temperaturas.items():
        promedio = sum(temps) / len(temps)
        promedios[ciudad] = promedio
    return promedios


# Datos de ejemplo: temperaturas de 3 ciudades durante 4 semanas
datos_temperaturas = {
    "Ciudad A": [25, 26, 24, 27],
    "Ciudad B": [30, 32, 29, 31],
    "Ciudad C": [15, 18, 17, 16]
}

# Llamada a la función y mostrar resultados
promedios = calcular_temperatura_promedio(datos_temperaturas)
for ciudad, promedio in promedios.items():
    print(f"{ciudad}: {promedio:.2f}°C")