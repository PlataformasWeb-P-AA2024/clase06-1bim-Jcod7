from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from crear_base import Docente

from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de
# la entidad docentes
docentes = session.query(Docente).all() # [docente1, docente2, docente3]

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de todos los Docentes")
for s in docentes:
    print("%s %s" % (s.nombre,s.ciudad))
    print("---------")

# Obtener todos los registros de
# la tabla docentes que tengan como valor en
# el atributo especifico
docentes_dos = session.query(Docente).filter(Docente.ciudad=="Loja").all()
print(docentes_dos)

# Consulta de todos los docentes en la ciudad de Loja, ordenados por nombre
docentes = session.query(Docente).filter(Docente.ciudad=="Loja").order_by(Docente.nombre).all()
print(docentes)

# Consulta de todos los docentes cuya ciudad no es None, ordenados por nombre
docentes = session.query(Docente).filter(Docente.ciudad!=None).order_by(Docente.nombre).all()
print(docentes)

# Consulta de todos los docentes en la ciudad de Loja y que tienen un nombre definido, ordenados por nombre
docentes = session.query(Docente).filter(Docente.ciudad=="Loja", Docente.nombre!=None).order_by(Docente.nombre).all()
print(docentes)

# Consulta de todos los docentes cuya ciudad contiene "oja" y que tienen un nombre definido, ordenados por nombre
docentes = session.query(Docente).filter(Docente.ciudad.like("%oja%"), Docente.nombre!=None).order_by(Docente.nombre).all()
print(docentes)

# Uso de and_ para combinar condiciones: Consulta de todos los docentes cuya ciudad contiene "oja" y que tienen un nombre definido, ordenados por nombre
docentes = session.query(Docente).filter(and_(Docente.ciudad.like("%oja%"), Docente.nombre!=None)).order_by(Docente.nombre).all()
print(docentes)

# Uso de in_ para consultar docentes cuyo apellido está en una lista específica, ordenados por nombre
docentes = session.query(Docente).filter(Docente.apellido.in_(['Minga', 'Borrero'])).order_by(Docente.nombre).all()
print(docentes)

# Uso de or_ para consultar docentes cuyo apellido es "Minga" o "García", ordenados por nombre
docentes = session.query(Docente).filter(or_(Docente.apellido=="Minga", Docente.apellido=="García")).order_by(Docente.nombre).all()
print(docentes)


