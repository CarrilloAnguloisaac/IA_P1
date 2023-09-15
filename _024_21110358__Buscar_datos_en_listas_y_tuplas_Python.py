colores = input('Introduce un color:\n')
tupla_colores = ('rojo', 'azul', 'verde', 'amarillo')

if colores in tupla_colores[0]:
	print('El color rojo está admitido')
elif colores in tupla_colores[1]:
	print('El color azul está admitido')
elif colores in tupla_colores[2]:
	print('El color verde está admitido')
elif colores in tupla_colores[3]:
	print('El color amarillo está admitido')
else:
	print('Color no admitido')