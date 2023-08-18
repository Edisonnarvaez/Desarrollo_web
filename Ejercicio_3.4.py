print("Bienvenido al sistema para verificar el valor de un traje de acuerdo a la promocion de El harapiento distinguido")
valor_traje = float(input("Ingresa el valor del traje: "))


descuento_superior = 0.15  # 15%
descuento_inferior = 0.08  # 8%

if valor_traje > 2500:
    descuento = valor_traje * descuento_superior
else:
    descuento = valor_traje * descuento_inferior

precio_final = valor_traje - descuento


print(f"El descuento aplicado es de: ${descuento:.2f} ")
print(f"El precio final a pagar es de: ${precio_final:.2f}")

