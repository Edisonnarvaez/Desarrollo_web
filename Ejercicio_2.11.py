print('Bienvenido señor usuario al sistema para el calculo del volumen de un recipiente cubico')

lado_1=int(input('Favor ingrese la medida del lado 1 en metros del recipiente (alberca) '))

lado_2=int(input('Favor ingrese la medida del lado 2 en metros del recipiente (alberca) '))

lado_3=int(input('Favor ingrese la medida del lado 3 en metros del recipiente (alberca) '))

valor=int(input('Favor ingrese el valor en pesos del metro cubico de agua '))


volumen=lado_1*lado_2*lado_3

pago=volumen*valor

print(f'El Volumen del recipiente (Alberca) es de {volumen} por lo que debera pagar {pago}')

