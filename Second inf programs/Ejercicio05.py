import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)

app = tk.Tk()
app.title("Gestor de Tareas")

task_entry = tk.Entry(app)
task_entry.pack(pady=13)

add_button = tk.Button(app, text="Agregar Tarea", command=add_task)
add_button.pack()

delete_button = tk.Button(app, text="Eliminar Tarea", command=delete_task)
delete_button.pack()

task_listbox = tk.Listbox(app)
task_listbox.pack()

app.mainloop()