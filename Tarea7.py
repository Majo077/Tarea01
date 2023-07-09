## Ejercicio: Solicitar al usuario una cadena de texto y que se imprima invertida. (Usando la función reversed).

## Definimos una variable 
palabra = input('Ingrese una palabra: ')
print(palabra)
## Luego vamos a invertir esa palabra, llamando a la función reversed y colocando en el argumento el contenido de la variable palabra. 
## Creamos una cadena vacia, punto join y colocamos como argumento el resultado que retorna el objeto reserved. 
palabra_invertida = ''.join(reversed(palabra))
print(palabra_invertida)

