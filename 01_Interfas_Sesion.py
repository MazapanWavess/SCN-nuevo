# IMPORTAMOS LIBRERIAS (FALTA LA LIBRERIA SQLITE)
import tkinter
#import sqlite3 
#from PIL import Image, ImageTk


#--------------------------------------------------------
# AQUI SE PONDRA LAS FUNCIONES QUE OCUPAREMOS

# FUNCIONES PARA BOTON INICIA SESION
def entrar(e):
    eti3["background"] = "#2d3541"
    eti3["foreground"] = "#00ADB5"

def salir(e):
    eti3["background"] = "#00ADB5"
    eti3["foreground"] = "#2d3541"

# FUNCIONES PARA LAS CAJAS DE TEXTO
def on_enter_usuario(e):
    usuario.delete(0, 'end')

def on_leave_usuario(e):
    if usuario.get() == '':
        usuario.insert(0, 'Usuario')
        

# LAS MISMAS FUNCIONES DE LA CAJA DE TEXTO "usuarios" PARA LA CAJA DE TEXTO "contraseña"
def on_enter_contraseña(e):
    contraseña.delete(0, 'end')

def on_leave_contraseña(e):
    if contraseña.get() == '':
        contraseña.insert(0, 'Contraseña')

# Nueva ventana
#--------------------------------------------------------

#--------------------------------------------------------

def otra_ventana():
    z=tkinter.Toplevel()
    z.geometry("925x500")
    z.title("Ventana secundaria")
    z.config(bg='#222831')

    def ventana_Agregar():
        t=tkinter.Toplevel()
        t.geometry("925x500")
        t.title("Ventana secundaria")
        t.config(bg='#222831')

    boton33=tkinter.Button(z,width=10, pady=7,text="Cerrar sesion",
                                bg="#00ADB5",
                                fg="#2d3541",
                                border=0,
                                activeforeground="#00ADB5",
                                activebackground="#2d3541",
                                command=z.destroy)
    boton33.place(x=10,y=10)

    nombre = usuario.get()
    nombre.upper()
    eti1=tkinter.Label(z,text="BIENVENIDO "+ nombre,
                        fg='#00ADB5', 
                        bg='#222831',
                        font=('Microsoft YaHei UI Light', 24, 'bold'))
    eti1.pack(padx=10,pady=10)

    eti2=tkinter.Label(z,text="MENÚ",
                        fg='#00ADB5', 
                        bg='#222831',
                        font=('Microsoft YaHei UI Light', 15, 'bold'))
    eti2.pack(fill="x",padx=10,pady=10)


# 1
    eti3=tkinter.Button(z,text="¿Como usar SCN?",
                        bg="#00ADB5",
                        fg="#2d3541",
                        width=15,
                        pady= 7,
                        border=0,
                        activeforeground="#00ADB5",
                        activebackground="#2d3541",
                        font=('Microsoft YaHei UI Light', 7, 'bold'),
                        command=ventana_Agregar)
    eti3.place(x=800,y=10)

# 2
    eti3=tkinter.Button(z,text="AGREGAR PRODUCTO",
                        bg="#00ADB5",
                        fg="#2d3541",
                        width=25,
                        border=0,
                        activeforeground="#00ADB5",
                        activebackground="#2d3541",
                        font=('Microsoft YaHei UI Light', 15, 'bold'))
    eti3.place(x=100,y=160)

# 3
    eti3=tkinter.Button(z,text="LISTA DE PRODUCTOS",
                        bg="#00ADB5",
                        fg="#2d3541",
                        width=25,
                        border=0,
                        activeforeground="#00ADB5",
                        activebackground="#2d3541",
                        font=('Microsoft YaHei UI Light', 15, 'bold'))
    eti3.place(x=100,y=260)

# 4
    eti3=tkinter.Button(z,text="BUSCAR PRODUCTO",
                        bg="#00ADB5",
                        fg="#2d3541",
                        width=25,
                        border=0,
                        activeforeground="#00ADB5",
                        activebackground="#2d3541",
                        font=('Microsoft YaHei UI Light', 15, 'bold'))
    eti3.place(x=100,y=360)

#5
    eti3=tkinter.Button(z,text="REGISTRAR VENTA",
                        bg="#00ADB5",
                        fg="#2d3541",
                        width=25,
                        border=0,
                        activeforeground="#00ADB5",
                        activebackground="#2d3541",
                        font=('Microsoft YaHei UI Light', 15, 'bold'))
    eti3.place(x=520,y=160)

#6
    eti3=tkinter.Button(z,text="VENTAS DEL DIA",
                        bg="#00ADB5",
                        fg="#2d3541",
                        width=25,
                        border=0,
                        activeforeground="#00ADB5",
                        activebackground="#2d3541",
                        font=('Microsoft YaHei UI Light', 15, 'bold'))
    eti3.place(x=520,y=260)

#7
    eti3=tkinter.Button(z,text="VENTAS ANTERIORES",
                        bg="#00ADB5",
                        fg="#2d3541",
                        width=25,
                        border=0,
                        activeforeground="#00ADB5",
                        activebackground="#2d3541",
                        font=('Microsoft YaHei UI Light', 15, 'bold'))
    eti3.place(x=520,y=360)


    eti3=tkinter.Button(z,text="SALIR",command=z.quit,
                        bg="#00ADB5",
                        fg="#2d3541",
                        width=25,
                        border=0,
                        activeforeground="#00ADB5",
                        activebackground="#2d3541",
                        font=('Microsoft YaHei UI Light', 10, 'bold'))
    eti3.place(x=345,y=450)

#--------------------------------------------------------


# CREAMOS LA VENTANA VENTANA
ventana = tkinter.Tk()
ventana.geometry("925x500")
ventana.title("SCN")
ventana.config(bg='#222831')

#--------------------------------------------------------
# AQUI SE PONDRA LA TABLAS PARA LA BASE DE DATOS


#--------------------------------------------------------
# Aquí se debe poner la imagen

img1 = tkinter.PhotoImage(file=(r"F:\04_Proyecto\scn nuevo\SCN-nuevo\01.png"))
tkinter.Label(ventana,image=img1,border=0,bg='#222831').place(x=50,y=50)


#--------------------------------------------------------
# ETIQUETAS Y CAJAS DE TEXTO INICIO DE SESION

# ETIQUETA 1
l2 = tkinter.Label(ventana, text="Inicia sesión", fg='#00ADB5', bg='#222831')
l2.config(font=('Microsoft YaHei UI Light', 24, 'bold'))
l2.place(x=570, y=60)

# FRAME PARA LAS CAJAS DE TEXTO
f1 = tkinter.Frame(ventana, width=350, height=350, bg='#222831')
f1.place(x=480, y=100)



# CAJA 1 CON SUS FUNCIONES
usuario = tkinter.Entry(f1, width=25, fg='#00ADB5', border=0, bg='#222831')
usuario.config(font=('Microsoft YaHei UI Light', 11, ))
usuario.bind("<FocusIn>", on_enter_usuario)
usuario.bind("<FocusOut>", on_leave_usuario)
usuario.insert(0, 'Usuario')
usuario.get()
usuario.place(x=30, y=60)

# frame de la parte inferior de la caja de texto 1
tkinter.Frame(f1, width=295, height=2, bg='WHITE').place(x=25, y=87)



# CAJA DE TEXTO 2 CON SUS FUNCIONES
contraseña = tkinter.Entry(f1, width=21, fg='#00ADB5', border=0, bg='#222831')
contraseña.config(font=('Microsoft YaHei UI Light', 11, ))
contraseña.bind("<FocusIn>", on_enter_contraseña)
contraseña.bind("<FocusOut>", on_leave_contraseña)
contraseña.insert(0, 'Contraseña')
contraseña.place(x=30, y=130)

# frame de la parte inferior de la caja de texto 2
tkinter.Frame(f1, width=295, height=2, bg='white').place(x=25, y=157)

#--------------------------------------------------------
# CREAMOS EL BOTON PARA EL INICIO DE SESION

eti3 = tkinter.Button(f1, width=39, pady=7, text='Inicia sesión',
                                bg="#00ADB5",
                                fg="#2d3541",
                                border=0,
                                activeforeground="#00ADB5",
                                activebackground="#2d3541",
                                command=otra_ventana)

eti3.place(x=35, y=204)
eti3.bind("<Enter>", entrar)
eti3.bind("<Leave>", salir)

#--------------------------------------------------------
# REGISTRARSE

#ETIQUETA SI NO TIENE CUENTA

l1=tkinter.Label(f1,text="No tienes cuenta?",fg="white",bg='#222831')
l1.config(font=('Microsoft YaHei UI Light',9, ))
l1.place(x=95,y=250)

b2=tkinter.Button(f1,width=8,text='Registrate',border=0,bg='#222831',fg='#00ADB5')
b2.place(x=200,y=250)


ventana.mainloop()


