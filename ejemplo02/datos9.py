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

# Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena "Educación regular" en tipo de educación.

establecimientos = session.query(Establecimiento).join(
    Establecimiento.parroquia
).filter(
	Establecimiento.numDocentes > 40,
	Establecimiento.tipoEducacion == 'Educación regular'
).order_by(
	Parroquia.nombParroquia
).all()

print("Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena Educación regular en tipo de educación.")
for establecimiento in establecimientos:
	print("Nombre de las Parroquias Ordenado: %s | Numero de Profesores: %d | Tipo educación: %s" 
	   % (establecimiento.parroquia.nombParroquia,
	   establecimiento.numDocentes,
	   establecimiento.tipoEducacion))
