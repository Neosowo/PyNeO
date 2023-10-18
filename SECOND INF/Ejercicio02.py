def ingesta():
    try:
        cedstr = input("Ingrese su cedula en este formato (00-00000000): ")
        if len(cedstr)!= 11:
            print("Cedula invalida")
            ingesta()
        ced = cedstr.split("-")
        if len(ced)!= 2:
            print("Cedula invalida")
            ingesta()
        verificacion(ced)
    except ValueError:
        print("Cedula invalida")
        ingesta()

def verificacion(ced):
    prov = ced[0]
    cedstr = ced[1]
    if prov == "01":
        print('Usted proviene de Azuay')
    elif prov == "02":
        print('Usted proviene de Bolivar')
    elif prov == "03":
        print('Usted proviene de Cañar')
    elif prov == "04":
        print('Usted proviene de Carchi')
    elif prov == "05":
        print('Usted proviene de Cotopaxi')
    elif prov == "06":
        print('Usted proviene de Chimborazo')
    elif prov == "07":
        print('Usted proviene de El Oro')
    elif prov == "08":
        print('Usted proviene de Esmeraldas')
    elif prov == "09":
        print('Usted proviene de Guayas')
    elif prov == "10":
        print('Usted proviene de Imbabura')
    elif prov == "11":
        print('Usted proviene de Loja')
    elif prov == "12":
        print('Usted proviene de Los Rios')
    elif prov == "13":
        print('Usted proviene de Manabí')
    elif prov == "14":
        print('Usted proviene de Morona Santiago')
    elif prov == "15":
        print('Usted proviene de Napo')
    elif prov == "16":
        print('Usted proviene de Pastaza')
    elif prov == "17":
        print('Usted proviene de Pichincha')
    elif prov == "18":
        print('Usted proviene de Tungurahua')
    elif prov == "19":
        print('Usted proviene de Zamora Chinchipe')
    elif prov == "20":
        print('Usted proviene de Galápagos')
    elif prov == "21":
        print('Usted proviene de Sucumbios')
    elif prov == "22":
        print('Usted proviene de Orellana')
    elif prov == "23":
        print('Usted proviene de Santo Domingo de los Tsáchilas')
    elif prov == "24":
        print('Usted proviene de Santa Elena')
    elif prov == "30":
        print('Número reservado para ecuatorianos registrados en el exterior.')
    else:
        print("Error!")
        exit()
ingesta()