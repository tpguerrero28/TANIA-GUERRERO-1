# Escritura de Archivo de Texto

# Crea y abre un nuevo archivo llamado my_notes.txt en modo escritura
with open('my_notes.txt', 'w') as file:
    # Escribe notas personales en el archivo
    file.write("Nota 1: realizando tareas semana 16\n")
    file.write("Nota 2: vamos logrando el objetivo.\n")
    file.write("Nota 3: tarea realizada con exito GRACIAS MISTER POR SUS ENSEÑANZA.\n")

# Lectura de Archivo de Texto

# Abre el archivo my_notes.txt en modo lectura
with open('my_notes.txt', 'r') as file:
    # Lee el contenido del archivo línea por línea
    for line in file:
        # Muestra cada línea leída en la consola
        print(line.strip())  # strip() elimina espacios en blanco al inicio y al final

# El uso de 'with' asegura que el archivo se cierre automáticamente al salir del bloque