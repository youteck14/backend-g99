from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.usuarios import UsuarioModel

class UsuarioRequestDto(SQLAlchemyAutoSchema):
    #pasar atributos a la clase que estamos heredando
    class Meta:
        
        model = UsuarioModel