from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

from configuracion import engine


from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String
# La clase saludo cuando migre la informacion de la base de datos donde toma las clases y se ejevuta
# todas las class que contenga el formato __tablename__ 
class Saludo(Base):
    __tablename__ = 'saludos'
# crea algunas variables
    id = Column(Integer, primary_key=True)
    mensaje = Column(String(200))
    tipo = Column(String(200))


"""
class Saludo2(Base):
    __tablename__ = 'saludo2'
    id = Column(Integer, primary_key=True)
    mensaje = Column(String(200))
    tipo = Column(String(200))
    origen = Column(String(200))
"""

Base.metadata.create_all(engine)
