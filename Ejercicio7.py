#7. Escribir un programa que tome una lista de números ingresada por el usuario y cree una nueva lista que contenga solo los números pares de la lista original.

lista_numeros = []
lista_numeros_par = []

def menu():
        print('==================== M E N U ======================')
        print('[1] Agregar a la lista')
        print('[2] Ver lista original')
        print('[3] Ver lista de pares')
        print('[4] Salir')
        print('===================================================')


while True:
    menu()
    respuesta = int(input('Seleccione una opción: '))

    if respuesta == 1:
         agregar = input('Número a agregar: ')
         lista_numeros.append(agregar)

    if respuesta == 2:
         for i in lista_numeros:
            print(i)
    
    if respuesta == 3:
         for i in lista_numeros:
              if int(i) % 2 == 0:
                   lista_numeros_par.append(i)
        
         for e in lista_numeros_par:
            print(e)

    elif respuesta == 4:
        break
