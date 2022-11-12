from flask import Flask
from config import conexion
from flask_migrate import Migrate
from os import environ
from dotenv import load_dotenv
from flask_restful import Api
from models.usuarios import UsuarioModel
from flask_mysqldb import MySQL
from models.tareas import TareaModel
from controllers.usuarioController import UsuariosController, UsuarioController
from controllers.pruebaController import PruebaController
from controllers.tareaController import TareasController,TareaController
#para que puedan ser utilizadas como variables de entorno
load_dotenv()

app = Flask(__name__)

#aca inicializamos la clase Api que nos servira para poder utilizar todos los
#controladores dentro de aplicacion de Flask
api = Api(app)

#la conexio a la base de datos que usara SQLALCHEMY para conectarse
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')

#Mostrara todas las consultas en leguaje SQL que se realiza a la base de datos
app.config['SQLALCHEMY_ECHO'] = environ.get('MOSTRAR_SQL')#ESTO ES UN BOOLEAN
#inicializamos la instancia de Flask-SQLAlchemy con las propiedades seteadas en la aplicacion de flask
conexion.init_app(app)
#mysql = MySQL(app)
#Inicializamos la clase Migrate con la configuracion de nuestra base de datos y aplicacion de Flask
migrate = Migrate(app,conexion)

#Declaras todas las rutas que vamos a utilizar mediante los controladores
api.add_resource(UsuariosController, '/usuarios')
api.add_resource(PruebaController,'/prueba')
api.add_resource(UsuarioController, '/usuario/<int:id>')
api.add_resource(TareasController,'/tareas')
api.add_resource(TareaController,'/tarea/<int:usuarioId>')

if __name__ == '__main__':
    app.run(debug=True)