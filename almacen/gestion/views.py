from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PruebaSerializer, DepartamentoSerializer
from rest_framework import status
from .models import DepartamentoModel

@api_view(http_method_names = ['GET', 'POST'])
def saludar(request: Request):
    #request.dta es el cuerpo (body) que me enviar el cliente
    print(request.data)
    #es la informacion enviada por la URL pero en formato de llave-valor
    print(request.query_params)
    #print(request.data.keys)
    if request.method == 'GET':
        return Response(data={
            'message': 'Bienvenido a mi API'
        },status = 200)
    elif request.method == 'POST':
        body = request.data
        nombre = body.get('nombre')
        # en base al nombre que vamos a recibir por el body en vez de que diga
        return Response(data={
            'message': f'Hola {nombre} '
        })

@api_view(http_method_names = ['GET'])
def parametros(request:Request,nombre):
    return Response(data={
        'message': 'Bienvenido al endpoint de parametros'
    })

class PruebaApiView(ListCreateAPIView):
    #vistas genericas me piden dos atributos sirven para trabajar con modelos de la base de datos, no se suele trabajar informacion aislada
    #serializador_class > DTO que convertia la informacion entrante a tipos de datos conocidos por python y convertia la informacion saliente a tipos de datos conocidos por los JSON
    serializer_class = PruebaSerializer
    #queryset > la informacion que vamos a extraer de nuestra base de datos
    queryset = [{
        'nombre':'Eduardo',
        'apellido':'De Rivero'
    },{
        'nombre':'Raul',
        'apellido':'Martinez',

    },{
        'nombre':'Ximena',
        'apellido':'Recabarren'    
    }]

    def post(self,request: Request):
        print(request.data)
        body = request.data
        serializador = PruebaSerializer(data=body)
        dataValida = serializador.is_valid()
        if not dataValida:
            return Response(data={
            'message':'Data incorrecta',
            #error>mostrara los errores del poque la data es invalida
            'content':serializador.errors
            })
        else:
            #validatred_data > mostrara la data ya validad, osea ya pasada por el filtro del serializado
            print(serializador.validated_data)
            self.queryset.append(serializador.validated_data)
        return Response(data={
            'message':'Usuario agregado exitosamente'
        },status=status.HTTP_201_CREATED)


class DepartamentosApiView(ListCreateAPIView):
    serializer_class = DepartamentoSerializer
    #SELECT * FROM departamentos
    queryset = DepartamentoModel.objects.all()

class DepartamentoApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = DepartamentoSerializer
    queryset = DepartamentoModel.objects.all()

#Realizar el crud pero ahora con los almacenes