# 6. Escribir un programa que tome una lista de palabras ingresada por el usuario y muestre cuántas palabras comienzan con la letra "a".

lista_palabras = []

def menu():
        print('==================== M E N U ======================')
        print('[1] Agregar a la lista')
        print('[2] Ver lista')
        print('[3] Mostrar palabras que comienzan con la letra A')
        print('[4] Salir')
        print('===================================================')


while True:
    menu()
    respuesta = int(input('Seleccione una opción: '))

    if respuesta == 1:
         agregar = input('Palabra a agregar: ')
         lista_palabras.append(agregar)

    if respuesta == 2:
         for i in lista_palabras:
            print(i)
    
    if respuesta == 3:
         contador = 0
         for i in lista_palabras:
              if i[0].upper() == 'A':
                   contador = contador + 1
         print('La cantidad de palabras con A es = ' + str(contador))

    elif respuesta == 4:
        break


"""
La estructura de control while True en Python crea un bucle infinito.
Significa que el bloque de código dentro del bucle se ejecutará repetidamente hasta que se produzca una interrupción
explícita o una condición de salida.

La estructura de control while True en Python crea un bucle infinito.
Significa que el bloque de código dentro del bucle se ejecutará repetidamente hasta que se
produzca una interrupción explícita o una condición de salida.

"""
    
