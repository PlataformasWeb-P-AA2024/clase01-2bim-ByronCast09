from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
#Base.metadata.create_all(engine)
class Provincia(Base):
    __tablename__ = 'provincias'
    id = Column(Integer, primary_key=True,index=True)
    codigo_DPoliAdmiProvincia = Column(Integer, nullable=False, index=True)
    nombProvincia = Column(String(50), nullable=False)

    def __repr__(self):
        return "Código División Política Administrativa Provincia: %d\n  Nombre de la Provincia=%s\n"% (
                          self.codigo_DPoliAdmiProvincia,
                          self.nombProvincia)
# - A cada provincia perdile el número de docentes
    def numero_docentes_provincia(self):
        return session.query(Establecimiento.numDocentes).join(Parroquia).join(Canton).filter(Canton.codigo_DPoliAdmiProvincia == self.codigo_DPoliAdmiProvincia).count()

#- A cada provincia preguntar la lista de parroquias
    def obtener_lista_parroquias(self):
        parroquias = session.query(Parroquia).join(Canton).filter(Canton.codigo_DPoliAdmiProvincia == self.codigo_DPoliAdmiProvincia).all()
        nombres_parroquias = [parroquia.nombParroquia for parroquia in parroquias]
        cadena = ",".join(nombres_parroquias)
        return cadena
    
class Canton(Base):
    __tablename__ = 'cantones'
    id = Column(Integer, primary_key=True)
    codigoDPoliAdmiCantón = Column(Integer, nullable=False, index=True)
    nombCanton = Column(String(50), nullable=False)
    codigo_DPoliAdmiProvincia = Column(Integer, ForeignKey('provincias.codigo_DPoliAdmiProvincia'), nullable=False,index=True)
    provincia = relationship("Provincia", backref="cantones") #(un Provincia tiene muchos Cantones).
    
    def __repr__(self):
        return "Código División Política Administrativa  Cantón: %d\n  Nombre del Cantón: %s\n  Código División Política Administrativa Provincia: %d"% (
                          self.codigoDPoliAdmiCantón,
                          self.nombCanton,
                          self.codigo_DPoliAdmiProvincia)
    
    # Numero 1 : A cada, canton pedirle el numero de estudiantes
    def numero_estudiantes_canton(self):
        parroquias = session.query(Parroquia).filter_by(codigoDPoliAdmiCantón=self.codigoDPoliAdmiCantón).all()
        total_estudiantes = 0
        for parroquia in parroquias:
            establecimientos = session.query(Establecimiento).filter_by(codigoDPoliAdmiParroquia=parroquia.codigoDPoliAdmiParroquia).all()
            for establecimiento in establecimientos:
                total_estudiantes += establecimiento.numEstudiantes
        return total_estudiantes


class Parroquia(Base):
    __tablename__ = 'parroquias'
    id = Column(Integer, primary_key=True)
    codigoDPoliAdmiParroquia = Column(Integer, nullable=False, index=True)
    nombParroquia = Column(String(100), nullable=False)
    codigoDPoliAdmiCantón = Column(Integer, ForeignKey('cantones.codigoDPoliAdmiCantón'), nullable=False, index=True)
    canton = relationship("Canton", backref="parroquias") #(un Canton tiene muchas Parroquias).
    def __repr__(self):
        return "Codigo División Política Administrativa Parroquia: %d\n  Nombre de la Parroquia: %s\n  Código División Política Administrativa Cantón: %d"% (
                          self.codigoDPoliAdmiParroquia,
                          self.nombParroquia,
                          self.codigoDPoliAdmiCantón)
    #- A cada parroaquia preguntar el número de establecimientos
    def numero_establecimientos_parroquia(self):
        return session.query(Establecimiento).filter_by(codigoDPoliAdmiParroquia=self.codigoDPoliAdmiParroquia).count()
    
     #- A cada parroquia preguntarle los tipos jornada de los establecimientos
    def obtener_jornadas_establecimientos(self):
        establecimientos = session.query(Establecimiento).filter_by(codigoDPoliAdmiParroquia=self.codigoDPoliAdmiParroquia).all()
        tipos_jornada = [establecimiento.jornada for establecimiento in establecimientos]
        cadena = ", ".join(set(tipos_jornada))
        return cadena
#------------------------
class Establecimiento(Base):
    __tablename__ = 'establecimientos'
    id = Column(Integer, primary_key=True)
    codigoAMIE = Column(String(55), nullable=False)
    nombreInstiEducativa = Column(String(80))
    ZonaAdmi = Column(String(80))
    denominaciónDistrito = Column(String(80))
    codigoDistrito = Column(String(70), nullable=False)
    codigoCircuitoEduca = Column(String(70), nullable=False)
    sostenimiento = Column(String(70))
    regimenEscolar = Column(String(70))
    jurisdiccion = Column(String(70))
    tipoEducacion = Column(String(70))
    modalidad = Column(String(70))
    jornada = Column(String(70))
    nivel = Column(String(70))
    etnia = Column(String(70))
    acceso = Column(String(70))
    numEstudiantes = Column(Integer, nullable=False)
    numDocentes = Column(Integer, nullable=False)
    estado = Column(String(70))
    codigoDPoliAdmiParroquia = Column(Integer, ForeignKey('parroquias.codigoDPoliAdmiParroquia'), index=True)
    parroquia = relationship("Parroquia", backref="establecimientos") #(una Parroquia tiene muchos Establecimientos).
    def __repr__(self):
        return ("Codigo AMIE: %s\nNombre de la institución educativa: %s\nZona Administrativa: %s\n"
                "Denominación del Distrito: %s\nCódigo del Distrito: %s\nCódigo del Circuito Educativo: %s\n"
                "Sostenimiento: %s\nRegimen Escolar: %s\nJurisdiccion: %s\nTipo de Educacion: %s\n"
                "Modalidad: %s\nJornada: %s\nNivel: %s\nEtnia: %s\nAcceso: %s\nNumero de Estudiantes: %d\n"
                "Numero de Docentes: %d\nEstado: %s\nCódigo División Política Administrativa Parroquia: %d" % (
                    self.codigoAMIE,
                    self.nombreInstiEducativa,
                    self.ZonaAdmi,
                    self.denominaciónDistrito,
                    self.codigoDistrito,
                    self.codigoCircuitoEduca,
                    self.sostenimiento,
                    self.regimenEscolar,
                    self.jurisdiccion,
                    self.tipoEducacion,
                    self.modalidad,
                    self.jornada,
                    self.nivel,
                    self.etnia,
                    self.acceso,
                    self.numEstudiantes,
                    self.numDocentes,
                    self.estado,
                    self.codigoDPoliAdmiParroquia
                ))

Base.metadata.create_all(engine)