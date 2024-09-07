from tkinter import *
from tkinter import messagebox


def login():
    usuario = entrada1.get()
    senha=entrada2.get()

    if (usuario=="" and senha==""):
        messagebox.showinfo("", "Acesso Negado")
    elif (usuario=="Gabriel" and senha=="admin"):
        messagebox.showinfo("","Login autorizado")
    else:
        messagebox.showinfo("", "Usuário e Senha incorretos")
root=Tk()
root.title('Login')
root.geometry("300x200")

global entrada1
global entrada2

Label(root, text="Usuário").place(x=20, y=20)
Label(root, text="Senha").place(x=20, y=70)

entrada1=Entry(root, bd=5)
entrada1.place(x=140, y=20)

entrada2=Entry(root, bd=5)
entrada2.place(x=140, y=70)

Button(root, text="Login", command=login, height=3, width=13, bd=6).place(x=100, y=120)
root.mainloop()