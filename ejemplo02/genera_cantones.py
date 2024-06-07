from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

from crear_tablas import Canton,Base
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

with open('Listado-Instituciones-Educativas-02.csv', 'r',encoding='utf-8-sig') as file:
    reader = csv.DictReader(file, delimiter='|')
    cantones = {}
    for row in reader:
        codigoCantonJson = int(row['Código División Política Administrativa  Cantón'])
        nombreCantonJson = row['Cantón']
        codDivPoliProvinciaJson = int(row['Código División Política Administrativa Provincia'])
        #verifica si codigo canton ya existe en el diccionario sino crea una nueva instancia en la alse canton
        if codigoCantonJson not in cantones:
            cantones[codigoCantonJson] = Canton(codigoDPoliAdmiCantón=codigoCantonJson, nombCanton=nombreCantonJson,
                                                 codigo_DPoliAdmiProvincia=codDivPoliProvinciaJson)

            
for canton in cantones.values():
    session.add(canton)


session.commit()