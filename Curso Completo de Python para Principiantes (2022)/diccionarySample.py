# Crear un diccionario
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Bogotá"
}

# Acceder a los valores por clave
print(persona["nombre"])  # Salida: Juan
print(persona["edad"])    # Salida: 30

# Modificar un valor
persona["edad"] = 31

# Añadir un nuevo par clave-valor
persona["profesion"] = "Ingeniero"
persona["empresa"] = "SoftwareOne"

# Verificar si una clave está en el diccionario
print("ciudad" in persona)  # Salida: True
print("genero" in persona)  # Salida: False

# Obtener una lista de todas las claves
claves = persona.keys()
print(claves)  # Salida: dict_keys(['nombre', 'edad', 'ciudad', 'profesion'])

# Obtener una lista de todos los valores
valores = persona.values()
print(valores)  # Salida: dict_values(['Juan', 31, 'Bogotá', 'Ingeniero'])