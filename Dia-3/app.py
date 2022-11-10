from flask import Flask
from config import conexion
from models.participantes import ParticipanteModel

app = Flask(__name__)
#formato para las cdenas de conexion de las base de datos:
# dialecto://username:password@host:part/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/flask_sqlalchemy'

#para inicializar mi aplicacion
#configuro mi conexion de sqlalchemy con la aplicacion de flask
conexion.init_app(app)

#indicaremos la creacion de las nuevas tablas que no se encuentren registrados en la base de datos PERO esos modelos tiene que ser utilizado en el proyecto para que pueda crear la tabla en la bd, emitira un error si no logro conectar a la base de datos
def inicializacion():
    #para utilizar el metodo create_all necesita estar dentro de un endpoint o una funcionalidad de flask, en este caso estamos utilizando un metodo llamado before_first_request que se ejecutara antes de realizar la primera peticion a la API
    conexion.create_all()

app.before_first_request(inicializacion)

@app.route('/participantes', methods=['GET'])
def participantes():
    resultado = conexion.session.query(ParticipanteModel).all()
    print(resultado)
    print(resultado[0].nombre)
    print(resultado[0].apellido)
    return{
        'message': 'Los participantes son'
    }

app.run(debug=True)