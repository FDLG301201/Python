# 12. Escribir una función que tome una cadena de texto y devuelva el número de palabras que tienen al menos 5 caracteres.

cadena = input('Por favor, escribir lo que plazca: ')

# Utilizando split() sin argumentos para dividir por espacios en blanco
palabras = cadena.split()

def funcion_de_cadena(cadena_texto):
    cont = 0
    for i in palabras:
        if(len(i) >= 5):
            cont+= 1
    
    print('La cantidad de palabras con al menos 6 caracteres es: ' + str(cont))


funcion_de_cadena(cadena)