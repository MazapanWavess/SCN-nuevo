# Modulos
from tkinter import *
import sqlite3
from tkinter import messagebox
from PIL import ImageTk,Image


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

#--------------------------------------------------------------------------------------------------------------

class BotonesDiferentes:
    def __init__(self,ubicacion,ancho,TamañoLetra,texto,color1,color2,x,y,comando):
        
        self.ubicacion  = ubicacion
        self.ancho = ancho
        self.TamañoLetra = TamañoLetra
        self.texto = texto
        self.color1 = color1
        self.color2 = color2
        self.x = x
        self.y = y
        self.comando = comando

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
                        activebackground=self.color2,
                        command=self.comando)
        Boton.place(x=self.x, y=self.y)
        Boton.bind("<Enter>", entrar)
        Boton.bind("<Leave>", salir)

#--------------------------------------------------------------------------------------------------------------
class Home:
    def __init__(self):
        

        self.home = Frame(scn,width=925,
                            height=500,
                            bg="#222831")
        self.home.place(x=0,y=0)

        self.home2 = Frame(self.home,width=925,
                            height=460,
                            bg="#393E46")
        self.home2.place(x=0,y=40)


        self.boton_home = BotonesDiferentes(self.home,
                                            5,
                                            3,
                                            "M",
                                            "#222831",#2d3541
                                            '#00ADB5',
                                            5,
                                            8,
                                            Menu,)
        self.boton_home.Botones()

        self.eti_agregar_producto = Label(self.home,
                                            text="Inicio",
                                            fg="#EEEEEE",
                                            bg="#222831")
        self.eti_agregar_producto.place(x=50,y=4)
        self.eti_agregar_producto.config(font=('Microsoft YaHei UI Light', 15))


#--------------------------------------------------------------------------------------------------------------
class Menu:
    def __init__(self):
        
        def quitar_menu():
            self.menu.destroy()

        self.menu = Frame(scn,width=300,
                            height=500,
                            bg="#00ADB5")
        self.menu.place(x=0,y=0)

        self.quitar_menu = Button(self.menu,
                                    text="X",
                                    command=quitar_menu)
        self.quitar_menu.place(x=5,y=8)

        self.boton_home = BotonesDiferentes(self.menu,
                                            5,
                                            3,
                                            "X",
                                            "#00ADB5",#00ADB5
                                            '#222831',
                                            5,
                                            8,
                                            quitar_menu,)
        self.boton_home.Botones()

        # BOTON 1 (HOME)
        self.boton_home = BotonesDiferentes(self.menu,
                                            42,
                                            10,
                                            "H O M E",
                                            "#00ADB5",
                                            '#2d3541',
                                            0,
                                            80,
                                            Home)
        self.boton_home.Botones()

        # BOTON 2 (AGREGAR PRODUCTO)
        self.boton_Agregar_Producto = BotonesDiferentes(self.menu,
                                            42,
                                            10,
                                            "AGREGAR PRODUCTO",
                                            "#00ADB5",
                                            '#2d3541',
                                            0,
                                            117,
                                            AgregarProducto)
        self.boton_Agregar_Producto.Botones()

        # BOTON 3 (LISTA DE PRODUCTOS PRODUCTO)
        self.boton_lista_Productos = BotonesDiferentes(self.menu,
                                            42,
                                            10,
                                            "LISTA DE PRODUCTOS",
                                            "#00ADB5",
                                            '#2d3541',
                                            0,
                                            157,
                                            ListaProductos)
        self.boton_lista_Productos.Botones()

        # BOTON 4 (BUSCAR PRODUCTO)
        self.boton_buscar_producto = BotonesDiferentes(self.menu,
                                            42,
                                            10,
                                            "BUSCAR PRODUCTO",
                                            "#00ADB5",
                                            '#2d3541',
                                            0,
                                            191,
                                            BuscarProductos)
        self.boton_buscar_producto.Botones()

        # BOTON 5 (REGISTAR VENTA DE PRODUCTO)
        self.boton_registrar_venta = BotonesDiferentes(self.menu,
                                            42,
                                            10,
                                            "REGISTRAR VENTA",
                                            "#00ADB5",
                                            '#2d3541',
                                            0,
                                            228,
                                            RegistrarVenta)
        self.boton_registrar_venta.Botones()

        # BOTON 6 (VER VENTAS DEL DIA)
        self.boton_ventas_dia = BotonesDiferentes(self.menu,
                                            42,
                                            10,
                                            "VENTAS DEL DIA",
                                            "#00ADB5",
                                            '#2d3541',
                                            0,
                                            265,
                                            VentasDelDia)
        self.boton_ventas_dia.Botones()

        # BOTON 7 (VER VENTAS DE DIAS ANTERIORES)
        self.boton_ventas_anteriores = BotonesDiferentes(self.menu,
                                            42,
                                            10,
                                            "VENTAS ANTERIORES",
                                            "#00ADB5",
                                            '#2d3541',
                                            0,
                                            302,
                                            VentasAnteriores)
        self.boton_ventas_anteriores.Botones()

        # BOTON 8 (AYUDA)
        self.boton_ayuda = BotonesDiferentes(self.menu,
                                            42,
                                            10,
                                            " A Y U D A ",
                                            "#00ADB5",
                                            '#2d3541',
                                            0,
                                            463,
                                            NONE)
        self.boton_ayuda.Botones()


#--------------------------------------------------------------------------------------------------------------
class AgregarProducto:
    def __init__(self):
        
        self.agregar_producto = Frame(scn,width=925,
                            height=500,
                            bg="#222831")
        self.agregar_producto.place(x=0,y=0)

        self.agregar_producto2 = Frame(self.agregar_producto,width=925,
                            height=460,
                            bg="#393E46")
        self.agregar_producto2.place(x=0,y=40)

        self.boton_home = BotonesDiferentes(self.agregar_producto,
                                            5,
                                            3,
                                            "M",
                                            "#222831",#2d3541
                                            '#00ADB5',
                                            5,
                                            8,
                                            Menu,)
        self.boton_home.Botones()

        self.eti_agregar_producto = Label(self.agregar_producto,
                                            text="Agregar Producto",
                                            fg="#EEEEEE",
                                            bg="#222831")
        self.eti_agregar_producto.place(x=50,y=4 )
        self.eti_agregar_producto.config(font=('Microsoft YaHei UI Light', 15))

#--------------------------------------------------------------------------------------------------------------
class ListaProductos:
    def __init__(self):
        
        self.lista_producto = Frame(scn,width=925,
                            height=500,
                            bg="#222831")
        self.lista_producto.place(x=0,y=0)

        self.lista_producto2 = Frame(self.lista_producto,width=925,
                            height=460,
                            bg="#393E46")
        self.lista_producto2.place(x=0,y=40)

        self.boton_home = BotonesDiferentes(self.lista_producto,
                                            5,
                                            3,
                                            "M",
                                            "#222831",#2d3541
                                            '#00ADB5',
                                            5,
                                            8,
                                            Menu,)
        self.boton_home.Botones()

        self.eti_lista_producto = Label(self.lista_producto,
                                            text="Lista De Productos",
                                            fg="#EEEEEE",
                                            bg="#222831")
        self.eti_lista_producto.place(x=50,y=4 )
        self.eti_lista_producto.config(font=('Microsoft YaHei UI Light', 15))

#--------------------------------------------------------------------------------------------------------------
class BuscarProductos:
    def __init__(self):
        
        self.buscar_producto = Frame(scn,width=925,
                            height=500,
                            bg="#222831")
        self.buscar_producto.place(x=0,y=0)

        self.buscar_producto2 = Frame(self.buscar_producto,width=925,
                            height=460,
                            bg="#393E46")
        self.buscar_producto2.place(x=0,y=40)

        self.boton_home = BotonesDiferentes(self.buscar_producto,
                                            5,
                                            3,
                                            "M",
                                            "#222831",#2d3541
                                            '#00ADB5',
                                            5,
                                            8,
                                            Menu,)
        self.boton_home.Botones()

        self.eti_buscar_producto = Label(self.buscar_producto,
                                            text="Buscar Productos",
                                            fg="#EEEEEE",
                                            bg="#222831")
        self.eti_buscar_producto.place(x=50,y=4 )
        self.eti_buscar_producto.config(font=('Microsoft YaHei UI Light', 15))

#--------------------------------------------------------------------------------------------------------------
class RegistrarVenta:
    def __init__(self):
        
        self.registra_venta = Frame(scn,width=925,
                            height=500,
                            bg="#222831")
        self.registra_venta.place(x=0,y=0)

        self.registra_venta2 = Frame(self.registra_venta,width=925,
                            height=460,
                            bg="#393E46")
        self.registra_venta2.place(x=0,y=40)

        self.boton_home = BotonesDiferentes(self.registra_venta,
                                            5,
                                            3,
                                            "M",
                                            "#222831",#2d3541
                                            '#00ADB5',
                                            5,
                                            8,
                                            Menu,)
        self.boton_home.Botones()

        self.eti_registrar_venta = Label(self.registra_venta,
                                            text="Registrar Venta",
                                            fg="#EEEEEE",
                                            bg="#222831")
        self.eti_registrar_venta.place(x=50,y=4 )
        self.eti_registrar_venta.config(font=('Microsoft YaHei UI Light', 15))

#--------------------------------------------------------------------------------------------------------------
class VentasDelDia:
    def __init__(self):
        
        self.ventas_del_dia = Frame(scn,width=925,
                            height=500,
                            bg="#222831")
        self.ventas_del_dia.place(x=0,y=0)

        self.ventas_del_dia2 = Frame(self.ventas_del_dia,width=925,
                            height=460,
                            bg="#393E46")
        self.ventas_del_dia2.place(x=0,y=40)

        self.boton_home = BotonesDiferentes(self.ventas_del_dia,
                                            5,
                                            3,
                                            "M",
                                            "#222831",#2d3541
                                            '#00ADB5',
                                            5,
                                            8,
                                            Menu,)
        self.boton_home.Botones()

        self.eti_ventas_del_dia = Label(self.ventas_del_dia,
                                            text="Ventas Del Dia",
                                            fg="#EEEEEE",
                                            bg="#222831")
        self.eti_ventas_del_dia.place(x=50,y=4 )
        self.eti_ventas_del_dia.config(font=('Microsoft YaHei UI Light', 15))

#--------------------------------------------------------------------------------------------------------------
class VentasAnteriores:
    def __init__(self):
        
        self.ventas_anteriores = Frame(scn,width=925,
                            height=500,
                            bg="#222831")
        self.ventas_anteriores.place(x=0,y=0)

        self.ventas_anteriores2 = Frame(self.ventas_anteriores,width=925,
                            height=460,
                            bg="#393E46")
        self.ventas_anteriores2.place(x=0,y=40)

        self.boton_home = BotonesDiferentes(self.ventas_anteriores,
                                            5,
                                            3,
                                            "M",
                                            "#222831",#2d3541
                                            '#00ADB5',
                                            5,
                                            8,
                                            Menu,)
        self.boton_home.Botones()

        self.eti_ventas_anteriores = Label(self.ventas_anteriores,
                                            text="Ventas Anteriores",
                                            fg="#EEEEEE",
                                            bg="#222831")
        self.eti_ventas_anteriores.place(x=50,y=4 )
        self.eti_ventas_anteriores.config(font=('Microsoft YaHei UI Light', 15))



#--------------------------------------------------------------------------------------------------------------

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
                                                    264,
                                                    None)
        self.boton_registrarse.Botones()

        # Etiqueta Para llevar a inicio de sesion
        self.l1=Label(self.cajas_registrar,text="Ya tienes una cuenta?",fg="white",bg='#222831')
        self.l1.config(font=('Microsoft YaHei UI Light',9, ))
        self.l1.place(x=73,y=313)

        self.regresar=Button(self.cajas_registrar,
                        width=9,
                        text='Iniciar Sesion',
                        border=0,
                        bg='#222831',
                        fg='#00ADB5',
                        command=self.registra_cuenta.destroy)
        self.regresar.place(x=200,y=313)

#--------------------------------------------------------------------------------------------------------------

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
                                                    204,
                                                    Home)
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