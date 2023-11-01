# SE IMPORTA TODOS LOS MODULOS NECESARIOS
import sqlite3            
import datetime
import tkinter
from PIL import ImageTk,Image
from tkinter import messagebox
import ast

# ESTABLECEMOS CONEXION CON BASE DE DATOS Y EJECUTAMOS COMANDOS

conexion = sqlite3.connect('SCP.db')
cursor = conexion.cursor()

#-------------------------------------------------------------------------------------
# SE CREAN TABLAS CON LOS NOMBRES 'PRODUCTOS','VENTAS' Y 'USUARIOS' DENTRO DE LA BASE DE DATOS. :3

cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    precio REAL,
                    inversion REAL,
                    cantidad INTEGER,
                    precio_unidad REAL
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ventas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    producto_id INTEGER,
                    cantidad INTEGER,
                    fecha DATE,
                    venta REAL,
                    ganancia REAL,
                    FOREIGN KEY (producto_id) REFERENCES productos(id)
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                    (id INTEGER PRIMARY KEY,
                    usuario TEXT,
                    contraseña TEXT)''')

#-------------------------------------------------------------------------------------
# APARTIR DE AQUI SE DEFINEN TODAS LAS FUNCIONES QUE HARA LA APLICACION

# CREACION DE LA CUENTA
def register_user():
    usuario = input("Ingrese un nombre de usuario: ")
    contraseña = input("Ingrese una contraseña: ")

    cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (usuario,))
    existing_user = cursor.fetchone()

    if existing_user:
        print("El usuario ya está registrado. Intente con otro nombre de usuario.")
    else:
        cursor.execute("INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)", (usuario, contraseña))
        conexion.commit()
        print("Registro exitoso. El usuario se ha registrado correctamente.")

    conexion.close()

# INICIO DE SESION
def login_user():
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND contraseña = ?", (usuario, contraseña))
    user = cursor.fetchone()
    conexion.close()

    if user:
        print("Inicio de sesión exitoso para:", user[1])
    else:
        print("Nombre de usuario o contraseña incorrectos. Intente de nuevo.")

