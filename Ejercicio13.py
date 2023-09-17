# 13. Escribir una función que tome una lista de palabras y devuelva una nueva lista
# que contenga solo las palabras que son palíndromos (es decir, se leen igual de izquierda a derecha y de derecha a izquierda).

lista_palabras = ['hola', 'adios', 'rayos', 'sol', 'amor', 'casa', 'ana', 'oso']
palindromos = []

def funcion_de_cadena(cadena):
    for i in lista_palabras:
        if(i == i[::-1]):
            palindromos.append(i)

    for e in palindromos:      
        print(e)


funcion_de_cadena(lista_palabras)