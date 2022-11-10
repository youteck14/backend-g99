# las tablas se crean en forma de clases
from config import conexion
from sqlalchemy import Column, types

class ParticipanteModel(conexion.Model):
    #Ahora esta clase tendra un comportamiento como si fuera una tabla, es decir todos sus atributos formaran columnas
    id = Column(type_ = types.Integer, autoincrement=True, primary_key = True)
    nombre = Column(type_ = types.String(length=45), nullable=False)
    apellido = Column(type_ = types.String(length=50), nullable=False)

    # con el atributo __tablename__ sirve para indicar como se llamara esta table en la base de datos
    __tablename__ = 'participantes'