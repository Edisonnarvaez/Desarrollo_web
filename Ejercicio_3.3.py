print('Bienvenido al sistema para calcular el precio de lapices')
print('tenga en cuenta que por 1000 o mas unidades se le cobrara 5 euros')
cantidad_lapices = int(input("Ingresa la cantidad de lápices: "))


precio_mayor = 85
precio_menor = 90

if cantidad_lapices >= 1000:
    costo_total = cantidad_lapices * precio_mayor
    print(f"El costo total es de {costo_total} euros.")
else:
    costo_total = cantidad_lapices * precio_menor
    print(f"El costo total es de {costo_total} euros.")