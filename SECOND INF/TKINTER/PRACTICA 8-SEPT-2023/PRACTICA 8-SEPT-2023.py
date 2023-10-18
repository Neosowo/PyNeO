from tkinter import *

def convertidor():
    n = float(input.get())
    km = n * 1.60
    Label3.config(text=km)

root = Tk()
root.title("Conversor milla a km")
root.minsize(width=300, height=290)

canvas = Canvas(width=155, height=155)
imagen = PhotoImage(file="Second inf programs/TKINTER/PRACTICA 8-SEPT-2023/logo.png")
canvas.create_image(0, 0, anchor=NW, image=imagen)
canvas.grid(column=1, row=0)


input = Entry(width=10, font=("Times New Roman", 14))
input.insert(END, string="0")
input.grid(column=1, row=1)

Label1 = Label(text="Millas", font=("Times New Roman", 14))
Label1.grid(column=2, row=1)

Label2 = Label(text="Es igual a: ", font=("Times New Roman", 14))
Label2.grid(column=0, row=2)

Label3 = Label(text="0", font=("Times New Roman", 14))
Label3.grid(column=1, row=2)

Label4 = Label(text="Km", font=("Times New Roman", 14))
Label4.grid(column=2, row=2)

button = Button(text="Calcular", font=("Times New Roman", 14), command=convertidor)
button.grid(column=1, row=3)



root.mainloop()