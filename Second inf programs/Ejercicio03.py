val = int(input('Coloque un número: '))
val2 = int(input('Coloque el segundo número: '))
op = input("MENU\n1. Multiplicar\n2. Dividir\n3. Elevacion")

if(op == '1'):
    print('opcion 1')
    mult = val * val2
    print("RESULTADO: " + mult)
elif(op == '2'):
    val3 = int(input('Ingrese un valor para dividir: '))
    div = mult / val3
    print

    val4 = int(input('Ingrese un valor para poder elevar: '))

    ele = div**val4
    print('Tu resultado es: ', ele)