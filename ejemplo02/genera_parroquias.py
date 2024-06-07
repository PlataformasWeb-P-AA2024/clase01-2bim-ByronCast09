from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

from crear_tablas import Parroquia,Base
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

with open('Listado-Instituciones-Educativas-02.csv', 'r',encoding='utf-8-sig') as file:
    reader = csv.DictReader(file, delimiter='|')
    parroquias = {}
    for row in reader:
        codigoDPAdmiParroquiaJson = int(row['Código División Política Administrativa  Parroquia'])
        nombreParroqJson = row['Parroquia']
        codDivPoliCantonJson = int(row['Código División Política Administrativa  Cantón'])
        if codigoDPAdmiParroquiaJson not in parroquias:
            parroquias[codigoDPAdmiParroquiaJson] = Parroquia(codigoDPoliAdmiParroquia=codigoDPAdmiParroquiaJson, nombParroquia=nombreParroqJson,
                                                 codigoDPoliAdmiCantón=codDivPoliCantonJson)

            
for parroquia in parroquias.values():
    session.add(parroquia)

session.commit()
