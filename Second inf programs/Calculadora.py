import tkinter as tk
import numpy as np
from scipy import stats

owo = tk.Tk()

palabra = tk.StringVar()
entrada = tk.StringVar(owo)
def convertidor():
    entrada_usuario = entrada.get()  
    n = entrada_usuario.split('+')
    
    numeros = []  
    x = 0  
    
    while x < len(n):
        try:
            numero = float(n[x]) 
            numeros.append(numero)  
        except ValueError:
            print(f"Error: '{n[x]}' no es un número válido")
        x += 1
    
    if numeros:
        suma = np.sum(numeros)
        media = np.mean(numeros)
        mediana = np.median(numeros)
        moda = stats.mode(numeros)


        Rsum.config(text=suma)
        Rprom.config(text=media)
        Rmediana.config(text=mediana)
        Rmoda.config(text=moda)
        
    else:
        print("No se encontraron números válidos en la entrada del usuario")


owo.geometry("500x320")
owo.configure(background="#141414")
owo.title("Calculadora")
owo.resizable(False, False)
ruta_icono = "C:/Users/erick/OneDrive/Escritorio/ico.ico"
owo.iconbitmap(ruta_icono)
#tk.Wm.wm_title(owo, "Convertidor")

tk.Label(
    owo,
    text="INTRODUCE LAS CANTIDADES A SUMAR:",
    font=("Courier", 15),
        bg="#131313",
    fg="#fff",

).pack(
    fill=tk.BOTH,
)

tk.Entry(
    owo,
    foreground="#fff",
    bg="#141414",
    borderwidth=1,
    font=("courier", 14),
    textvariable=entrada,

    
).pack_configure(
    fill=tk.BOTH,
)

tk.Label(
    owo,
    text="SUMA TOTAL:",
    font=("Courier", 15),
        bg="#131313",
    fg="#fff",

).pack(
    fill=tk.BOTH,
)


Rsum = tk.Label(
    owo,
    text="-",
    font=("Courier", 15),
        bg="#131313",
    fg="#fff",

)
Rsum.pack(
    fill=tk.BOTH,
)

tk.Label(
    owo,
    text="MEDIA:",
    font=("Courier", 15),
        bg="#131313",
    fg="#fff",

).pack(
    fill=tk.BOTH,
)


Rprom = tk.Label(
    owo,
    text="-",
    font=("Courier", 15),
        bg="#131313",
    fg="#fff",

)
Rprom.pack(
    fill=tk.BOTH,
)

tk.Label(
    owo,
    text="MEDIANA:",
    font=("Courier", 15),
        bg="#131313",
    fg="#fff",

).pack(
    fill=tk.BOTH,
)


Rmediana = tk.Label(
    owo,
    text="-",
    font=("Courier", 15),
        bg="#131313",
    fg="#fff",

)
Rmediana.pack(
    fill=tk.BOTH,
)

tk.Label(
    owo,
    text="MODA:",
    font=("Courier", 15),
        bg="#131313",
    fg="#fff",

).pack(
    fill=tk.BOTH,
)


Rmoda = tk.Label(
    owo,
    text="-",
    font=("Courier", 15),
        bg="#131313",
    fg="#fff",

)
Rmoda.pack(
    fill=tk.BOTH,
)



tk.Button(
    owo,
    text = "CALCULAR",
    font= ("Courier", 15),
    command=convertidor,
    relief="flat",
    bg="white",
    fg="black",
    
).pack()




owo.mainloop()