import re

texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.findall("e", texto)
print(busqueda)

texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.findall("es", texto)
print(busqueda)
