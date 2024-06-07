from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

from crear_tablas import Provincia,Base
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

with open('Listado-Instituciones-Educativas-02.csv', 'r',encoding='utf-8-sig') as file:
    reader = csv.DictReader(file, delimiter='|')
    provincias = {}
    for row in reader:
        codigoAdmProvJson = int(row['Código División Política Administrativa Provincia'])
        nombreProvJson = row['Provincia']
        if codigoAdmProvJson not in provincias:
            provincia = Provincia(codigo_DPoliAdmiProvincia=codigoAdmProvJson, nombProvincia=nombreProvJson)
            provincias[codigoAdmProvJson] = provincia
            
for provincia in provincias.values():
    session.add(provincia)

session.commit()
