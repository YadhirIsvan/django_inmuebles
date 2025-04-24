from rest_framework import serializers
from inmuebleslist_app.models import Edificacion, Empresa,Comentario




class ComentarioSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = Comentario
        exclude = ['edificacion']
        #fields = "__all__"


class EdificacionSerializer(serializers.ModelSerializer):
    comentarios = ComentarioSerializer(many = True, read_only = True)
    empresass_nombre = serializers.CharField(source= 'empresa.nombre')
    # longitud_direccion = serializers.SerializerMethodField()
    # longitud_pais = serializers.SerializerMethodField()

    class Meta:
        model = Edificacion
        fields = "__all__"
        # fields = ['id', 'pais', 'activate', 'imagen']
        #exclude = ['id']

# class EmpresasAV(serializers.ModelSerializer):

#     # edificacionlist = EdificacionSerializer(many = True, read_only = True)
#     # edificacionserializer = serializers.StringRelatedField(many = True)
#     edificacionlist = serializers.HyperlinkedRelatedField(
#         many = True,
#         read_only = True, 
#         view_name= 'detalles'
#     )

#     class Meta:
#         model = Empresa
#         fields = "__all__"
#         # fields = ['id', 'pais', 'activate', 'imagen']
#         # exclude = ['id']
    






class EmpresasAV(serializers.ModelSerializer):
# serializers.HyperlinkedModelSerializer
    edificacionlist = EdificacionSerializer(many = True, read_only = True)
    # edificacionserializer = serializers.StringRelatedField(many = True)


    # url = serializers.HyperlinkedIdentityField(view_name="empresa-detalle")  #  Asegura que DRF pueda generar la URL de Empresa


    # edificacionlist = serializers.HyperlinkedRelatedField(
    #     many = True,
    #     read_only = True, 
    #     view_name= 'detalles'
    # )

    class Meta:
        model = Empresa
        fields = "__all__"
        # fields = ['id', 'pais', 'activate', 'imagen']
        # exclude = ['id']
    




# VALIDADORES Y FUNCIONES DIRECTAS A LOS OBJETOS
    # def get_longitud_direccion(seld, object):
    #     cantidad_caracteres = len(object.direccion)
    #     return cantidad_caracteres

    # def get_longitud_pais(seld, object):
    #     cantidad_caracteres_pais = len(object.pais)
    #     return cantidad_caracteres_pais

    # def validate(self, data):
    #     if data['pais'] == data['direccion']:
    #         raise serializers.ValidationError("no puede ser tener el mismo nombre el pais que la direccion")
    #     else:
    #         return data
    
    # def validate_imagen(self, data):
    #     if len(data)  < 2:
    #         raise serializers.ValidationError("la url de la imagen es muy corta")
    #     else:
    #         return data



#--------------HACI ES UNA FORMA DE HACER SERIALIZADORES----------------------

# def column_longitud(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("cadena de caracteres demasiado corta")

# class InmuebleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     direccion = serializers.CharField(validators=[column_longitud])
#     pais = serializers.CharField(validators=[column_longitud])
#     descripcion = serializers.CharField()
#     imagen =  serializers.CharField()
#     activate =serializers.BooleanField()
    
#     def create(self, validate_data):
#         return Inmueble.objects.create(**validate_data)
    
#     def update(self, instance, validated_data):
#         instance.direccion = validated_data.get('direccion', instance.direccion)
#         instance.pais = validated_data.get('pais', instance.pais)
#         instance.descripcion = validated_data.get('descripcion', instance.descripcion)
#         instance.imagen = validated_data.get('imagen', instance.imagen)
#         instance.activate = validated_data.get('activate', instance.activate)
#         instance.save()
#         return instance
    
        
    