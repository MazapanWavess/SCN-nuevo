# IMPORTAMOS LIBRERIAS (FALTA LA LIBRERIA SQLITE)
import tkinter
import sqlite3 

#--------------------------------------------------------
# AQUI SE PONDRA LAS FUNCIONES QUE OCUPAREMOS

# FUNCIONES PARA BOTON INICIA SESION
def entrar(e):
    boton_Iniciar["background"] = "#00ADB5"
    boton_Iniciar["foreground"] = "#222831"

def salir(e):
    boton_Iniciar["background"] = "#222831"
    boton_Iniciar["foreground"] = "#00ADB5"

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


#--------------------------------------------------------
# CREAMOS LA VENTANA VENTANA
ventana = tkinter.Tk()
ventana.geometry("925x500")
ventana.title("SCN")
ventana.config(bg='white')

#--------------------------------------------------------
# AQUI SE PONDRA LA TABLAS PARA LA BASE DE DATOS

#--------------------------------------------------------
# Aquí se debe poner la imagen

#--------------------------------------------------------
# ETIQUETAS Y CAJAS DE TEXTO INICIO DE SESION

# ETIQUETA 1
l2 = tkinter.Label(ventana, text="Inicia sesión", fg='#00ADB5', bg='white')
l2.config(font=('Microsoft YaHei UI Light', 24, 'bold'))
l2.place(x=570, y=60)

# FRAME PARA LAS CAJAS DE TEXTO
f1 = tkinter.Frame(ventana, width=350, height=350, bg='white')
f1.place(x=480, y=100)



# CAJA 1 CON SUS FUNCIONES
usuario = tkinter.Entry(f1, width=25, fg='#00ADB5', border=0, bg='white')
usuario.config(font=('Microsoft YaHei UI Light', 11, ))
usuario.bind("<FocusIn>", on_enter_usuario)
usuario.bind("<FocusOut>", on_leave_usuario)
usuario.insert(0, 'Usuario')
usuario.place(x=30, y=60)

# frame de la parte inferior de la caja de texto 1
tkinter.Frame(f1, width=295, height=2, bg='#222831').place(x=25, y=87)



# CAJA DE TEXTO 2 CON SUS FUNCIONES
contraseña = tkinter.Entry(f1, width=21, fg='#00ADB5', border=0, bg='white')
contraseña.config(font=('Microsoft YaHei UI Light', 11, ))
contraseña.bind("<FocusIn>", on_enter_contraseña)
contraseña.bind("<FocusOut>", on_leave_contraseña)
contraseña.insert(0, 'Contraseña')
contraseña.place(x=30, y=130)

# frame de la parte inferior de la caja de texto 2
tkinter.Frame(f1, width=295, height=2, bg='#222831').place(x=25, y=157)

#--------------------------------------------------------
# CREAMOS EL BOTON PARA EL INICIO DE SESION

boton_Iniciar = tkinter.Button(f1, width=39, pady=7, text='Inicia sesión',
                                bg="#00ADB5",
                                fg="#222831",
                                border=0,
                                activeforeground="#222831",
                                activebackground="#00ADB5")

boton_Iniciar.place(x=35, y=204)
boton_Iniciar.bind("<Enter>", entrar)
boton_Iniciar.bind("<Leave>", salir)

#--------------------------------------------------------
# REGISTRARSE

#ETIQUETA SI NO TIENE CUENTA

l1=tkinter.Label(f1,text="No tienes cuenta?",fg="#222831",bg='white')
l1.config(font=('Microsoft YaHei UI Light',9, ))
l1.place(x=95,y=250) 

b2=tkinter.Button(f1,width=8,text='Registrate',border=0,bg='white',fg='#00ADB5')
b2.place(x=200,y=250)


ventana.mainloop()


