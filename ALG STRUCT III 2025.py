"""Ingresar numeros y buscar los numros que estan en las posiciones pares"""

"""a=[] ; b=[]
numero = int(input("Ingrese un numero: "))
while (numero !=0):
    a.append(numero)
    numero = int(input("Ingrese un numero: "))

for numero in range (2, len(a),2):
    b.append(a[numero])
    print(b)"""
    



"""Modificar el ejercicio anterior para que luego de ingresar la lista me pida un numero y me indique donde esta -1 si no esta en la lista"""

"""a=[] 

numero = int(input("Ingrese un numero: "))

while (numero !=0):
    a.append(numero)
    numero = int(input("Ingrese un numero: "))

bad=-1
usuario=int(input("Ingrese un numero a buscar: "))
if usuario in a:
    indice =a.index(usuario)
    print(("E nro {usuraio} esta en la lusta de la posicion {indice}"))
else:
    print("El nro no esta en la lista", bad)"""

"""Modificar el ejercicio anterior para que indique cuantas veces se repite un numero sino que arroje -1"""

a=[]

numero = int(input("Ingrese un numero: "))

while (numero !=0):
    a.append(numero)
    numero = int(input("Ingrese un numero: "))

buscar=int(input("Ingrese un numero a buscar: "))
if buscar in a:
    repetido=a.count(buscar)
    print(f"el numero {buscar} se repite {repetido} veces")
else:
    print("-1")