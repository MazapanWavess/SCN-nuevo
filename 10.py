from tkinter import *

ventana = Tk()
ventana.geometry("900x500")
ventana.config(bg="white")

def ventana_vocales():
    VentanaVocales = Toplevel()
    VentanaVocales.geometry("900x500")
    VentanaVocales.title("Ventana Vocales")
    VentanaVocales.config(bg="blue")

def ventana_palabras():
    VentanaPalabras = Toplevel()
    VentanaPalabras.geometry("900x500")
    VentanaPalabras.title("Ventana Vocales")
    VentanaPalabras.config(bg="blue")


def ventana_secundaria():
    ventana2 = Toplevel()
    ventana2.geometry("900x500")
    ventana2.title("ventana secundaria")
    ventana2.config(bg="black")


    nombre = caja_nombre.get()

    etiqueta_bienvenida = Label(ventana2,text="Bienvenido "+ nombre)
    etiqueta_bienvenida.config(bg="white")
    etiqueta_bienvenida.pack()

    vocales = Button(ventana2,
                        width=40,
                        pady=7,
                        text="V O C A L E S",
                        command=ventana_vocales)
    vocales.pack()

    palabras_basicas = Button(ventana2,
                        width=40,
                        pady=7,
                        text="P A L A B R A S  B A S I C A S",
                        command=ventana_palabras)
    palabras_basicas.pack()


Etiqueta = Label(ventana,text="Escribe tu nombre:")
Etiqueta.pack()

caja_nombre = Entry(ventana)
caja_nombre.pack()

boton_llamar_ventana = Button(ventana,
                                width=39,
                                pady=7,
                                text="CAmbiar ventana",
                                command=ventana_secundaria)
boton_llamar_ventana.pack()
ventana.mainloop()