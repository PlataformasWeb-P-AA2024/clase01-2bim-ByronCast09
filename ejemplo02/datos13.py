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

# Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores y régimen escolar igual Costa.

establecimientos = session.query(Establecimiento).filter(
    Establecimiento.numDocentes > 100,
	Establecimiento.regimenEscolar == 'COSTA'
).order_by(
	Establecimiento.numDocentes
).all()

print("Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores y régimen escolar igual Costa.")
for establecimiento in establecimientos:
	print("Nombre de Establecimiento Ordenado por Num.Profesores: %s | numero de Estudiantes: %d |Numero Profesores: %d | Regimen Escolar: %s" 
	   % (establecimiento.nombreInstiEducativa,
	   establecimiento.numEstudiantes,
	   establecimiento.numDocentes,
	   establecimiento.regimenEscolar))
