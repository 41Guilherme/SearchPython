from tkinter import *
import webbrowser

win = Tk()
win.title("Pesquisa Rápida")

label1 = Label(win, text='Insira URL Aqui:  ',font=('arial',10,'bold'))
label1.grid(row=0,column=0)

entry =Entry(win,width=30)
entry.grid(row=0,column=1)


def pesquisar():
    url = entry.get()
    webbrowser.open(url)


button = Button(win,text="PESQUISAR", command=pesquisar)
button.grid(row=1,column=0,pady=10,columnspan=2)

win.mainloop()
