#Nos permite decidir de acuerdo al argumento que se le pasa entre parentesis
x = 0
if (x == 1):
    print("x es igual a 1")

#Si queremos ingresar otra condicionante usando la misma variable, pero con diferente argumento, usamos la siguiente línea
elif(x == 2):
    print("x es igual a 2")

#En caso de que no se cumpla podemos usar else, que vc
else:
    print(f"{x} no es ni 1 ni 0")