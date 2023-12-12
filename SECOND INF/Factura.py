import tkinter as tk
from tkinter import messagebox



def verifle():
  canti1=cant1.get()
  canti2=cant2.get()
  canti3=cant3.get()
  canti4=cant4.get()
  canti5=cant5.get()
  canti6=cant6.get()
  canti7=cant7.get()
  canti8=cant8.get()
  canti9=cant9.get()
  canti10=cant10.get()
  
  try:
      canti1=float(canti1) if canti1 else 0
      canti2=float(canti2) if canti2 else 0
      canti3=float(canti3) if canti3 else 0
      canti4=float(canti4) if canti4 else 0
      canti5=float(canti5) if canti5 else 0
      canti6=float(canti6) if canti6 else 0
      canti7=float(canti7) if canti7 else 0
      canti8=float(canti8) if canti8 else 0
      canti9=float(canti9) if canti9 else 0
      canti10=float(canti10) if canti10 else 0     
  except ValueError:
      tk.messagebox.showerror("Error", "Ingrese números")
      return

  vun1=vu1.get()
  vun2=vu2.get()
  vun3=vu3.get()
  vun4=vu4.get()
  vun5=vu5.get()
  vun6=vu6.get()
  vun7=vu7.get()
  vun8=vu8.get()
  vun9=vu9.get()
  vun10=vu10.get()
  try:
      vun1=float(vun1) if vun1 else 0
      vun2=float(vun2) if vun2 else 0
      vun3=float(vun3) if vun3 else 0
      vun4=float(vun4) if vun4 else 0
      vun5=float(vun5) if vun5 else 0
      vun6=float(vun6) if vun6 else 0
      vun7=float(vun7) if vun7 else 0
      vun8=float(vun8) if vun8 else 0
      vun9=float(vun9) if vun9 else 0
      vun10=float(vun10) if vun10 else 0     
  except ValueError:
      tk.messagebox.showerror("Error", "Ingrese números válidos")
      return 
            
def vtotal():
    canti1=cant1.get()
    canti2=cant2.get()
    canti3=cant3.get()
    canti4=cant4.get()
    canti5=cant5.get()
    canti6=cant6.get()
    canti7=cant7.get()
    canti8=cant8.get()
    canti9=cant9.get()
    canti10=cant10.get()
    
    canti1=float(canti1) if canti1 else 0
    canti2=float(canti2) if canti2 else 0
    canti3=float(canti3) if canti3 else 0
    canti4=float(canti4) if canti4 else 0
    canti5=float(canti5) if canti5 else 0
    canti6=float(canti6) if canti6 else 0
    canti7=float(canti7) if canti7 else 0
    canti8=float(canti8) if canti8 else 0
    canti9=float(canti9) if canti9 else 0
    canti10=float(canti10) if canti10 else 0
    
    vun1=vu1.get()
    vun2=vu2.get()
    vun3=vu3.get()
    vun4=vu4.get()
    vun5=vu5.get()
    vun6=vu6.get()
    vun7=vu7.get()
    vun8=vu8.get()
    vun9=vu9.get()
    vun10=vu10.get()
                
                
    vun1=float(vun1) if vun1 else 0
    vun2=float(vun2) if vun2 else 0
    vun3=float(vun3) if vun3 else 0
    vun4=float(vun4) if vun4 else 0
    vun5=float(vun5) if vun5 else 0
    vun6=float(vun6) if vun6 else 0
    vun7=float(vun7) if vun7 else 0
    vun8=float(vun8) if vun8 else 0
    vun9=float(vun9) if vun9 else 0
    vun10=float(vun10) if vun10 else 0
    
  
    rest1=canti1*vun1
    rest2=canti2*vun2
    rest3=canti3*vun3
    rest4=canti4*vun4
    rest5=canti5*vun5
    rest6=canti6*vun6
    rest7=canti7*vun7
    rest8=canti8*vun8
    rest9=canti9*vun9
    rest10=canti10*vun10
    
    vt1.delete(0, tk.END)
    vt1.insert(0, str(rest1))
    vt2.delete(0, tk.END)
    vt2.insert(0, str(rest2))
    vt3.delete(0, tk.END)
    vt3.insert(0, str(rest3))
    vt4.delete(0, tk.END)
    vt4.insert(0, str(rest4))
    vt5.delete(0, tk.END)
    vt5.insert(0, str(rest5))
    vt6.delete(0, tk.END)
    vt6.insert(0, str(rest6))
    vt7.delete(0, tk.END)
    vt7.insert(0, str(rest7))
    vt8.delete(0, tk.END)
    vt8.insert(0, str(rest8))
    vt9.delete(0, tk.END)
    vt9.insert(0, str(rest9))
    vt10.delete(0, tk.END)
    vt10.insert(0, str(rest10))
    
def subtotal():
  vtl1=vt1.get()
  vtl2=vt2.get()
  vtl3=vt3.get()
  vtl4=vt4.get()
  vtl5=vt5.get()
  vtl6=vt6.get()
  vtl7=vt7.get()
  vtl8=vt8.get()
  vtl9=vt9.get()
  vtl10=vt10.get()
  
  vtl1=float(vtl1) if vtl1 else 0
  vtl2=float(vtl2) if vtl2 else 0
  vtl3=float(vtl3) if vtl3 else 0
  vtl4=float(vtl4) if vtl4 else 0
  vtl5=float(vtl5) if vtl5 else 0
  vtl6=float(vtl6) if vtl6 else 0
  vtl7=float(vtl7) if vtl7 else 0
  vtl8=float(vtl8) if vtl8 else 0
  vtl9=float(vtl9) if vtl9 else 0
  vtl10=float(vtl10) if vtl10 else 0
  
  subtl=vtl1+vtl2+vtl3+vtl4+vtl5+vtl6+vtl7+vtl8+vtl9+vtl10
  
  sbt.config(text=f"$ {subtl}")
  sbtl0=float(0)
  sbtl12=float(0)
  IVA= subtl*0.12
  total=subtl+sbtl0+sbtl12+IVA
  sbtl0=round(sbtl0,2)
  sbtl12=round(sbtl12,2)
  total=round(total,2)
  IVA=round(IVA,2)
  
  sbt0.config(text=f"$ {sbtl0}")
  sbt12.config(text=f"$ {sbtl12}")
  ivap.config(text=f"$ {IVA}")
  tlp.config(text=f"$ {total}") 
  return subtl, sbtl0, sbtl12, IVA, total
  
def saved(subtl, sbtl0, sbtl12, iva, total):
     
    nombre=nameen.get()
    ciruc=ruccen.get()
    direccion= direccen.get()
    telf=telfcen.get()
    detal1=detail1.get()
    detal2=detail2.get()
    detal3=detail3.get()
    detal4=detail4.get()
    detal5=detail5.get()
    detal6=detail6.get()
    detal7=detail7.get()
    detal8=detail8.get()
    detal9=detail9.get()
    detal10=detail10.get()

    sub=subtotal(subtl)
    sub0=subtotal(sbtl0)
    sub12=subtotal(sbtl12)
    IVA=subtotal(iva)
    total=subtotal(total)
    
    with open("Datos.txt", "a") as f:
      f.write(f"  {nombre} , {ciruc} , {direccion} , {telf}" + "\n")
      f.write("----------------------------------------------------" + "\n")
      
    with open("Datos2.txt", "a") as f:
      f.write(f"Subtotal: {subtl}"+ "\n" + "Sub0%: {sub0}"+"\n"+"Sub2%: {sub12}"+"\n"+"IVA: {IVA}"+"\n"+"Total: {total}")
      f.write("----------------------------------------------------" + "\n")
def eject():
    verifle()
    vtotal()
    subtotal()
    saved()   
    

vent=tk.Tk()
vent.title("Cabecera")
vent.minsize(width=50, height=600)
emp=tk.Label(vent,text="           Razón Socio:                                                           ")
emp.grid(row=0, column=1, columnspan=2, sticky="ew")
emp2=tk.Label(vent,text="                     MTPSTORE")
emp2.grid(row=0, column=2)

ruc=tk.Label(vent,text="        Ruc:                                                                       ")
ruc.grid(row=1, column=1, columnspan=2, sticky="ew")
ruc2=tk.Label(vent,text="               0990970211001")
ruc2.grid(row=1, column=2)

direc=tk.Label(vent,text="      Dirección:                                                           ")
direc.grid(row=2, column=1, columnspan=2, sticky="ew")
direc2=tk.Label(vent,text="               6 1/2 Vía Daule")
direc2.grid(row=2, column=2)

telf=tk.Label(vent,text="                      Telf:                                                                                     ")
telf.grid(row=3, column=1, columnspan=2, sticky="ew")
direc2=tk.Label(vent,text="                          6005800")
direc2.grid(row=3, column=2)


line=tk.Label(vent,text="------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
line.grid(row=4, column=0, columnspan=4 , sticky="ew")



name=tk.Label(vent,text="                       Nombre: ")
name.grid(row=5, column=0, columnspan=3, sticky="ew")
nameen=tk.Entry(vent)
nameen.grid(row=5, column=2)

rucc=tk.Label(vent,text="                     CI/RUC: ")
rucc.grid(row=6, column=0, columnspan=3, sticky="ew")
ruccen=tk.Entry(vent)
ruccen.grid(row=6, column=2)

direcc=tk.Label(vent,text="                         Dirección: ")
direcc.grid(row=7, column=0, columnspan=3, sticky="ew")
direccen=tk.Entry(vent)
direccen.grid(row=7, column=2)

telfc=tk.Label(vent,text="                        Teléfono: ")
telfc.grid(row=8, column=0, columnspan=3, sticky="ew")
telfcen=tk.Entry(vent)
telfcen.grid(row=8, column=2)

line2=tk.Label(vent,text="------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
line2.grid(row=9, column=0, columnspan=4, sticky="ew")
line3=tk.Label(vent,text="------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
line3.grid(row=10, column=0, columnspan=4, sticky="ew")

dt=tk.Label(vent,text="Cantidad")
dt2=tk.Label(vent,text="Detalle")
dt3=tk.Label(vent,text="Valor Unidad")
dt4=tk.Label(vent,text="Valor Total")
dt.grid(row=11,column=0)
dt2.grid(row=11,column=1)
dt3.grid(row=11,column=2)
dt4.grid(row=11,column=3)

cant1=tk.Entry(vent)
cant1.grid(row=13,column=0)
detail1=tk.Entry(vent)
detail1.grid(row=13,column=1)
vu1=tk.Entry(vent)
vu1.grid(row=13,column=2)
vt1=tk.Entry(vent)
vt1.grid(row=13,column=3)

cant2=tk.Entry(vent)
cant2.grid(row=14,column=0)
detail2=tk.Entry(vent)
detail2.grid(row=14,column=1)
vu2=tk.Entry(vent)
vu2.grid(row=14,column=2)
vt2=tk.Entry(vent)
vt2.grid(row=14,column=3)

cant3=tk.Entry(vent)
cant3.grid(row=15,column=0)
detail3=tk.Entry(vent)
detail3.grid(row=15,column=1)
vu3=tk.Entry(vent)
vu3.grid(row=15,column=2)
vt3=tk.Entry(vent)
vt3.grid(row=15,column=3)

cant4=tk.Entry(vent)
cant4.grid(row=16,column=0)
detail4=tk.Entry(vent)
detail4.grid(row=16,column=1)
vu4=tk.Entry(vent)
vu4.grid(row=16,column=2)
vt4=tk.Entry(vent)
vt4.grid(row=16,column=3)

cant5=tk.Entry(vent)
cant5.grid(row=17,column=0)
detail5=tk.Entry(vent)
detail5.grid(row=17,column=1)
vu5=tk.Entry(vent)
vu5.grid(row=17,column=2)
vt5=tk.Entry(vent)
vt5.grid(row=17,column=3)

cant6=tk.Entry(vent)
cant6.grid(row=18,column=0)
detail6=tk.Entry(vent)
detail6.grid(row=18,column=1)
vu6=tk.Entry(vent)
vu6.grid(row=18,column=2)
vt6=tk.Entry(vent)
vt6.grid(row=18,column=3)

cant7=tk.Entry(vent)
cant7.grid(row=19,column=0)
detail7=tk.Entry(vent)
detail7.grid(row=19,column=1)
vu7=tk.Entry(vent)
vu7.grid(row=19,column=2)
vt7=tk.Entry(vent)
vt7.grid(row=19,column=3)

cant8=tk.Entry(vent)
cant8.grid(row=20,column=0)
detail8=tk.Entry(vent)
detail8.grid(row=20,column=1)
vu8=tk.Entry(vent)
vu8.grid(row=20,column=2)
vt8=tk.Entry(vent)
vt8.grid(row=20,column=3)

cant9=tk.Entry(vent)
cant9.grid(row=21,column=0)
detail9=tk.Entry(vent)
detail9.grid(row=21,column=1)
vu9=tk.Entry(vent)
vu9.grid(row=21,column=2)
vt9=tk.Entry(vent)
vt9.grid(row=21,column=3)

cant10=tk.Entry(vent)
cant10.grid(row=22,column=0)
detail10=tk.Entry(vent)
detail10.grid(row=22,column=1)
vu10=tk.Entry(vent)
vu10.grid(row=22,column=2)
vt10=tk.Entry(vent)
vt10.grid(row=22,column=3)

line4=tk.Label(vent,text="------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
line4.grid(row=23, column=0, columnspan=4, sticky="ew")
line5=tk.Label(vent,text="------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
line5.grid(row=24, column=0, columnspan=4, sticky="ew")

sb=tk.Label(vent,text="Subtotal")
sb0=tk.Label(vent,text="Sub 0%")
sb12=tk.Label(vent,text="Sub 12%")
iva=tk.Label(vent,text="IVA")
tl=tk.Label(vent,text="Total")
sb.grid(row=25,column=2)
sb0.grid(row=26,column=2)
sb12.grid(row=27,column=2)
iva.grid(row=28,column=2)
tl.grid(row=29,column=2)



sbt=tk.Label(vent,text="$$")
sbt0=tk.Label(vent,text="$$")
sbt12=tk.Label(vent,text="$$")
ivap=tk.Label(vent,text="$$")
tlp=tk.Label(vent,text="$$")

sbt.grid(row=25,column=3)
sbt0.grid(row=26,column=3)
sbt12.grid(row=27,column=3)
ivap.grid(row=28,column=3)
tlp.grid(row=29,column=3)



bt=tk.Button(vent,text="Calcular ", command=eject)
bt.grid(row=27,column=1)


    

vent.mainloop()