from marshmallow import Schema, fields

#DTO (Data Transfer Object) - Objetos de Transferencia de datos) manual

class PruebaDto(Schema):
    #el DTO no solamente sirve para validar la informacion que hemos dfeinido, sino que ademas validara alguna informacion extra que no vamos a utilizar
    id = fields.Int()
    nombre = fields.Str(required=True , error_messages={'required':'Este campo es obligatorio'})
    correo = fields.Email(error_messages={'invalid':'No es un correo valido'})
