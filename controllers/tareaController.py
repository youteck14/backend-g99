from flask_restful import Resource, request
from config import conexion
from models.tareas import TareaModel
from models.usuarios import UsuarioModel
from dtos.tareaDto import TareaRequestDto

class TareasController(Resource):
    def post(self):
        body = request.get_json()
        try:
            serializador = TareaRequestDto()
            dataSerializada = serializador.load(body)
            #buscar si existe el usuario con ese id, si no existe emitir un eror indicando que el usuario no existe
            existUser = dataSerializada.get('usuarioId')

            usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id=dataSerializada.get('usuarioId')).first()
            if usuarioEncontrado is None:
                raise Exception('Usuario no existe')
            

            nuevaTarea = TareaModel(**dataSerializada)
            conexion.session.add(nuevaTarea)
            conexion.session.commit()
            
            return{
                'message':'Tarea agregada exitosamente'
            }

        except Exception as error:
            return{
                'message':'Error al crear la tarea',
                'content': error.args
            }

class TareaController(Resource):
    def get(self,usuarioId):
        #buscar todas las tareas utilizando el usuarioId y luego serializarlas y devolverlas
        tareasEncontradas = conexion.session.query(TareaModel).filter_by(usuarioId = usuarioId).all()
        serializador = TareaRequestDto(many=True)
        data = serializador.dump(tareasEncontradas)

        return{
            'message':'Las tareas son',
            'content':data
        }