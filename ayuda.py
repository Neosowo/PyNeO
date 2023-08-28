def ingesta():
    try:
        anastr = input("INGRESE SU FECHA DE NACIMIENTO EN ESTE FORMATO (AA/MM/DD): ")
        anao = anastr.split('/')
        if(len(anao) != 3):
            print("ERROR")
            ingesta()
        else:
            verificacion(anao)
    except ValueError:
        print("ERROR")
        ingesta()
def verificacion(anao):
    aniostr = anao[0]
    messtr = anao[1]
    diastr = anao[2]
    año = int(aniostr)
    mes = int(messtr)
    dia = int(diastr)
    if(año < 1800 or año > 2023):
        print("ERROR")
        ingesta()
    if(mes < 1 or mes > 12):
        print("ERROR")
        ingesta()
    if(dia < 1 or dia > 31):
        print("ERROR")
        ingesta()
    impresion(año)

def impresion(año):
    ano = 2023 - año
    if (ano < 0):
        ano = ano * -1
    print(f"2023 - {año} = {ano}\nTIENES {ano} ANOS")

ingesta()