from flask_restful import Resource, request
from dtos.prueba import PruebaDto
from marshmallow.exceptions import ValidationError

class PruebaController(Resource):
    def post(self):
        try:
            data = request.get_json()
            validador = PruebaDto()
            #cargar la informacion a validar
            dataValidadda = validador.load(data)
            print(dataValidadda)

            return {
                'message':'ok'
            }
        #si al momento de hacer la validacion de nuestro DTO falla algun
        #atributo entonces el propio marshmallow emitira un error que lo
        #podremos capturar mediante el except de ValidationError
        except ValidationError as error:
            #args > el atributo donde se almacenara toda la descripcion de los
            #errores
            return{
                'message':'Error al hacer la consulta',
                'content': error.args
            }