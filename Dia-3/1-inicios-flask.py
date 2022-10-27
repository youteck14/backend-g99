from flask import Flask, request
#request > toda la informacion que puedo leer del usuario, dentro de ella tendremos el body
from datetime import datetime
# __name__> muestra si el archivo es el archivo principal del proyecto el valor de '__main__' y si no
#entonces mostrara otro valor
from flask_cors import CORS



usuarios = [{
    'correo': 'sanson121416@gmail.com',
    'nombre': 'yohan',
    'apellido': "Romero"
}]

""" print(__name__) """
app = Flask(__name__)#instancia
#DECLARAR LOS CORS (intercambio de recursos de origen compartido)

CORS(app)

# Endpoint > es cuando definimos una ruta para que puede ser accedida
#si no se define que verbo HTTP puede acceder, entonces el valor por defecto sera GET
@app.route('/',methods = ['GET'])#se modificara solo cuando sea la rota /
def inicio():
    #Controlador> la funcionalidad que tendra mi endpoint
    print('Ingreso al endpoint inicial')
    #Siempre en todo controlador har que retornar algo
    return 'Bienvenido a mi primera API en Flask semana 2'

@app.route('/estado', methods = ['GET'])
def estado():
    hora_servidor = datetime.now().strftime('%Y-%m-%d %I-%M-%S-%p')
    
    return {        
        'estado': True,
        'hora': hora_servidor
    }
#run> sirve para correr nuestro servidor en modo de desarrollo
@app.route('/registrarse',methods=['POST'])
def registro():
    #request.data > el body pero en formato puro(formato bytes)
    print(request.data)
    print(request.get_json())
    #request .get_json() > convierte la informacion entrante en un diccionario para que pueda
    #ser utilizado sin problemas en python
    body = request.get_json()
    #iterar el arreglo de usuarios y validar que no exista un usuario con ese correo proveniente del body

    #body.get('correo')si en el primero no esta esa llave te arroja none, el segundo sale error si no existe
    #body['correo']

    """ for n in range(len(usuarios)):
        if(usuarios['correo'] != body.get['correo']):
            usuarios.append(n)
        else:
            return "El usuario ya esta registrado" """

    for usuario in usuarios:
        print(usuario)
        correo = usuario.get('correo')
        if correo == body.get('correo'):
            return{
                'message': 'El usuario ya esta registrado'
            }

    usuarios.append(body)
    #si no existe entonces agregar ese usuario al arreglo, caso contrario, retornar un mensaje
    #que diga que el usuario ya esta registrado
    return {
        'message': 'Usuario registrado exitosamente.'
    }


@app.route('/listar-usuarios',methods=['GET'])
def listar():
    return {
        'message':'Los usuarios son',
        'content': usuarios
    }
#crear un endpoint que sea '/listar_usuarios' y este devolvera el siguiente resultado
#{message: 'Los usuarios son ', content: [{...}. {...}]}




#si declaramos algo despues del metodo run este nunca se llamara
#porque aca se queda 'pegado' esperando peticiones del ciente
app.run(debug=True)#debug = indicara si guardamos algun archivo dentro del proyecto reiniciara automaticamente el servidor


#TAREA MD-TABLES
#HACER EL FRONTEND DE LA IMAGEN EN TELEGRAM
#FRONTEND DE LA TABLA Y FORMULARIO
#MANDADR MENSAJE PRIVADO DE TODOS LAS TAREAS AL PROFE

