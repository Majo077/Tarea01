## Ejercicio: Solicitar al usuario una cadena de texto y verificar que sea capicúa o anagrama o palíndromo.

palabra = input('Ingrese una palabra: ')
if str(palabra) == str(palabra)[::-1]:
    print('Es palíndromo, o sea se lee de derecha a izquierda y viceversa')
else:
    print('No es palíndromo o capicúa')

## Sintaxis de corte ::-1  se utiliza con cadenas, lo que va a hacer es invertir la cadena. 




