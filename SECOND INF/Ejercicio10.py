#s = "hola como estas"

#for x in s:
 #   print(x)

#El numero siguiente es igual a la suma de sus dos predesesores

x = 0
y = 0
z = 1

r = int(input("Ingrese el número de iteraciones: "))
uwu = 1


print("1. 0")
for x in range(r):
    x = y
    y = z
    z = x + y;
    if(z % 2):
       r = 0
    else:
        uwu += 1
        print(f"{uwu}. {z}")

    
