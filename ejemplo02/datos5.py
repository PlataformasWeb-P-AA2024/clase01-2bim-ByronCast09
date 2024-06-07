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

# Las parroquias que tienen establecimientos únicamente en la jornada "Matutina, Vesperina y Nocturna"

establecimientos = session.query(Establecimiento).join(
    Establecimiento.parroquia
).filter(
	Establecimiento.jornada.in_(['Matutina', 'Vesperina', 'Nocturna'])
).all()

print("Las parroquias que tienen establecimientos únicamente en la jornada = Matutina, Vesperina y Nocturna")
for establecimiento in establecimientos:
	print("Nombre de las Parroquias: %s | Jordana Matutina,vespertina y nocturna: %s" 
	   % (establecimiento.parroquia.nombParroquia,
	   establecimiento.jornada))
