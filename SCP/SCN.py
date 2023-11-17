# Modulos
from tkinter import *
import sqlite3
from tkinter import messagebox

# Tablas bases de datos



# Ventana principal

scn = Tk()
scn.geometry("925x500")
scn.title("Sofware de Control de Negocios (SCN)")
scn.config(bg='white')


# Clases
class CajasDeTexto:
    def __init__(self,ubicacion,ancho,color1,color2,nombre,x,y,texto):
        
        self.ubicacion = ubicacion
        self.ancho = ancho
        self.color1 = color1
        self.color2 = color2
        self.nombre = nombre
        self.x = x
        self.y = y
        self.texto = texto

    def Caja(self):

        def on_enter(e):
            etiqueta.delete(0,'end')    
        def on_leave(e):
            if etiqueta.get()=='':   
                etiqueta.insert(0,self.texto)
        
        etiqueta = StringVar()
        etiqueta=Entry(self.ubicacion,
                        width=self.ancho,
                        fg=self.color1,
                        border=0,
                        bg=self.color2,
                        )
        etiqueta.config(font=('Microsoft YaHei UI Light',11,))
        etiqueta.bind("<FocusIn>",on_enter)
        etiqueta.bind("<FocusOut>",on_leave)
        etiqueta.insert(0,self.nombre)
        etiqueta.place(x=self.x,y=self.y)

#--------------------------------------------------------

class BotonesDiferentes:
    def __init__(self,ubicacion,ancho,TamañoLetra,texto,color1,color2,x,y):
        
        self.ubicacion  = ubicacion
        self.ancho = ancho
        self.TamañoLetra = TamañoLetra
        self.texto = texto
        self.color1 = color1
        self.color2 = color2
        self.x = x
        self.y = y

    def Botones(self):

        def entrar(e):
            Boton["background"] = self.color2
            Boton["foreground"] = self.color1

        def salir(e):   
            Boton["background"] = self.color1
            Boton["foreground"] = self.color2
        
        Boton = Button(self.ubicacion,
                        width=self.ancho,
                        pady=self.TamañoLetra,
                        text=self.texto,
                        bg=self.color1,
                        fg=self.color2,
                        border=0,
                        activeforeground=self.color1,
                        activebackground=self.color2)
        Boton.place(x=self.x, y=self.y)
        Boton.bind("<Enter>", entrar)
        Boton.bind("<Leave>", salir)

#--------------------------------------------------------
class RegistrarCuenta:
    def __init__(self):

        # Frames Para registrarse
        self.registra_cuenta = Frame(scn,width=925,
                                    height=500,
                                    bg="#222831")
        self.registra_cuenta.place(x=0,y=0)
        
        #Frame para Cajas de texto registrarse
        self.cajas_registrar = Frame(self.registra_cuenta,
                                        width=350,
                                        height=350,
                                        bg="#222831")
        self.cajas_registrar.place(x=480,y=70)

        #Etiqueta "Registrarse"
        self.Etiqueta_Registrarse = Label(self.registra_cuenta,
                                            text="Registrarse",
                                            fg="#00ADB5",
                                            bg="#222831")
        self.Etiqueta_Registrarse.config(font=('Microsoft YaHei UI Light',23, 'bold'))
        self.Etiqueta_Registrarse.place(x=575,y=60)

        # Caja 1 (Usuario)
        self.Usuario = CajasDeTexto(self.cajas_registrar,
                                21,
                                "#00ADB5",
                                "#222831",
                                "Usuario",
                                30,
                                60,
                                "Usuario")
        self.Usuario.Caja()
        Frame(self.cajas_registrar,width=295,height=2,bg='white').place(x=25,y=87)

        # Caja 2 (Contraseña)
        self.Contraseña = CajasDeTexto(self.cajas_registrar,
                                21,
                                "#00ADB5",
                                "#222831",
                                "Contraseña",
                                30,
                                130,
                                "Contraseña")
        self.Contraseña.Caja()
        Frame(self.cajas_registrar,width=295,height=2,bg='white').place(x=25,y=157)

        # Caja 3 (Confirmar Contraseña)
        self.conf_contraseña = CajasDeTexto(self.cajas_registrar,
                                21,
                                "#00ADB5",
                                "#222831",
                                "Confirmar Contraseña",
                                30,
                                130+70,
                                "Confirmar Contraseña")
        self.conf_contraseña.Caja()
        Frame(self.cajas_registrar,width=295,height=2,bg='white').place(x=25,y=157+70)

        # Boton 1 (Registrarse)
        self.boton_registrarse = BotonesDiferentes(self.cajas_registrar,
                                                    39,
                                                    7,
                                                    "Registrarse",
                                                    "#00ADB5",
                                                    "#2d3541",
                                                    35,
                                                    264)
        self.boton_registrarse.Botones()

        # Etiqueta Para llevar a inicio de sesion
        self.l1=Label(self.cajas_registrar,text="Ya tienes una cuenta",fg="white",bg='#222831')
        self.l1.config(font=('Microsoft YaHei UI Light',9, ))
        self.l1.place(x=70,y=313)

        self.regresar=Button(self.cajas_registrar,
                        width=9,
                        text='Iniciar Sesion',
                        border=0,
                        bg='#222831',
                        fg='#00ADB5',
                        command=inicio_sesion_obj)
        self.regresar.place(x=210,y=313)

#--------------------------------------------------------

class InicioSesion:
    def __init__(self,principal):

        self.principal = principal
        self.inicio_sesion = Frame(scn,width=925,
                                height=500,
                                bg='#222831')
        self.inicio_sesion.place(x=0,y=0)

        # Etiqueta "Inicia Sesion"
        self.Eti_Inicia_Sesion = Label(scn,text="Inicia sesión", fg='#00ADB5', bg='#222831')
        self.Eti_Inicia_Sesion.config(font=('Microsoft YaHei UI Light', 24, 'bold'))
        self.Eti_Inicia_Sesion.place(x=570, y=60)

        # Frame para las cajas de texto
        self.Cajas_Texto=Frame(self.inicio_sesion,width=350,height=350,bg='#222831')
        self.Cajas_Texto.place(x=480,y=100)

        # Caja 1 (Usuario)
        self.Usuario = CajasDeTexto(self.Cajas_Texto,
                                21,
                                "#00ADB5",
                                "#222831",
                                "Usuario",
                                30,
                                60,
                                "Usuario")
        self.Usuario.Caja()
        Frame(self.Cajas_Texto, width=295, height=2, bg='WHITE').place(x=25, y=87)


        # Caja 2 (Contraseña)
        self.Contraseña = CajasDeTexto(self.Cajas_Texto,
                                21,
                                "#00ADB5",
                                "#222831",
                                "Contraseña",
                                30,
                                130,
                                "Contraseña")
        self.Contraseña.Caja()
        Frame(self.Cajas_Texto,width=295,height=2,bg='white').place(x=25,y=157)


        # Boton 1 (Inicio de sesion)
        self.boton_inicio_sesion = BotonesDiferentes(self.Cajas_Texto,
                                                    39,
                                                    7,
                                                    "Inicia Sesion",
                                                    "#00ADB5",
                                                    "#2d3541",
                                                    35,
                                                    204)
        self.boton_inicio_sesion.Botones()

        #imagen
        self.img1 = PhotoImage(file=(r"F:\04_Proyecto\scn nuevo\SCN-nuevo\01.png"))
        Label(self.inicio_sesion,image=self.img1,border=0,bg='#222831').place(x=50,y=50)

        # Etiqueta si no tiene cuenta (Registrarse)
        self.l1=Label(self.Cajas_Texto,text="No tienes cuenta?",fg="white",bg='#222831')
        self.l1.config(font=('Microsoft YaHei UI Light',9, ))
        self.l1.place(x=95,y=250)

        self.b2=Button(self.Cajas_Texto,
                        width=8,
                        text='Registrate',
                        border=0,
                        bg='#222831',
                        fg='#00ADB5',
                        command=RegistrarCuenta)
        self.b2.place(x=200,y=250)


inicio_sesion_obj = InicioSesion(scn)


scn.mainloop()