from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

from crear_tablas import Establecimiento,Parroquia,Base
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

with open('Listado-Instituciones-Educativas-02.csv', 'r',encoding='utf-8-sig') as file:
    reader = csv.DictReader(file, delimiter='|')
    establecimientos = {}
    for row in reader:
        try:
            codigoAMIEJson = row['Código AMIE']
            nombreInstiEducativaJson = row['Nombre de la Institución Educativa']
            ZonaAdmiJson = row['Zona Administrativa']
            denominaciónDistritoJson = row['Denominación del Distrito']
            codigoDistritoJson = row['Código de Distrito']
            codigoCircuitoEducaJson = row['Código de Circuito Educativo']
            sostenimientoJson = row['Sostenimiento']
            regimenEscolarJson = row['Régimen Escolar']
            jurisdiccionJson = row['Jurisdicción']
            tipoEducacionJson = row['Tipo de Educación']
            modalidadJson = row['Modalidad']
            jornadaJson = row['Jornada']
            nivelJson = row['Nivel']
            etniaJson = row['Etnia']
            accesoJson = row['Acceso (terrestre/ aéreo/fluvial)']
            
            numEstudiantesJson = int(row['Número de estudiantes'])
            numDocentesJson = int(row['Número de docentes'])
            estadoJson = row['Estado']
            codigoDPoliAdmiParroquiaJson = int(row['Código División Política Administrativa  Parroquia'])
            
            parroquia = session.query(Parroquia).filter_by(codigoDPoliAdmiParroquia=codigoDPoliAdmiParroquiaJson).one()
            
            #parroquia = session.query(Parroquia).filter_by(codigoDPoliAdmiParroquia=codigoDPoliAdmiParroquiaJson).first()

            if codigoAMIEJson not in establecimientos:
                establecimientos[codigoAMIEJson] = Establecimiento(
                    codigoAMIE=codigoAMIEJson,
                    nombreInstiEducativa=nombreInstiEducativaJson,
                    ZonaAdmi=ZonaAdmiJson,
                    denominaciónDistrito=denominaciónDistritoJson,
                    codigoDistrito=codigoDistritoJson,
                    codigoCircuitoEduca=codigoCircuitoEducaJson,
                    sostenimiento=sostenimientoJson,
                    regimenEscolar=regimenEscolarJson,
                    jurisdiccion=jurisdiccionJson,
                    tipoEducacion=tipoEducacionJson,
                    modalidad=modalidadJson,
                    jornada=jornadaJson,
                    nivel=nivelJson,
                    etnia=etniaJson,
                    acceso=accesoJson,
                    numEstudiantes=numEstudiantesJson,
                    numDocentes=numDocentesJson,
                    estado=estadoJson,
                    parroquia=parroquia
                )

        except KeyError as e:
            print(f"Error: Columna no encontrada  {e} en CSV.")
        except ValueError as e:
            print(f"Error: Invalid data format in CSV file: {e}")

            
for establecimiento in establecimientos.values():
    session.add(establecimiento)

session.commit()
