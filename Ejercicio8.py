#8. Escribir una función que tome una temperatura en grados Celsius y la convierta a grados Fahrenheit.

##Formula de Celsius a Farenheit: (1.8 * gradosF) + 32

a = int(input('Ingrese su temperatura es grados Celsius: '))

b = ((1.8 * a) + 32)

print(str(a) + ' grados Celcius equivale a: ' + str(b) + ' grados Fahrenheit')