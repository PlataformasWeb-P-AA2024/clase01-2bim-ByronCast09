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
    print(s.numero_estudiantes_canton())

