import re

texto = "Bienvenidos a Programación fácil y bienvenidos al curso de Python."
buscar = re.findall("[c-g]", texto)
print(buscar)

texto = "¿Van al zoológico?"
buscar = re.findall("zo{2}lógico", texto)
if buscar:
	print("Hay al menos una coincidencia.")
else:
	print("No hay coincidencias.")
	

texto = "La programación es fácil."
buscar = re.findall("progra..ción", texto)
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
