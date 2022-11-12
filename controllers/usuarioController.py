from flask_restful import Resource, request
from config import conexion
from models.usuarios import UsuarioModel
from dtos.usuarioDto import UsuarioRequestDto

class UsuariosController(Resource):
    #los metodos que nosotros queramos utilizar(GET,POST) lo tendremos que definir
    #como metodo de la clase

    def get(self):
        #parecido a un SELECT * FROM usuarios;
        #me devolvera con todas las instancias de la clases UsuarioModel
        #pero las tengo que formatear para poder devolverlas al frontend
        usuarios = conexion.session.query(UsuarioModel).all()

        #si queremos pasarle un conjunto de instancia (lista) al DTO
        serializador = UsuarioRequestDto(many=True)
        # a este metodo le pasamos la informacion proveniente de la base de datos y nos los convertira a un tipo de data que pueda ser legible por el frontend
        #en base al modelo que estamos trabajando en ese DTO hara la conversion de tipos de datos (str, int, float, etc)
        #dump convierte a un diccionario
        # el metodo dump solamente espera recibir  una instancia a la vez
        data = serializador.dump(usuarios)

        #print(usuarios)
        #print(usuarios[0].nombre)
        #hacer un for en el cual se iteren todos los usuarios y cada usuario convertilo a un diccionario que tenga el siguiente formato
        #usuariosFinales = []
        #for usuario in usuarios:           

        #    usuarioDiccionario = {
        #        'id':usuario.id,
        #       'nombre':usuario.nombre,
        #        'correo':usuario.correo,
        #        'telefono':usuario.telefono
        #    }
        #    usuariosFinales.append(usuarioDiccionario)
        #y luego agregarlo a la lista
        
        return{
            'message': 'Los usuarios son: ',
            'content': data
        }
    def post(self):

        body = request.get_json()
        try:
            #instancia de mi DTO de usuario
            serializador = UsuarioRequestDto()
            dataSerializada = serializador.load(body)
            print(dataSerializada)
            #creamos una nueva instancia de mi clase Model
            #para mayor informacion mira el archivo 'repaso_funciones_infinitas.py
            nuevoUsuario = UsuarioModel(**dataSerializada)
            #asigno los valores a los atributos provenientes del body
            #nuevoUsuario.correo = body.get('correo')
            #nuevoUsuario.nombre = body.get('nombre')
            #nuevoUsuario.telefono = body.get('telefono')

            #ahora agregamos a la base de datos ese nuevo registro creado en base a la instancia
            conexion.session.add(nuevoUsuario)
            #guardar de manera permanente la informacion agregada al nuevo usuario
            conexion.session.commit()
            #print(body)
            return{
                'message': 'Usuario creado exitosamente'
            }
        except Exception as error:
            print(error)
            return{
                'message': 'Error al crear el usuario',
                'content': error.args
            }


class UsuarioController(Resource):
    #NOTA: el parametro que nosotros indiquemos al metodo tiene que ser exactamente el mismo que hemos definido en la ruta
    def get(self,id):
        #devolver un solo usaurio
        # Select * from usuarios where id=2 limit 1;
        usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id=id).first()
        # utilizando el UsuarioRequestDto pasarle el usuarioEncontrado y devolver esa informacion
        serializador = UsuarioRequestDto()
        data = serializador.dump(usuarioEncontrado)
        return {
            'content': data
        }


    def put(self,id):
        try:
            #Buscare ese usuario por el id
            usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id=id).first()
            if usuarioEncontrado is None:
                raise Exception('Usuario no existe')

            body = request.get_json()
            serializador = UsuarioRequestDto()
            data = serializador.load(body)

            #podemos utilizar un try_except dentro de otro pero este funcionara solamente para el codigo que esta dentro del try y cada uno actuara de manera independiente

            #si el usuario no me envia el telefono entonces conservar el valor anterior PERO si me enviar el valor 'null' ahi si le enviamos el telefono
            telefono = usuarioEncontrado-telefono
            try:
                #si la llave 'telefono' no existe emitira un error por lo que ingresara al except y por ende, en este caso no haremos nada
                telefono = data['telefono']
            except:
                pass

            #aca sobreescribimos la informacion nueva del usuario
            usuarioEncontrado.nombre = data.get('nombre')
            usuarioEncontrado.correo = data.get('correo')
            usuarioEncontrado.telefono = data.get('telefono')

            #guardamos la informacion
            conexion.session.commit()
            return{
                'message': 'Usuario actualizado exitosamente'
            }
        except Exception as error:
            return {
                'message': 'Error al actualizar el usuario',
                'content':error.args
            }
    def delete(self,id):
        try:
            #buscamos al usuario
            usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id=id).first()
            #si no hay el usuario emitiremos un error
            if usuarioEncontrado is None:
                raise Exception('Usuario no existe')
            #asi eliminamos el usuario de la base de datos
            conexion.session.delete(usuarioEncontrado)
            #aqui comfirmamos la eliminacion de manera permanente
            conexion.session.commit()
            return {
                'message':'El usuario se elimino exitosamente'
            }
        except Exception as error:
            return{
                'message': 'Error al eliminar el usuario',
                'content': error.args
            }
