import tkinter as tk
from tkinter import messagebox

# Lista para almacenar los productos
productos = []

# Función para agregar productos
def agregar_producto():
    producto = entrada_producto.get()
    if producto:
        productos.append(producto)
        entrada_producto.delete(0, tk.END)
        messagebox.showinfo("Éxito", f"Producto '{producto}' agregado correctamente.")
    else:
        messagebox.showwarning("Advertencia", "Ingrese un nombre de producto válido.")

# Función para mostrar la lista de productos
def mostrar_lista():
    if productos:
        lista_texto = "\n".join(productos)
        messagebox.showinfo("Lista de Productos", f"Lista de Productos:\n\n{lista_texto}")
    else:
        messagebox.showinfo("Lista de Productos", "La lista de productos está vacía.")

# Función para buscar productos
def buscar_producto():
    producto_a_buscar = entrada_busqueda.get()
    if producto_a_buscar:
        resultados = [producto for producto in productos if producto_a_buscar.lower() in producto.lower()]
        if resultados:
            resultados_texto = "\n".join(resultados)
            messagebox.showinfo("Resultados de Búsqueda", f"Resultados de Búsqueda:\n\n{resultados_texto}")
        else:
            messagebox.showinfo("Resultados de Búsqueda", f"No se encontraron resultados para '{producto_a_buscar}'.")
    else:
        messagebox.showwarning("Advertencia", "Ingrese un término de búsqueda válido.")

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Gestor de Productos")

# Etiqueta y entrada para agregar productos
tk.Label(ventana, text="Agregar Producto:").pack()
entrada_producto = tk.Entry(ventana)
entrada_producto.pack()
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_producto)
boton_agregar.pack()

# Separador
tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)

# Etiqueta y entrada para buscar productos
tk.Label(ventana, text="Buscar Producto:").pack()
entrada_busqueda = tk.Entry(ventana)
entrada_busqueda.pack()
boton_buscar = tk.Button(ventana, text="Buscar", command=buscar_producto)
boton_buscar.pack()

# Separador
tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)

# Botón para mostrar la lista de productos
boton_mostrar_lista = tk.Button(ventana, text="Mostrar Lista", command=mostrar_lista)
boton_mostrar_lista.pack()

# Ejecutar la aplicación
ventana.mainloop()
