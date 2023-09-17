#Escribir un programa que tome una lista de números ingresada por el usuario y muestre el número más grande de la lista.

lista_numeros = []

def mostrar_menu():
   print('=======================')
   print('|====   M E N U   ====|')
   print('=======================')
   print('[1] Agregar número a la lista')
   print('[2] Ver todos los elementos de la lista')
   print('[3] Ver el número mayor de la lista')
   
   
while True:
  mostrar_menu()
  respuesta = int(input('Su opción: '))
  
  if respuesta == 1:
    print('Ingresa un número a la lista')
    num = int(input('Número: '))
    lista_numeros.append(num)

  elif respuesta == 2:
    for i in lista_numeros:
        print(i)
    

  elif respuesta == 3:
    m = 0
    for i  in lista_numeros:
     if i > m:
      m = i
    print(m)
    

 
  