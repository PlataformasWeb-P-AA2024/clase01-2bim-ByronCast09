from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from crear_tablas import *

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# Los establecimientos que tienen como parte de nombre la cadena "UNIDOS

establecimientos = session.query(Establecimiento).filter(
    Establecimiento.nombreInstiEducativa.like('%UNIDOS%')
).all()

#el profe pidio imprimir el nombre de provincia mas
print("Los establecimientos que tienen como parte de nombre la cadena UNIDOS")
for establecimiento in establecimientos:
	print("Nombre de los establecimientos con cadena UNIDOS: %s | Nombre de la provincia: %s" 
	   % (establecimiento.nombreInstiEducativa,establecimiento.parroquia.canton.provincia.nombProvincia))
