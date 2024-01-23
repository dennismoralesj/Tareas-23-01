##Programa que identifique el dato que ingreso el usuario

x = input("Ingrese El Dato a corroborar su naturaleza: ")

try:
    valor_entero = int(x)
    print("El dato ingresad es un número entero.")
except ValueError:
    try:
        valor_float = float(x)
        print("El dato ingresado es un número flotante.")
    except ValueError:
        print("El dato ingresado es una cadena de texto")