from tkinter import *
janela = Tk()
janela.title("aqui temos uma janela")
janela.geometry('420x420')
label = Label(janela,text="aqui temos um texto",font=('arial',20,'bold'),fg='green')
label.pack()
janela.mainloop()
