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

# Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 090112.

establecimientos = session.query(Establecimiento).filter(
    Establecimiento.codigoDistrito == '090112'
).order_by(
	Establecimiento.sostenimiento
).all()

print("Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 090112.")
for establecimiento in establecimientos:
	print("Nombre de Establecimiento Ordenado por Sostenimiento: %s | Codigo de Distrito: %s" 
	   % (establecimiento.nombreInstiEducativa,
	   establecimiento.codigoDistrito))
