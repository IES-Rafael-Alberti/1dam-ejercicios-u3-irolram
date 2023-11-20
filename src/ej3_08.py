"""Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo"""
def PedirPalabra() -> str:
    
    palabra = input("Escribe una palabra: \n")
    return palabra
    

def palindromo(palabra) -> None:
    if  palabra == palabra[:: -1]:
        print("Es un palidnromo")
    else:
        print("No lo es")

def main():
    palabra = PedirPalabra()
    palindromo(palabra)

if __name__ == "__main__":
    main()
