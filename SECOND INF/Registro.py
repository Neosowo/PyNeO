import tkinter as tk
from tkinter import messagebox
owo = tk.Tk()
owo.title("Registro")
owo.minsize(width=150, height=150)


tk.Label(
    owo,
    text="1"
).grid(row=1, column=0)
tk.Label(
    owo,
    text="2"
).grid(row=2, column=0)
tk.Label(
    owo,
    text="3"
).grid(row=3, column=0)
tk.Label(
    owo,
    text="4"
).grid(row=4, column=0)
tk.Label(
    owo,
    text="5"
).grid(row=5, column=0)
tk.Label(
    owo,
    text="6"
).grid(row=6, column=0)
tk.Label(
    owo,
    text="Cantidad",
).grid(row=0, column=1)
tk.Label(
    owo,
    text="Detalle",
).grid(row=0, column=2)
tk.Label(
    owo,
    text="Cost. U.",
).grid(row=0, column=3)
tk.Label(
    owo,
    text="P.V.U",
).grid(row=0, column=4)
tk.Label(
    owo,
    text="M.C.U",
).grid(row=0, column=5)
CANT1 = tk.Entry(owo)
CANT1.grid(row=1, column=1)

CANT2 = tk.Entry(owo)
CANT2.grid(row=2, column=1)

CANT3 = tk.Entry(owo)
CANT3.grid(row=3, column=1)

CANT4 = tk.Entry(owo)
CANT4.grid(row=4, column=1)

CANT5 = tk.Entry(owo)
CANT5.grid(row=5, column=1)

CANT6 = tk.Entry(owo)
CANT6.grid(row=6, column=1)

DETAIL1 = tk.Entry(owo)
DETAIL1.grid(row=1, column=2)

DETAIL2 = tk.Entry(owo)
DETAIL2.grid(row=2, column=2)

DETAIL3 = tk.Entry(owo)
DETAIL3.grid(row=3, column=2)

DETAIL4 = tk.Entry(owo)
DETAIL4.grid(row=4, column=2)

DETAIL5 = tk.Entry(owo)
DETAIL5.grid(row=5, column=2)

DETAIL6 = tk.Entry(owo)
DETAIL6.grid(row=6, column=2)

COSTU1 = tk.Entry(owo)
COSTU1.grid(row=1, column=3)

COSTU2 = tk.Entry(owo)
COSTU2.grid(row=2, column=3)

COSTU3 = tk.Entry(owo)
COSTU3.grid(row=3, column=3)

COSTU4 = tk.Entry(owo)
COSTU4.grid(row=4, column=3)

COSTU5 = tk.Entry(owo)
COSTU5.grid(row=5, column=3)

COSTU6 = tk.Entry(owo)
COSTU6.grid(row=6, column=3)

PVU1 = tk.Entry(owo)
PVU1.grid(row=1, column=4)

PVU2 = tk.Entry(owo)
PVU2.grid(row=2, column=4)

PVU3 = tk.Entry(owo)
PVU3.grid(row=3, column=4)

PVU4 = tk.Entry(owo)
PVU4.grid(row=4, column=4)

PVU5 = tk.Entry(owo)
PVU5.grid(row=5, column=4)

PVU6 = tk.Entry(owo)
PVU6.grid(row=6, column=4)

MCU1 = tk.Entry(owo)
MCU1.grid(row=1, column=5)

MCU2 = tk.Entry(owo)
MCU2.grid(row=2, column=5)

MCU3 = tk.Entry(owo)
MCU3.grid(row=3, column=5)

MCU4 = tk.Entry(owo)
MCU4.grid(row=4, column=5)

MCU5 = tk.Entry(owo)
MCU5.grid(row=5, column=5)

MCU6 = tk.Entry(owo)
MCU6.grid(row=6, column=5)

def verification():
    entries = [CANT1, CANT2, CANT3, CANT4, CANT5, CANT6,
               COSTU1, COSTU2, COSTU3, COSTU4, COSTU5, COSTU6,
               PVU1, PVU2, PVU3, PVU4, PVU5, PVU6]

    for entry in entries:
        value = entry.get()
        if not value:
            tk.messagebox.showerror("Error", "Ingrese valores en todos los campos")
            return

        try:
            float(value)
        except ValueError:
            tk.messagebox.showerror("Error", "Ingrese números válidos")
            return
        
    details = [DETAIL1, DETAIL2, DETAIL3, DETAIL4, DETAIL5, DETAIL6]
    for qwe in details:
        valor = qwe.get()
    if not valor:
        tk.messagebox.showerror("Error", "Ingrese texto en todos los campos")
        return
    if any(char.isdigit() for char in valor):
        tk.messagebox.showerror("Error", "Los campos de detalle no deben contener números")
        return
    
    save_infomation()

        
def save_infomation():
    print("holamundo")



SAVE = tk.Button(
    owo,
    text="Guardar",
    command=verification,
).grid(row=7,column=3)


owo.mainloop()