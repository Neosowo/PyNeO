# Ejercicio 1
import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, result)

app = tk.Tk()
app.title("Calculadora")

entry = tk.Entry(app, width=20)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(app, text=button, width=5, command=calculate).grid(row=row_val, column=col_val)
    elif button == 'C':
        tk.Button(app, text=button, width=5, command=clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(app, text=button, width=5, command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

app.mainloop()
