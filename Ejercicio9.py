# 9. Escribir una función que tome una lista de números y devuelva la suma de todos los elementos de la lista.

lista_numeros = [1, 2 , 3 , 4 , 5]

def suma_numeros(numeros):
    suma = 0
    for i in numeros:
        suma = suma + i
    
    print(str(suma))

suma_numeros(lista_numeros)