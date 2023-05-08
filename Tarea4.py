## Título: hacer una pequeña calculadora 
## Hacer un programa que sume dos numeros y asegurar que el texto que ingrese el usuario se pueda transformar a numero. 

P1 = input('Ingrese un numero: ')
P2 = input('Ingrese otro numero: ')
if P1.isnumeric() == True and P2.isnumeric() == True:
    print('El texto ingresado se puede convertir a un numero')
    print('El resutado verdadero es')
    print(int(P1) + int(P2)) 
else:
    print('Uno de los valores no se puede convertir a numerico')    

   




