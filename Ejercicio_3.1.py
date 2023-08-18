print('Bienvenido señor usuario al sistema para determinar cual es el numero mayor de los valores suministrados ')

numero1 = float(input("Ingresa el primer numero: "))
numero2 = float(input("Ingresa el segundo numero: "))

# Comparamos los numeros usando  ">"
if numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}.")
else:
    print(f"{numero2} es mayor que {numero1}.")
