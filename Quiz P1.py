
from colorama import init, Fore, Style

datos = {
    "producto": "zapatillas air jordan 1",
    "color": "Blanco",
    "talla": 42,
    "stock": 20,
}

print("Bienvenido a la tienda de Nike")

print(datos)

print("----------------------------------------")

def editar( datos):

    dato = input("Ingrese la clave a editar: ")

    if dato in datos:
        nuevo_valor = input(f"Ingrese el nuevo valor para {dato}: ")
        datos[dato] = nuevo_valor
        print(f"{dato} actualizado a {nuevo_valor}.")
        print(datos)
    else:
        print("La clave no existe en los datos.")


print("----------------------------------------")


def eliminar(datos):

    valor_eliminado= input("Ingrese la clave a eliminar: ")

    if valor_eliminado in datos:
        del datos[valor_eliminado]
        print(f"{valor_eliminado} ha sido eliminad@.")
        print(datos)
    else:
        print("La clave no existe en los datos.")


menu = False

while menu == False:
 
    opcion = int(input("Menú interactivo\n1. Editar\n2. Eliminar\n3. Salir\n Digite una opción: "))

    if opcion == 1:
        print("Editando...")
        editar(datos)
        menu = True
    elif opcion == 2:
        print("Eliminando...")
        eliminar( datos)
        
    elif opcion == 3:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no valida, intentelo denuevo.")

    print("----------------------------------------------")