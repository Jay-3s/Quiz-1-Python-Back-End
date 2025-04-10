
menu = False

while menu == False:
 
    opcion = int(input("Menú interactivo\n1. Mostrar mensajes\n2. Nombres\n3. Salir\n Digite una opción: "))

    if opcion == 1:
        print("Mostrando mensajes...")
        
        menu = True
    elif opcion == 2:
        print("Mostrando nombres")
        break
    elif opcion == 3:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no valida, intentelo denuevo.")

    print("----------------------------------------------")
