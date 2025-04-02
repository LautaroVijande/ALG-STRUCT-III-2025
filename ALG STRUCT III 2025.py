"""Ingresar numeros y buscar los numros que estan en las posiciones pares"""

a=[] ; b=[]
numero = int(input("Ingrese un numero: "))
while (numero !=0):
    a.append(numero)
    numero = int(input("Ingrese un numero: "))

for numero in range (2, len(a),2):
    b.append(a[numero])
    print(b)
    



"""Modificar el ejercicio anterior para que luego de ingresar la lista me pida un numero y me indique donde esta -1 si no esta en la lista"""

a=[] ; b=[]

numero = int(input("Ingrese un numero: "))

while (numero !=0):
    a.append(numero)
    numero = int(input("Ingrese un numero: "))

for numero in range (2, len(a),2):
    b.append(a[numero])
    
print(b)
