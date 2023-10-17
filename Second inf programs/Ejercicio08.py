import tkinter as tk
import datetime
import subprocess
owo = tk.Tk()


user = tk.StringVar(owo)
password = tk.StringVar(owo)
register = open("regis.txt", "w")



def cont():

    if user.get() != "qwert" or password.get() != "qwert":

        with open("log.txt", "a") as log_file:
            log_file.write(f"ERROR - TIME: {datetime.datetime.now()}\n")
        




owo.geometry("400x320") #TAMAÑO DE LA VENTANA
owo.resizable(False, False) #NO PUEDA CAMBIAR TA

#Login


owo.title("Login")
tk.Label(
    owo,
    text="USER:",
    font=("Courier", 16),
    bg= "#141414",
    foreground="#fff"
).pack(
    fill=tk.BOTH,
)

tk.Entry(
    owo,
    foreground="#fff",
    bg="#141414",
    borderwidth=1,
    font=("courier", 14),
    textvariable=user,

    
).pack_configure(
    fill=tk.BOTH,
)

tk.Label(
    owo,
    text="CONTRASEÑA:",
    font=("Courier", 16),
    bg= "#141414",
    foreground="#fff"
).pack(
    fill=tk.BOTH,
)

tk.Entry(
    owo,
    foreground="#fff",
    bg="#141414",
    borderwidth=1,
    font=("courier", 14),
    textvariable=password,

    
).pack_configure(
    fill=tk.BOTH,
)

tk.Button(
    owo,
    text = "Iniciar sesion",
    font= ("Courier", 15),
    command=cont,
    relief="flat",
    bg="white",
    fg="black",
    
).pack()


register.close()
owo.mainloop()