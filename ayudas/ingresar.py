import sqlite3

# Función para crear la tabla de usuarios si no existe
def create_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                      (id INTEGER PRIMARY KEY,
                       username TEXT,
                       password TEXT)''')

    conn.commit()
    conn.close()

# Función para registrar un nuevo usuario
def register_user():
    username = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña: ")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username = ?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        print("El usuario ya está registrado. Intente con otro nombre de usuario.")
    else:
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("Registro exitoso. El usuario se ha registrado correctamente.")

    conn.close()

# Función para iniciar sesión
def login_user():
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        print("Inicio de sesión exitoso para:", user[1])
    else:
        print("Nombre de usuario o contraseña incorrectos. Intente de nuevo.")

# Crear la tabla de usuarios (ejecutar esto solo una vez)
create_table()

while True:
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    choice = input("Seleccione una opción: ")

    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    elif choice == "3":
        break
    else:
        print("Opción no válida. Intente de nuevo.")
