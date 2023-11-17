from tkinter import *

class CajasDeTexto:
    def __init__(self, ubicacion, ancho, color1, color2, nombre, x, y):
        self.ubicacion = ubicacion
        self.ancho = ancho
        self.color1 = color1
        self.color2 = color2
        self.nombre = nombre
        self.x = x
        self.y = y

    def Caja(self):
        def on_enter(e):
            etiqueta.delete(0, 'end')

        def on_leave(e):
            if etiqueta.get() == '':
                etiqueta.insert(0, 'Usuario')

        etiqueta = StringVar()
        etiqueta = Entry(self.ubicacion,
                        width=self.ancho,
                        fg=self.color1,
                        border=0,
                        bg=self.color2,
                        )
        etiqueta.config(font=('Microsoft YaHei UI Light', 11,))
        etiqueta.bind("<FocusIn>", on_enter)
        etiqueta.bind("<FocusOut>", on_leave)
        etiqueta.insert(0, self.nombre)
        etiqueta.place(x=self.x, y=self.y)


class InicioSesion:
    def __init__(self, principal):

        self.principal = principal
        self.inicio_sesion = Frame(scn, width=925,
                                    height=500,
                                    bg='#222831')
        self.inicio_sesion.place(x=0, y=0)

        # Etiqueta "Inicia Sesion"
        self.Eti_Inicia_Sesion = Label(scn, text="Inicia sesión", fg='#00ADB5', bg='#222831')
        self.Eti_Inicia_Sesion.config(font=('Microsoft YaHei UI Light', 24, 'bold'))
        self.Eti_Inicia_Sesion.place(x=570, y=60)

        # Frame para las cajas de texto
        self.Cajas_Texto = Frame(self.inicio_sesion, width=350, height=350, bg='#222831')
        self.Cajas_Texto.place(x=480, y=100)

        # Caja 1
        self.Usuario = CajasDeTexto(self.Cajas_Texto,
                                        21,
                                        "#00ADB5",
                                        "white",
                                        "Usuario",
                                        30,
                                        130)
        self.Usuario.Caja()  # Llama al método Caja para crear la caja de texto


scn = Tk()
scn.geometry("925x500")
scn.title("Software de Control de Negocios (SCN)")
scn.config(bg='white')

inicio_sesion_obj = InicioSesion(scn)

scn.mainloop()
