
información_personal={
    "nombre": "Johanna",
    "edad": 36,
    "ciudad": "Guayaquil",
    "profesión":"Ingeniera en Sistema"
}
print(información_personal)

#acceder
información_personal["ciudad"]="Cuenca"

print(información_personal)

# Agregar una nueva clave-valor (ya existe "profesión", pero la aseguramos)
información_personal["profesión"] = "Desarrollador de Software"

# Verificar si "telefono" existe, si no, agregarlo
if "telefono" not in información_personal:
    información_personal["telefono"] = "0952147896"

# Eliminar la clave "edad"
del información_personal["edad"]

# Imprimir el diccionario final
print(información_personal)