print('Bienvenido señor trabajador al sistema para calcular su salario en base a horas por semana')

sueldo = int(input('Favor ingrese el valor por una hora de su trabajo : '))
horas_trabajadas = float(input('Favor ingrese el nuemro de horas que trabajo en la semana : '))

salario_semana = sueldo * horas_trabajadas

print(f'El dinero que recibira por las {horas_trabajadas} horas trabajadas es de : $ {salario_semana}')