from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from crear_tablas import Establecimiento,Base

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# Todos los establecimientos que pertenecen al Código División Política Administrativa Parroquia con valor 020151 y 020153

establecimientos = session.query(Establecimiento).filter(
    Establecimiento.codigoDPoliAdmiParroquia.in_([20151, 20153])
).all()
print("Todos los establecimientos que pertenecen al Código División Política Administrativa Parroquia con valor 20151 y 20153:")
for establecimiento in establecimientos:
	print("Nombre del establecimiento: %s | Código valor: %d" 
	   % (establecimiento.nombreInstiEducativa,
	   establecimiento.codigoDPoliAdmiParroquia))
