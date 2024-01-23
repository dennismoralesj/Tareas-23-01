##Programa  que calcule al ingresar la hora indique cuantos segundos han transcurrido del dia

hora = input("Ingrese la horas que desea con el formato (Hora, Minutos): ")
hora, minutos = map(int, hora.split(":"))

segundos = hora * 3600 + minutos * 60

print("La cantidad de segundos que han transcurrido desde la hora ingresada es: ", segundos)

