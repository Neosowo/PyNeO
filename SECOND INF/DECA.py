import tkinter as tk
from tkinter import messagebox

owo = tk.Tk()

owo.title("Cabecera")
owo.geometry("525x600")
owo.resizable(False, False)

cantidad_total_por_producto = {}

cantidades = []
detalles = []
valores = []
totales = []

def calcular_entrada(entry_cant, entry_valu, entry_valt, entry_detal):
    cant = entry_cant.get()
    valu = entry_valu.get()

    if not cant.replace('.', '').replace('-', '').isdigit() or not valu.replace('.', '').replace('-', '').isdigit():
        messagebox.showwarning("Error", "no valido numero")
        return 0

    if not cant or not valu:
        return 0

    cant = float(cant)
    valu = float(valu)

    valt = cant * valu

    entry_valt.delete(0, tk.END)
    entry_valt.insert(0, f"{valt:.2f}")

    detal = entry_detal.get()
    entry_detal.delete(0, tk.END)
    entry_detal.insert(0, detal)

    return valt

def actualizar_cantidad_total(producto, cantidad):
    if producto in cantidad_total_por_producto:
        cantidad_total_por_producto[producto] += cantidad
    else:
        cantidad_total_por_producto[producto] = cantidad

    subms.set(f"${sum(cantidad_total_por_producto.values()):.2f}")

def trans():
    qname = name.get()
    qruc = ruc.get()
    qdireccion = direccion.get()
    qtel = tel.get()
    print(qname)
    
    qn1detal = str(n1detal.get())
    print(qn1detal)

    with open("Datos.txt", "a") as f:
      f.write(f"  {qname} , {qruc} , {qdireccion} , {qtel}" + "\n")
      f.write("////" + "\n")

    with open("Lista.txt", "a") as q:
        qn1detal = n1detal.get()
        print(qn1detal)
        qn2detal = n2detal.get()
        qn3detal = n3detal.get()
        qn4detal = n4detal.get()
        qn5detal = n5detal.get()
        qn6detal = n6detal.get()
        qn7detal = n7detal.get()
        qn8detal = n8detal.get()
        qn9detal = n9detal.get()
        qn10detal = n10detal.get()
        q.write("LISTA DE PRODUCTOS\n")
        if(len(qn1detal) > 0):
            q.write(f"{qn1detal}")
        if(len(qn2detal) > 0):
            q.write(f"{qn2detal}")
        if(len(qn3detal) > 0):
            q.write(f"{qn3detal}")
        if(len(qn4detal) > 0):
            q.write(f"{qn4detal}")
        if(len(qn5detal) > 0):
            q.write(f"{qn5detal}")
        if(len(qn6detal) > 0):
            q.write(f"{qn6detal}")
        if(len(qn7detal) > 0):
            q.write(f"{qn7detal}")
        if(len(qn8detal) > 0):
            q.write(f"{qn8detal}")
        if(len(qn9detal) > 0):
            q.write(f"{qn9detal}")
        if(len(qn10detal) > 0):
            q.write(f"{qn10detal}")
        
        
        


            



    if not any([cantidad.get() for cantidad in cantidades]):
        messagebox.showwarning("Warning", "Ingrese al menos una cantidad.")
        return
    


    productos = [detalle.get() for detalle in detalles]

    subtotal = 0

    for i, cant_entry in enumerate(cantidades):
        cantidad = cant_entry.get()
        if cantidad:
            cantidad = float(cantidad)
            valt = calcular_entrada(cant_entry, valores[i], totales[i], detalles[i])
            if valt:
                subtotal += valt
                actualizar_cantidad_total(productos[i], cantidad)


    iva = 0.12 * subtotal
    total = subtotal + iva

    subms.set(f"${subtotal}")



tk.Label(owo, text="Razon social:").grid(column=0, row=1)
tk.Label(owo, text="MTPSTORE").grid(column=3, row=1)
tk.Label(owo, text="R.U.C: ").grid(column=0, row=2)
tk.Label(owo, text="0990970211001").grid(column=3, row=2)
tk.Label(owo, text="Dirección: ").grid(column=0, row=3)
tk.Label(owo, text="Km 6 1/2 Vía Daule").grid(column=3, row=3)
tk.Label(owo, text="Telf:").grid(column=0, row=4)
tk.Label(owo, text="6005800").grid(column=3, row=4)

tk.Label(owo, text="-----------").grid(column=0, row=5)
tk.Label(owo, text="Nombre: ").grid(column=0, row=6)
tk.Label(owo, text="C.I./R.U.C.: ").grid(column=0, row=7)
tk.Label(owo, text="Dirección: ").grid(column=0, row=8)
tk.Label(owo, text="Telf: ").grid(column=0, row=9)
tk.Label(owo, text="-----------").grid(column=0, row=10)

name = tk.Entry(owo)
name.grid(column=3, row=6)
ruc = tk.Entry(owo)
ruc.grid(column=3, row=7)
direccion = tk.Entry(owo)
direccion.grid(column=3, row=8)
tel = tk.Entry(owo)
tel.grid(column=3, row=9)

tk.Label(owo, text="-------------------------").grid(column=0, row=10)
tk.Label(owo, text="Cantidad").grid(column=0, row=11)
tk.Label(owo, text="-------------------------").grid(column=1, row=10)
tk.Label(owo, text="Detalle").grid(column=1, row=11)
tk.Label(owo, text="-------------------------").grid(column=2, row=10)
tk.Label(owo, text="Valor U.").grid(column=2, row=11)
tk.Label(owo, text="-------------------------").grid(column=3, row=10)
tk.Label(owo, text="Valor T.").grid(column=3, row=11)

tk.Label(owo, text="Cant ").grid(column=0, row=12)

n1cant = tk.Entry(owo)
n1cant.grid(column=0, row=13)
n2cant = tk.Entry(owo)
n2cant.grid(column=0, row=14)
n3cant = tk.Entry(owo)
n3cant.grid(column=0, row=15)
n4cant = tk.Entry(owo)
n4cant.grid(column=0, row=16)
n5cant = tk.Entry(owo)
n5cant.grid(column=0, row=17)
n6cant = tk.Entry(owo)
n6cant.grid(column=0, row=18)
n7cant = tk.Entry(owo)
n7cant.grid(column=0, row=19)
n8cant = tk.Entry(owo)
n8cant.grid(column=0, row=20)
n9cant = tk.Entry(owo)
n9cant.grid(column=0, row=21)
n10cant = tk.Entry(owo)
n10cant.grid(column=0, row=22)

tk.Label(owo, text="Detalle ").grid(column=1, row=12)

n1detal = tk.Entry(owo)
n1detal.grid(column=1, row=13)
n2detal = tk.Entry(owo)
n2detal.grid(column=1, row=14)
n3detal = tk.Entry(owo)
n3detal.grid(column=1, row=15)
n4detal = tk.Entry(owo)
n4detal.grid(column=1, row=16)
n5detal = tk.Entry(owo)
n5detal.grid(column=1, row=17)
n6detal = tk.Entry(owo)
n6detal.grid(column=1, row=18)
n7detal = tk.Entry(owo)
n7detal.grid(column=1, row=19)
n8detal = tk.Entry(owo)
n8detal.grid(column=1, row=20)
n9detal = tk.Entry(owo)
n9detal.grid(column=1, row=21)
n10detal = tk.Entry(owo)
n10detal.grid(column=1, row=22)

tk.Label(owo, text="Val. U.").grid(column=2, row=12)

n1valu = tk.Entry(owo)
n1valu.grid(column=2, row=13)
n2valu = tk.Entry(owo)
n2valu.grid(column=2, row=14)
n3valu = tk.Entry(owo)
n3valu.grid(column=2, row=15)
n4valu = tk.Entry(owo)
n4valu.grid(column=2, row=16)
n5valu = tk.Entry(owo)
n5valu.grid(column=2, row=17)
n6valu = tk.Entry(owo)
n6valu.grid(column=2, row=18)
n7valu = tk.Entry(owo)
n7valu.grid(column=2, row=19)
n8valu = tk.Entry(owo)
n8valu.grid(column=2, row=20)
n9valu = tk.Entry(owo)
n9valu.grid(column=2, row=21)
n10valu = tk.Entry(owo)
n10valu.grid(column=2, row=22)

tk.Label(owo, text="Subtotal:").grid(column=2, row=23)
tk.Label(owo, text="Sub 0%:").grid(column=2, row=24)
tk.Label(owo, text="Sub 12%:").grid(column=2, row=25)

# BOTON CALCULAR
Calcular = tk.Button(owo, text="Calcular", command=trans).grid(column=1, row=25)

tk.Label(owo, text="IVA:").grid(column=2, row=26)
tk.Label(owo, text="Total:").grid(column=2, row=27)

subms = tk.Label(owo, text="$$").grid(column=3, row=23)
iva_label = tk.Label(owo, text="$$").grid(column=3, row=24)
tk.Label(owo, text="$$").grid(column=3, row=25)
total_label = tk.Label(owo, text="$$").grid(column=3, row=26)
tk.Label(owo, text="$$").grid(column=3, row=27)

tk.Label(owo, text="Val. T.").grid(column=3, row=12)

n1valt = tk.Entry(owo)
n1valt.grid(column=3, row=13)
n2valt = tk.Entry(owo)
n2valt.grid(column=3, row=14)
n3valt = tk.Entry(owo)
n3valt.grid(column=3, row=15)
n4valt = tk.Entry(owo)
n4valt.grid(column=3, row=16)
n5valt = tk.Entry(owo)
n5valt.grid(column=3, row=17)
n6valt = tk.Entry(owo)
n6valt.grid(column=3, row=18)
n7valt = tk.Entry(owo)
n7valt.grid(column=3, row=19)
n8valt = tk.Entry(owo)
n8valt.grid(column=3, row=20)
n9valt = tk.Entry(owo)
n9valt.grid(column=3, row=21)
n10valt = tk.Entry(owo)
n10valt.grid(column=3, row=22)


for i in range(1, 11):
    cantidad_entry = tk.Entry(owo)
    cantidad_entry.grid(column=0, row=11+i)
    cantidades.append(cantidad_entry)

    detalle_entry = tk.Entry(owo)
    detalle_entry.grid(column=1, row=11+i)
    detalles.append(detalle_entry)

    valor_entry = tk.Entry(owo)
    valor_entry.grid(column=2, row=11+i)
    valores.append(valor_entry)

    total_entry = tk.Entry(owo)
    total_entry.grid(column=3, row=11+i)
    totales.append(total_entry)


subms = tk.StringVar()
subms.set("$$")
subms_label = tk.Label(owo, textvariable=subms)
subms_label.grid(column=3, row=23)
owo.mainloop()