##Programa que permita operar la formula cuadratica

import cmath
def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = cmath.sqrt(b**2 - 4*a*c)


    x1 = (-b + discriminante) / (2*a)
    x2 = (-b - discriminante) / (2*a)

    return x1, x2

a = float(input("Ingresa el coeficiente de la variable a: "))
b = float(input("Ingresa el coeficiente de la variable b: "))
c = float(input("Ingresa el coeficiente de la variable c: "))


x1, x2 = resolver_ecuacion_cuadratica(a, b, c)

print(f"Las soluciones son: x1 = {x1} y x2 = {x2}")