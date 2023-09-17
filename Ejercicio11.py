#11. Escribir una función que tome una lista de números y devuelva una nueva lista que contenga solo los 
#    números que son múltiplos de 3 y 5 al mismo tiempo.

lista_numeros1 = [1, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10, 11, 12, 13, 14, 15, 30, 60]
lista_numeros2 = []

def funcion_vacana(numeros):
    for i in lista_numeros1:
        if (i % 3 == 0 and i % 5 == 0):
            lista_numeros2.append(i)
    return lista_numeros2

print(str(funcion_vacana(lista_numeros1)))