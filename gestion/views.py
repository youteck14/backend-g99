from rest_framework.generics import CreateAPIView, ListCreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import UsuarioModel, PlatoModel
from .serializers import UsuarioSerializer, PlatoSerializer
#IsAutenticated > Solamente verifica que en la peticion este enviando una token valida
#IsAuthenticatedOrReadOnly > Solamente para los metodos QUE NO SEAN GET pedira una token valida
#IsAdminUser > Verifica que el usuario del token sea un usuario administrador (is_superuser = True)
# AllowAny > Permite el libre acceso a todo el mundo
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from .permissions import SoloAdmin

class RegistroUsuarioApiView(CreateAPIView):

    queryset = UsuarioModel.objects.all()
    serializer_class = UsuarioSerializer

    def post(self,request:Request):
        informacion = self.serializer_class(data=request.data)
        #aqui se valida que todos los datos sean correctos
        es_valida = informacion.is_valid()

        if not es_valida:
            return Response(data={
                'message': 'Error al crear el usuario',
                'content': informacion.errors
            },status=status.HTTP_400_BAD_REQUEST)
        else:
            #Gracias que el serializador es un modelSerializer el metodo
            # save sirve para registrar ese nuevo usuario en la bd
            nuevoUsusario = informacion.save()
            #utilizamos el serializador para convertir el nuevo usuario creado a una data legible
            nuevoUsuarioSerializado = self.serializer_class(instance = nuevoUsusario)
            return Response(data = {
                'message': 'Usuario creado exitosamente, ya se puede logear',
                #contiene todo el valor del registro pero con sus valores ya 
                #registrados en la base de datos(informacion.data)
                'content': nuevoUsuarioSerializado.data
            },status=status.HTTP_201_CREATED)

class PlatosApiView(ListCreateAPIView):
    queryset = PlatoModel.objects.all()
    serializer_class = PlatoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request:Request):
        #podemos pasar dos parametros PERO o e suno o es el otro
        #data > pasar informacion que aun no esta guardada en la bd, eso se usa para hacer la validacion de esa info
        #instance > pasar una INSTANCIA de ese registro que ya se encuentra en la bd, se utiliza para convertir esa informacion en una informacion legible para el client
        data = self.serializer_class(data = request.data)#body
        #raise_exception > si hay algun error, automaticamente detiene todo el proceso y emite el error
        data.is_valid(raise_exception=True)

        nuevoPlato = data.save()

        return Response(data={
            'messasge' : 'plato creado exitosamente',
            'content' : self.serializer_class(instance=nuevoPlato).data#nos devuelve la informacion proveniente de la instancia
            #tom ala finromacion de la bd y devuelveme en forma de diccionario
        })

    def get(self,request:Request):
        #ejecuta el queryset para que otra vez se vuelva a llamar a la extraccion de la informacion
        #platos = self.get_queryset()
        # SELECT¨* FROM platos WHERE disponibilidad = true;
        platos = PlatoModel.objects.filter(disponibilidad = True).all()
        #many > sirve para indicar al serializador que se le pasara un conjunto de instancias y las tiene que iterar para poder serializarlas / desiarizarlas
        platos_serializados = self.serializer_class(instance=platos , many=True)

        return Response(data={
            'message':'Los platos son',
            'content': platos_serializados.data
        })

class PlatoToggleApiView(UpdateAPIView):
    queryset = PlatoModel.objects.all()
    serializer_class = PlatoSerializer
    permission_classes = [IsAuthenticated]
    def put(self, request:Request, id:str):
        #primero busco si existe el plato
        #SELECT * FROM platos WHERE id = ... LIMIT 1;
        platoEncontrado = PlatoModel.objects.filter(id=id).first()

        if platoEncontrado is None:
            return Response(data={
                'message': 'plato no encontrado'
            }, status = status.HTTP_404_NOT_FOUND)
        #actualizare el estado de la disponibilidad
        #la nueva disponibilidad sera la anterior al reves
        platoEncontrado.disponibilidad = not platoEncontrado.disponibilidad

        platoEncontrado.save()

        return Response(data={
            'message': 'plato actualizado exitosamente',
            'content':self.serializer_class(instance=platoEncontrado).data
        }, status = status.HTTP_201_CREATED)

class PlatoUpdateApiView(UpdateAPIView):
    queryset = PlatoModel.objects.all()
    serializer_class = PlatoSerializer
    permission_classes = [IsAuthenticated]


class VistaProtegidaPlatosApiView(ListAPIView):
    queryset = PlatoModel.objects.all()
    serializer_class = PlatoSerializer
    # authentication_classes > indica la forma que se utilizara para autenticar, em este caso no necesitamos indicar ningun autentication ya que estamos utilizando la libreria simple-jwt, este seria su valor por defecto que esta indifcado en el archivo settings.py
    authentication_classes = [JWTAuthentication]

    #me permite agregar permisos a mis metodos de esta vista generica
    #permission_classes = [IsAuthenticated]
    permission_classes = [SoloAdmin]
    def get(self, request:Request):
        #resques.auth > me devolvera lo que se esta utilizando para la autenticacion (la JWT)
        print('El auth es: ', request.auth)
        # request.user > una vez que ya comprobo que el usuario existe y la token es correcta, ahora en el request.user se almacenara el usuario que esta utilizando esa token (gracias al parametro 'USER_ID_CLAIM')
        print('El user es:',request.user)

        return Response(data={
            'message':'Hola',
            'usuario':{
                'id': request.user.id,
                'correo': request.user.correo
            }
        })


