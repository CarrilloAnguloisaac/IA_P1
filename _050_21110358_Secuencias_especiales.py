import re

texto = "Bienvenidos a Programaci�n f�cil y bienvenidos al curso de Python."
buscar = re.findall("[c-g]", texto)
print(buscar)

texto = "�Van al zool�gico?"
buscar = re.findall("zo{2}l�gico", texto)
if buscar:
	print("Hay al menos una coincidencia.")
else:
	print("No hay coincidencias.")
	

texto = "La programaci�n es f�cil."
buscar = re.findall("progra..ci�n", texto)
if buscar:
	print("Hay al menos una coincidencia.")
else:
	print("No hay coincidencias.")
	
exto = "Se acerca el invierno."
buscar = re.findall("^Se acerca", texto)
if buscar:
	print("Hay al menos una coincidencia.")
else:
	print("No hay coincidencias.")
