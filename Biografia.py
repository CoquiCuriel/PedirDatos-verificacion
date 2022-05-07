"""
Created on Fri May  6 19:35:32 2022

@author: Ricardo Curiel
"""
print("**"*5 + "Bienvenido, cargando información." + "**"*5)

nombre = input("Ingrese su nombre: ")

while(nombre.isdigit() == True or len(nombre) < 3):
    print("Por favor, ingrese un nombre válido")
    nombre = input()

apellido = input("Ingrese su apellido: ")
while(apellido.isdigit() == True or len(apellido) < 3):
    print("Por favor, ingrese un apellido válido")
    apellido = input()

dia_nacimiento = input("Ingrese su día de nacimiento: ")
while dia_nacimiento.isdigit() == False or int(dia_nacimiento) <= 0 or int(dia_nacimiento) > 31:
    print("ATENCION!! -- Ingrese un dia válido")
    dia_nacimiento = input()

mes_nacimiento = input("Ingrese mes de nacimiento: ")
while (mes_nacimiento.isdigit() == False or int(mes_nacimiento) <= 0 or int(mes_nacimiento) > 12):
    print("ATENCION!! -- Ingrese un mes válido:")
    mes_nacimiento = input()

anio_nacimiento = input("Ingrese su año de natalicio: ")
while(anio_nacimiento.isdigit() == False or int(anio_nacimiento) < 1910 or int(anio_nacimiento) > 2022):
    print("ATENCION!! -- Ingrese un año válido: ")
    anio_nacimiento = input()

fecha_nacimiento = dia_nacimiento+"/"+mes_nacimiento+"/"+anio_nacimiento

calle = input("Ingrese la calle de su dirección: ")
while(calle.isdigit() == True):
    calle = input("ATENCION: Ingrese una calle correcta: ")

numero = input("Ingrese número de su dirección: ")
while(numero.isdigit() != True or int(numero) < 0):
    numero = input("ATENCIÓN: Ingrese un valor válido: ")

#Imprimir datos

print("-"*10 + "Datos cargados" + "-"*10)
print(f"--NOMBRE COMPLETO: {nombre} {apellido}")
print(f"--FECHA DE NACIMIENTO: {fecha_nacimiento}")
print(f"--DIRECCIÓN: {calle} {numero}")