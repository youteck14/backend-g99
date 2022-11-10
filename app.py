from flask import Flask
from config import conexion
from flask_migrate import Migrate
from os import environ
from dotenv import load_dotenv
from models.usuarios import UsuarioModel
from flask_mysqldb import MySQL
#para que puedan ser utilizadas como variables de entorno
load_dotenv()

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')
app.config['MYSQL_HOST'] = environ.get('MYSQL_HOST')  # None
app.config['MYSQL_USER'] = environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = environ.get('MYSQL_DB')
app.config['MYSQL_PORT'] = int(environ.get('MYSQL_PORT'))
#inicializamos la instancia de Flask-SQLAlchemy con las propiedades seteadas en la aplicacion de flask
#conexion.init_app(app)
mysql = MySQL(app)
#Inicializamos la clase Migrate con la configuracion de nuestra base de datos y aplicacion de Flask
migrate = Migrate(app,conexion)

if __name__ == '__main__':
    app.run(debug=True)