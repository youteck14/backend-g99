#serializer legible cuando entra y legible de salida para el frontend
#serializer es como un traductor
from .models import UsuarioModel, PlatoModel
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):

    def save(self):
        #es el que se encarga de guardar el registro en la base de datos
        #1. Crea la instancia de nuestro nuevo usuario
                                    #parametros de un diccionario
        nuevoUsuario = UsuarioModel(**self.validated_data)

        #encripto la password
        #2. genero el hash de la password
        nuevoUsuario.set_password(self.validated_data.get('password'))

        #3. guardamos el usuario en la base de datos
        nuevoUsuario.save()

        return nuevoUsuario

    class Meta:
        fields = '__all__'
        model = UsuarioModel
        #usamos el modelo para no tener que mapear todo denuevo

        #definimos un nuevo atributo llamado extra_kwargs en el cual se realiza
        #mediante un diccionario y se utilizara para indicar parametros adicionales
        #a nuestras columnas
        extra_kwargs = {
            'password':{
                'write_only':True
            },
            'id':{
                'read_only':True
            }
        }
        # con la anterior configuracion estamos indicando que el atributo 'password' solamente sera para escribir mas no para devolver (read) y mienstras que el 'id' sera solamente para lectura, mas nunca se podra utilizara para la escritura (write)

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatoModel
        fields = '__all__'
        #utilizando el atributo extra_kwargs indicar que solamente la 
        #disponibilidad sera de solo lectura
        extra_kwargs = {
            'disponibilidad' : {
                'read_only': True
            }
        }