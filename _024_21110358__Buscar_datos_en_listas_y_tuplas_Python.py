colores = input('Introduce un color:\n')
tupla_colores = ('rojo', 'azul', 'verde', 'amarillo')

if colores in tupla_colores[0]:
	print('El color rojo est� admitido')
elif colores in tupla_colores[1]:
	print('El color azul est� admitido')
elif colores in tupla_colores[2]:
	print('El color verde est� admitido')
elif colores in tupla_colores[3]:
	print('El color amarillo est� admitido')
else:
	print('Color no admitido')