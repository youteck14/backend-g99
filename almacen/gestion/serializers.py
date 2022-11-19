from rest_framework import serializers
from .models import DepartamentoModel

class PruebaSerializer(serializers.Serializer):
    #un serializador es el que transforma la info entrante y saliente
    nombre = serializers.CharField(max_length=40, allow_null=False)
    apellido = serializers.CharField(allow_null=False)

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartamentoModel
        fields = '__all__'#['id','nombre'] > esto salamente usara esas columnas del modelo
        #si quisieramos utilizar todas las columnas exceptuando una o dos (minoria)
        #voy a utilizar todas las columnas menos la columna 'nombre'
        # exclude = ['nombre']
        #NOTA: No se usa las dos , o se usa 'fields' o se usa 'exlude'