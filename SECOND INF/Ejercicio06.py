import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        text.delete('1.0', tk.END)
        with open(file_path, 'r') as file:
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get('1.0', tk.END))

app = tk.Tk()
app.title("Editor de Texto")

text = tk.Text(app)
text.pack()

menu = tk.Menu(app)
app.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Abrir", command=open_file)
file_menu.add_command(label="Guardar", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=app.quit)

app.mainloop()
