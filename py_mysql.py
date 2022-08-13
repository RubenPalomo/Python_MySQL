import mysql.connector

conexion = mysql.connector.connect(
    user = "root",
    password = "",
    host = "localhost",
    database = "pruebas"
)

existe_alumnos = False
mycursor = conexion.cursor()
mycursor.execute("SHOW TABLES")

for  table in mycursor:
    nombre_tabla = ''.join(table)
    if ("alumnos" in nombre_tabla):
        existe_alumnos = True

if not existe_alumnos:
    mycursor.execute(
        "CREATE TABLE alumnos (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(20), apellido VARCHAR(255))"
    )
    print("Tabla alumnos creada")


val = '("Johny", "Melavo"), ("Elsa", "Pato Aqui"), ("Aitor", "Tilla"), ("Rosa", "Melano"), ("Juan", "Car Lost"), ("Armando", "Bronca"), ("Fulanito", "Menganitez"), ("Nose", "Meocurre Nada")'
sql = f'INSERT INTO alumnos (nombre, apellido) VALUES {val}'
mycursor.execute(sql)

mycursor.execute("SELECT * FROM alumnos WHERE nombre = 'Aitor'")
myresult = mycursor.fetchall()

for datos in myresult:
    print(datos)

conexion.commit()
