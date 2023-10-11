#Desarrolla un inicio de sesión con metodos
users = ["nose"] 
password = ["nose"]

def register():
    newuser = users.append(input("Nuevo usuario: "))
    newpass = password.append(input("Contraseña: "))


def login():
    user = input("Usuario: ")
    passw = input("Contraseña: ")
    if user in users and passw == password[users.index(user)]:
        print("Bienvenido uwu")
    else:
        print("Usuario o contraseña incorrectos")


while True:
    choice = input("Seleccione una opción: \n1. Registrar \n2. Iniciar sesión \n3. Salir \nOP: ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Hasta luego.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")