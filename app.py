from flask import Flask
from config import conexion
from flask_migrate import Migrate
from os import environ
from dotenv import load_dotenv
from flask_restful import Api
from models.usuarios import UsuarioModel
from flask_mysqldb import MySQL
from models.tareas import TareaModel
from controllers.usuarioController import UsuariosController
from controllers.pruebaController import PruebaController
#para que puedan ser utilizadas como variables de entorno
load_dotenv()

app = Flask(__name__)

#aca inicializamos la clase Api que nos servira para poder utilizar todos los
#controladores dentro de aplicacion de Flask
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')

#inicializamos la instancia de Flask-SQLAlchemy con las propiedades seteadas en la aplicacion de flask
conexion.init_app(app)
#mysql = MySQL(app)
#Inicializamos la clase Migrate con la configuracion de nuestra base de datos y aplicacion de Flask
migrate = Migrate(app,conexion)

#Declaras todas las rutas que vamos a utilizar mediante los controladores
api.add_resource(UsuariosController, '/usuarios')
api.add_resource(PruebaController,'/prueba')

if __name__ == '__main__':
    app.run(debug=True)