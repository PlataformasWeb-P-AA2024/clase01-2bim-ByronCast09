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

# Los cantones que tiene establecimientos con 0 número de profesores y 210 estudiantes

establecimientos = session.query(Establecimiento).join(
    Establecimiento.parroquia
).join(
	Parroquia.canton
).filter(
	Establecimiento.numEstudiantes==210,
	Establecimiento.numDocentes==0
).all()

print("Los cantones que tiene establecimientos con 0 número de profesores y 210 estudiantes")
for establecimiento in establecimientos:
	print("Nombre de los Cantones: %s | Numero de estudiantes con 210: %d y Docente 0: %d" 
	   % (establecimiento.parroquia.canton.nombCanton,
	   establecimiento.numEstudiantes,
	   establecimiento.numDocentes))
