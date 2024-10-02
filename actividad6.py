def cifrado(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = 65 if char .isupper() else 97
            resultado += chr((ord(char) - base  + desplazamiento) % 26 + base)
        else:
            resultado += char
    return resultado

def descifrado(texto, desplazamiento):
    return cifrado(texto, -desplazamiento)

def main():
    while True:
        print("\nSelecciona una opcion: ")
        print("1. Encriptar")
        print("2.Desencriptar")
        print("3.Salir")
        opcion = input("Ingresa 1, 2 o 3: ")
        if opcion =="3":
            print("Saliendo del programa")
            break
        if opcion not in["1", "2"]:
            print("Opcion no valida. Por favor Ingresa 1, 2, o 3")
            continue
        texto = input("Ingresa el texto: ")
        desplazamiento = int(input("Ingresa el desplazamiento(un numero en entero)"))

        if opcion == "1":
            mensaje_cifrado = cifrado(texto, desplazamiento)
            print(f"Mensaje encriptado: {mensaje_cifrado}")
        elif opcion == "2":
            mensaje_descifrado = descifrado(texto, desplazamiento)
            print(f"Mensaje desencriptado: {mensaje_descifrado}")
main()
