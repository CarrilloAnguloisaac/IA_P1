import re

texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.split(" ", texto)
print(busqueda)

texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.sub(" ",  "-",  texto, 4)
print(busqueda)

texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.sub(" ",  "-",  texto)
print(busqueda)

texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.split(" ", texto, 4)
print(busqueda)

texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.split("es", texto)
print(busqueda)