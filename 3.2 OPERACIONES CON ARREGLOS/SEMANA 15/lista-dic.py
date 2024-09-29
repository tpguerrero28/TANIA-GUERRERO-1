# Crear un Diccionario
informacion_personal = {
    "nombre": "Alberto Muñoz",
    "edad": 32,
    "ciudad": "Guayaquil",
    "profesion": "Militar"
}

# Acceder y Modificar Valores
# Acceder al valor asociado con la clave "ciudad"
ciudad_actual = informacion_personal["ciudad"]
print(f"Ciudad actual: {ciudad_actual}")

# Modificar la ciudad
informacion_personal["ciudad"] = "Guayaquil"
print(f"Nueva ciudad: {informacion_personal['ciudad']}")

# Agregar una nueva clave-valor para representar la "profesion"
informacion_personal["profesion"] = "Militar"

# Verificar Existencia de Claves
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0998527812"

# Eliminar una Clave
if "edad" in informacion_personal:
    del informacion_personal["edad"]  # Eliminar la clave "edad"

# Imprimir el Diccionario Final
print("Diccionario final:")
print(informacion_personal)