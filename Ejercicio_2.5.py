print('***** Bienvenido al sistema para calcular el area de un terreno *****')

print('Para calcular el area de un terreno triangular favor suministrar los siguientes datos :')

base_triangulo = float(input('favor ingrese el valor de la base del triangulo : '))

altura_triangulo = float(input('favor ingrese el valor de la altura del triangulo : '))

area_triangulo = (base_triangulo*altura_triangulo)/2

print(f'el area del triangulo con base {base_triangulo} y de altura {altura_triangulo} es : {area_triangulo} cm^2')

print('Para calcular el area de un terreno rectangular favor suministrar los siguientes datos :')

base_rectangulo = float(input('favor ingrese el valor de la base del rectangulo : '))

altura_rectangulo = float(input('favor ingrese el valor de la altura del rectangulo : '))

area_rectangulo = base_rectangulo*altura_rectangulo

print(f'el area del rectangulo con base ${base_rectangulo} y de altura {altura_rectangulo} es : {area_rectangulo} cm^2')

area_figura = area_triangulo + area_rectangulo

print('-----------------------------------------------')
print(f'El area total del terreno es {area_figura} cm^2')
print('-----------------------------------------------')