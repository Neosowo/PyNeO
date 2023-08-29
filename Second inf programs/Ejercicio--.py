#Desarrollar un programa que mediante los dos primeros digitos de tu cédula identifique su provincia
def registro(ced):
    n = 1
    while len(ced) != 10:
        ced = input("Su cédula no puede tener más de 10 dígitos")

    if ced[0] == "0" and ced[1] == "1":
        print('Usted proviene de Azuay')
    elif ced[0] == "0" and ced[1] == "2":
        print('Usted proviene de Bolivar')
    elif ced[0] == "0" and ced[1] == "3":
        print('Usted proviene de Cañar')
    elif ced[0] == "0" and ced[1] == "4":
        print('Usted proviene de Carchi')
    elif ced[0] == "0" and ced[1] == "5":
        print('Usted proviene de Cotopaxi')
    elif ced[0] == "0" and ced[1] == "6":
        print('Usted proviene de Chimborazo')
    elif ced[0] == "0" and ced[1] == "7":
        print('Usted proviene de El Oro')
    elif ced[0] == "0" and ced[1] == "8":
        print('Usted proviene de Esmeraldas')
    elif ced[0] == "0" and ced[1] == "9":
        print('Usted proviene de Guayas')
    elif ced[0] == "1" and ced[1] == "0":
        print('Usted proviene de Imbabura')
    elif ced[0] == "1" and ced[1] == "1":
        print('Usted proviene de Loja')
    elif ced[0] == "1" and ced[1] == "2":
        print('Usted proviene de Los Rios')
    elif ced[0] == "1" and ced[1] == "3":
        print('Usted proviene de Manabí')
    elif ced[0] == "1" and ced[1] == "4":
        print('Usted proviene de Morona Santiago')
    elif ced[0] == "1" and ced[1] == "5":
        print('Usted proviene de Napo')
    elif ced[0] == "1" and ced[1] == "6":
        print('Usted proviene de Pastaza')
    elif ced[0] == "1" and ced[1] == "7":
        print('Usted proviene de Pichincha')
    elif ced[0] == "1" and ced[1] == "8":
        print('Usted proviene de Tungurahua')
    elif ced[0] == "1" and ced[1] == "9":
        print('Usted proviene de Zamora Chinchipe')
    elif ced[0] == "2" and ced[1] == "0":
        print('Usted proviene de Galápagos')
    elif ced[0] == "2" and ced[1] == "1":
        print('Usted proviene de Sucumbios')
    elif ced[0] == "2" and ced[1] == "2":
        print('Usted proviene de Orellana')
    elif ced[0] == "2" and ced[1] == "3":
        print('Usted proviene de Santo Domingo de los Tsáchilas')
    elif ced[0] == "2" and ced[1] == "4":
        print('Usted proviene de Santa Elena')
    elif ced[0] == "3" and ced[1] == "0":
        print('N09úmero reservado para ecuatorianos registrados en el exterior.')

ced = input('Ingrese su cédula: ')
registro(ced)
