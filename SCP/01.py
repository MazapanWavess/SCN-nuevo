from tkinter import *
from PIL import ImageTk, Image

class ToggleMenuApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry('900x500')
        self.master.configure(bg='#262626')  # 12c4c0')
        self.master.resizable(0, 0)
        self.master.title('Toggle Menu')

        self.img1 = ImageTk.PhotoImage(Image.open(r"F:\03_Codigos_Prueba\02 ventanas pruebas\imagenes\open.png"))
        self.img2 = ImageTk.PhotoImage(Image.open(r"F:\03_Codigos_Prueba\02 ventanas pruebas\imagenes\close.png"))

        self.b2 = Button(self.master, image=self.img1, command=self.toggle_win, border=0, bg='#262626',
                            activebackground='#262626')
        self.b2.place(x=5, y=8)

        self.default_home()

        self.master.mainloop()

    def default_home(self):
        f2 = Frame(self.master, width=900, height=455, bg='#262626')
        f2.place(x=0, y=45)
        l2 = Label(f2, text='Home', fg='white', bg='#262626')
        l2.config(font=('Comic Sans MS', 90))
        l2.place(x=290, y=150 - 45)

    def home(self):
        self.f1.destroy()
        f2 = Frame(self.master, width=900, height=455, bg='#262626')
        f2.place(x=0, y=45)
        l2 = Label(f2, text='Home', fg='white', bg='#262626')
        l2.config(font=('Comic Sans MS', 90))
        l2.place(x=290, y=150 - 45)
        self.toggle_win()

    def acer(self):
        self.f1.destroy()
        f2 = Frame(self.master, width=900, height=455, bg='white')
        f2.place(x=0, y=45)
        l2 = Label(f2, text='Acer', fg='black', bg='white')
        l2.config(font=('Comic Sans MS', 90))
        l2.place(x=290, y=150 - 45)
        self.toggle_win()

    def dell(self):
        self.f1.destroy()
        f2 = Frame(self.master, width=900, height=455, bg='white')
        f2.place(x=0, y=45)
        l2 = Label(f2, text='Dell', fg='black', bg='white')
        l2.config(font=('Comic Sans MS', 90))
        l2.place(x=320, y=150 - 45)
        self.toggle_win()

    def toggle_win(self):
        self.f1 = Frame(self.master, width=300, height=500, bg='#12c4c0')
        self.f1.place(x=0, y=0)

        def bttn(x, y, text, bcolor, fcolor, cmd):
            def on_entera(e):
                myButton1['background'] = bcolor
                myButton1['foreground'] = '#262626'

            def on_leavea(e):
                myButton1['background'] = fcolor
                myButton1['foreground'] = '#262626'

            myButton1 = Button(self.f1, text=text,
                               width=42,
                               height=2,
                               fg='#262626',
                               border=0,
                               bg=fcolor,
                               activeforeground='#262626',
                               activebackground=bcolor,
                               command=cmd)

            myButton1.bind("<Enter>", on_entera)
            myButton1.bind("<Leave>", on_leavea)

            myButton1.place(x=x, y=y)

        bttn(0, 80, 'H O M E', '#0f9d9a', '#12c4c0', self.home)
        bttn(0, 117, 'A C E R', '#0f9d9a', '#12c4c0', self.acer)
        bttn(0, 154, 'D E L L', '#0f9d9a', '#12c4c0', self.dell)
        bttn(0, 191, 'A S U S', '#0f9d9a', '#12c4c0', None)
        bttn(0, 228, 'A P P L E', '#0f9d9a', '#12c4c0', None)
        bttn(0, 265, 'A C E R', '#0f9d9a', '#12c4c0', None)

        def dele():
            self.f1.destroy()
            b2 = Button(self.master, image=self.img1, command=self.toggle_win, border=0, bg='#262626',
                        activebackground='#262626')
            b2.place(x=5, y=8)

        Button(self.f1, image=self.img2, border=0, command=dele, bg='#12c4c0', activebackground='#12c4c0').place(x=5, y=10)


if __name__ == "__main__":
    app = ToggleMenuApp(Tk())
