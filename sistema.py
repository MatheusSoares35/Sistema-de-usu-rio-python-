from tkinter import *
import user


window = Tk()
window.geometry("550x500")
window.title("aqui temo uma janela")
window.configure(bg="#a08811")
t1 = Label(window, text="aqui temos uma interface",fg="#854c18",bg='#f08811')
buton = Button(window, text="Botão da interface",
               command=user.teste
               )
buton.pack()
t1.pack()

window.mainloop()