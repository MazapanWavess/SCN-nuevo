from tkinter import *
w = Tk()
w.geometry("300x500")
w.config(bg="#141414")

def bttn(x,y,text,bcolor,fcolor,cmd):

    def on_enter(e):
        mybutton["background"]=bcolor
        mybutton["foreground"]=fcolor

    def on_leave(e):
        mybutton["background"]=fcolor
        mybutton["foreground"]=bcolor

    mybutton=Button(w,width=42,height=2,text=text,
                    fg=bcolor,
                    bg=fcolor,
                    border=0,
                    activeforeground=fcolor,
                    activebackground=bcolor,
                    command=cmd,)
    
    mybutton.bind("<Enter>",on_enter)
    mybutton.bind("<Leave>",on_leave)

    mybutton.place(x=x,y=y)
    
    

def cmd():
    print("you clicked A C E R")

def cmd1():
    print("you clicked A P P L E")

def cmd2():
    print("you clicked D E L L")

def cmd3():
    print("you clicked A S U S")



bttn(0,0,"A C E R","#ffcc66","#141414",cmd)
bttn(0,37,"A P P L E","#25dae9","#141414",cmd1)
bttn(0,74,"D E L L","#f86263","#141414",cmd2)
bttn(0,110,"A S U S","#ffa157","#141414",cmd3)

w.mainloop() 
