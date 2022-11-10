from flask import Flask
from config import conexion
from flask_migrate import Migrate
from os import environ
from dotenv import load_dotenv
from models.usuarios import UsuarioModel
#para que puedan ser utilizadas como variables de entorno
load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')
#inicializamos la instancia de Flask-SQLAlchemy con las propiedades seteadas en la aplicacion de flask
conexion.init_app(app)

#Inicializamos la clase Migrate con la configuracion de nuestra base de datos y aplicacion de Flask
migrate = Migrate(app,conexion)

app.run(debug=True)