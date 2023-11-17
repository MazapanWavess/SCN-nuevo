from tkinter import *

class CajasDeTexto:
    def __init__(self, ubicacion, ancho, color1, color2, nombre, x, y, texto):
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
            etiqueta.delete(0, 'end')

        def on_leave(e):
            if etiqueta.get() == '':
                etiqueta.insert(0, self.texto)

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

class BotonesDiferentes:
    def __init__(self, ubicacion, ancho, TamañoLetra, texto, color1, color2, x, y, command=None):
        self.ubicacion = ubicacion
        self.ancho = ancho
        self.TamañoLetra = TamañoLetra
        self.texto = texto
        self.color1 = color1
        self.color2 = color2
        self.x = x
        self.y = y
        self.command = command

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
                       command=self.command)  # Cambia la línea aquí
        Boton.place(x=self.x, y=self.y)
        Boton.bind("<Enter>", entrar)
        Boton.bind("<Leave>", salir)

class PaginaRegistro(Frame):
    def __init__(self, master, volver_a_inicio):
        super().__init__(master, bg="#222831")
        self.master = master
        self.volver_a_inicio = volver_a_inicio

        # Resto del código para la página de registro

        self.boton_volver = BotonesDiferentes(self, 39, 7, "Volver a Inicio", '#222831', '#00ADB5', 35, 264, command=self.volver_a_inicio)
        self.boton_volver.Botones()

class PaginaInicioSesion(Frame):
    def __init__(self, master, mostrar_registro):
        super().__init__(master, bg='#222831')
        self.master = master
        self.mostrar_registro = mostrar_registro

        # Resto del código para la página de inicio de sesión

        self.boton_registro = BotonesDiferentes(self, 39, 7, "Registrarse", "#00ADB5", "#2d3541", 35, 204, command=self.mostrar_registro)
        self.boton_registro.Botones()

class Aplicacion:
    def __init__(self, master):
        self.master = master
        self.pagina_inicio_sesion = PaginaInicioSesion(self.master, self.mostrar_registro)
        self.pagina_registro = PaginaRegistro(self.master, self.mostrar_inicio_sesion)
        self.pagina_actual = None

        self.mostrar_inicio_sesion()

    def mostrar_registro(self):
        if self.pagina_actual:
            self.pagina_actual.pack_forget()
        self.pagina_actual = self.pagina_registro
        self.pagina_actual.pack(fill='both', expand=True)

    def mostrar_inicio_sesion(self):
        if self.pagina_actual:
            self.pagina_actual.pack_forget()
        self.pagina_actual = self.pagina_inicio_sesion
        self.pagina_actual.pack(fill='both', expand=True)

if __name__ == "__main__":
    scn = Tk()
    scn.geometry("925x500")
    scn.title("Software de Control de Negocios (SCN)")
    scn.config(bg='white')

    app = Aplicacion(scn)

    scn.mainloop()
