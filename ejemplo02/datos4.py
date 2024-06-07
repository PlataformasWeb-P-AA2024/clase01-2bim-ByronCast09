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

# Todos los establecimientos del cantón de Urdaneta y Vinces.

establecimientos = session.query(Establecimiento).join(
    Establecimiento.parroquia
).join(
    Parroquia.canton
).filter(
    Canton.nombCanton.in_(['URDANETA', 'VINCES'])
).all()

print("Todos los establecimientos del cantón de Urdaneta y Vinces.")
for establecimiento in establecimientos:
	print("Nombre del establecimiento: %s | Cantón: %s" 
	   % (establecimiento.nombreInstiEducativa,
	   establecimiento.parroquia.canton.nombCanton))
