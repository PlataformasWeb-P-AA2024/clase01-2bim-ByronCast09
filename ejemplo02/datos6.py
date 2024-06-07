from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from crear_tablas import *

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera enlace al gestor de base de datos
# para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()
#profe quiso solo ecantones imprimir 
# Los cantones que tienen establecimientos con número de estudiantes tales como: 1, 74, 100
cantones = session.query(Canton).join(
    Canton.parroquias
).join(
    Parroquia.establecimientos
).filter(
    Establecimiento.numEstudiantes.in_([1, 74, 100])
).distinct().all()

print("Los cantones que tienen establecimientos con número de estudiantes tales como: 1, 74, 100")
for canton in cantones:
    print("Nombre del Canton: %s " % (canton.nombCanton))