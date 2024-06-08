from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

from crear_tablas import *
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#- A cada cantón pedirle el número de estudiantes

cantones = session.query(Canton).all()

for s in cantones:
    print("Canton: %s Número de estudiantes:%d"% (s.nombCanton,s.numero_estudiantes_canton()))
print("---------------------------------------------\n")
#- A cada provincia perdile el número de docentes

provincias = session.query(Provincia).all()

for s in provincias:
    print("Provincia: %s Número de docentes:%d"% (s.nombProvincia,s.numero_docentes_provincia()))
print("---------------------------------------------\n")
#- A cada parroquia preguntar el número de establecimientos

parroquias = session.query(Parroquia).all()

for s in parroquias:
    print("Parroquia: %s Número de establecimientos:%d"% (s.nombParroquia,s.numero_establecimientos_parroquia()))
print("---------------------------------------------\n")

#- A cada provincia preguntar la lista de parroquias

provincias = session.query(Provincia).all()

for s in provincias:
    print("Provincia: %s\n Parroquias: %s\n"% (s.nombProvincia, s.obtener_lista_parroquias()))
print("---------------------------------------------\n")

#- A cada parroquia preguntarle los tipos jornada de los establecimientos

parroquias = session.query(Parroquia).all()

for s in parroquias:
    print("Parroquia: %s\n Tipo Jornada de Establecimientos: %s\n"% (s.nombParroquia, s.obtener_jornadas_establecimientos()))
