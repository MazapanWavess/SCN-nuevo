# IMPORTAMOS LIBRERIAS (FALTA LA LIBRERIA SQLITE)
import tkinter
import sqlite3 

#--------------------------------------------------------
# AQUI SE PONDRA LAS FUNCIONES QUE OCUPAREMOS

#--------------------------------------------------------
# CREAMOS LA VENTANA VENTANA
ventana = tkinter.Tk()
ventana.geometry("925x500")
ventana.title("SCN")
ventana.config(bg='white')
#--------------------------------------------------------
# AQUI SE PONDRA LA TABLAS PARA LA BASE DE DATOS

#--------------------------------------------------------
#Aqui se debe poner la imagen


#--------------------------------------------------------
# ETIQUETAS Y CAJAS DE TEXTO INICIO DE SESION

# ETIQUETA 1
l2=tkinter.Label(ventana,text="Inicia sesión",fg='#00ADB5',bg='white')
l2.config(font=('Microsoft YaHei UI Light',24, 'bold'))
l2.place(x=570,y=60)

# FRAME PARA LAS CAJAS DE TEXTO
f1=tkinter.Frame(ventana,width=350,height=350,bg='white')
f1.place(x=480,y=100)

# FUNCIONES PARA LAS CAJAS DE TEXTO
def on_enter(e):
    usuario.delete(0,'end')    
def on_leave(e):
    if usuario.get()=='':   
        usuario.insert(0,'Usuario')

# CAJA 1 CON SUS FUNCIONES
usuario = tkinter.Entry(f1,width=25,fg='#00ADB5',border=0,bg='white')
usuario.config(font=('Microsoft YaHei UI Light',11, ))
usuario.bind("<FocusIn>", on_enter) # Se activa cuando el foco de la ventana se establece
usuario.bind("<FocusOut>", on_leave) # Se activa cuando el foco de la ventana se pierde
usuario.insert(0,'Usuario')
usuario.place(x=30,y=60)

# frame de la parte inferior de la caja de texto 1
tkinter.Frame(f1,width=295,height=2,bg='#222831').place(x=25,y=87)

# LAS MISMAS FUNCIONES DE LA CAJA DE TEXTO "usuarios" PARA LA CAJA DE TEXTO "contraseña"
def on_enter(e):
    contraseña.delete(0,'end')    
def on_leave(e):
    if contraseña.get()=='':   
        contraseña.insert(0,'Contraseña')

# CAJA DE TEXTO 2 CON SUS FUNCIONES
contraseña =tkinter.Entry(f1,width=21,fg='#00ADB5',border=0,bg='white')
contraseña.config(font=('Microsoft YaHei UI Light',11, ))
contraseña.bind("<FocusIn>", on_enter)
contraseña.bind("<FocusOut>", on_leave)
contraseña.insert(0,'Contraseña')
contraseña.place(x=30,y=130)

# frame de la parte inferior de la caja de texto 2

tkinter.Frame(f1,width=295,height=2,bg='#222831').place(x=25,y=157)

#--------------------------------------------------------
# CREAMOS EL BOTON PARA EL INICIO DE SESION

tkinter.Button(f1,width=39,pady=7,text='Inicia sesión',bg='#393E46',fg='#00ADB5',border=0).place(x=35,y=204)


ventana.mainloop()