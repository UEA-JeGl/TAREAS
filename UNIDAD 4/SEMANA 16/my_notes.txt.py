# Escritura en el archivo de texto
with open("my_notes.txt", "w") as file:
    file.write("Primera nota: Aprender sobre archivos en Python.\n")
    file.write("Segunda nota: Practicar la lectura y escritura de archivos.\n")
    file.write("Tercera nota: Subir el código al repositorio de GitHub.\n")

# Lectura del archivo de texto línea por línea
with open("my_notes.txt", "r") as file:
    for line in file:
        print(line.strip())  # .strip() elimina espacios en blanco y saltos de línea

# Nota: El uso de 'with open' garantiza el cierre automático del archivo.