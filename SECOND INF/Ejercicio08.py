import tkinter as tk
import datetime
import subprocess

owo = tk.Tk()#owo es la ventana

user = tk.StringVar(owo)
password = tk.StringVar(owo)
register = open("regis.txt", "w")


def cont():
    if user.get() != "qwert" or password.get() != "qwert":
        with open("log.txt", "a") as log_file:
            log_file.write(f"ERROR - TIME: {datetime.datetime.now()}\n")
        

owo.geometry("400x320") #TAMAÑO DE LA VENTANA
owo.resizable(False, False) #NO PUEDA CAMBIAR TA
owo.title("Login") #TITULO DE LA VENTANA
#TEXTO
tk.Label( #TEXTO
    owo,
    text="USER:",
    font=("Courier", 16),
    bg= "#141414",
    foreground="#fff"
).pack(
    fill=tk.BOTH,
)
#ENTRADA DE TEXTO
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
#TEXTO
tk.Label(
    owo,
    text="CONTRASEÑA:",
    font=("Courier", 16),
    bg= "#141414",
    foreground="#fff"
).pack(
    fill=tk.BOTH,
)
#ENTRADA DE TEXTO
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
#BOTON
tk.Button( 
    owo,
    command=cont,
    text = "Iniciar sesion",
    font= ("Courier", 15),
    relief="flat",
    bg="white",
    fg="black",
    
).pack()


register.close()
owo.mainloop()
