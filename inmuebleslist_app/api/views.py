from rest_framework.response import Response
from inmuebleslist_app.models import Edificacion, Empresa
from inmuebleslist_app.api.serializer import EdificacionSerializer, EmpresasAV
from rest_framework.decorators import api_view
from rest_framework import  status
from rest_framework.views import APIView


class EmpresaAV(APIView):
    def get(self, request):
        empresa = Empresa.objects.all()
        serilizer = EmpresasAV(empresa, many=True, context = {'request' : request})
        return Response(serilizer.data)


    def post(self, request):
        desearilizer = EmpresasAV(data = request.data)
        if desearilizer.is_valid():
            desearilizer.save()
            return Response(desearilizer.data)
        else:
            return Response(desearilizer.errors, status=status.HTTP_400_BAD_REQUEST)


class EdificacionListAV(APIView):

    def get(self, request):
        edificacion = Edificacion.objects.all()
        serilizer = EdificacionSerializer(edificacion, many=True)
        return Response(serilizer.data)


    def post(self, request):
        desearilizer = EdificacionSerializer(data = request.data)
        if desearilizer.is_valid():
            desearilizer.save()
            return Response(desearilizer.data)
        else:
            return Response(desearilizer.errors, status=status.HTTP_400_BAD_REQUEST)


class EdificacionDetalleAV(APIView):
    def get(self, request, pk):
        try:
            edificacion = Edificacion.objects.get(pk = pk)            
        except Edificacion.DoesNotExist:
            return Response({'no se encuntra el inmueble que buscaste'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EdificacionSerializer(edificacion)
        return Response(serializer.data)

    def put(self, request, pk):

        try:
            edificacion = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({'el inmueble a actulizar no exite'}, status=status.HTTP_404_NOT_FOUND)

        de_serializer = EdificacionSerializer(edificacion, data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            edificacion = Edificacion.objects.get(pk = pk)
        except Edificacion.DoesNotExist:
            return Response({'el inmueble a eliminar no exite'}, status=status.HTTP_404_NOT_FOUND)

        Edificacion.delete()
        return Response({'elemento eliminado'}, status=status.HTTP_204_NO_CONTENT)



# @api_view(['GET', 'POST'])  
# def inmueble_list(request):
#     if request.method == 'GET':
#         inmueble = Inmueble.objects.all()
#         serializer = InmuebleSerializer(inmueble, many = True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         deserializer=InmuebleSerializer(data = request.data)
#         if deserializer.is_valid():
#             deserializer.save()
#             return Response(deserializer.data)
#         else:
#             return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    



# @api_view(['GET','PUT', 'DELETE'])
# def inmueble_detalle(request, pk):
    
#     if request.method == 'GET':
#         try:
#             inmueble = Inmueble.objects.get(pk=pk)
#             serializer = InmuebleSerializer(inmueble)
#             return Response(serializer.data)
#         except Inmueble.DoesNotExist:
#             return Response({'no existe ningun inmueble con ese id'} , status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'PUT':
#         inmueble = Inmueble.objects.get(pk = pk)
#         de_serializer = InmuebleSerializer(inmueble, data = request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'DELETE':
        
#         try:
#             inmueble = Inmueble.objects.get(pk = pk)
#             inmueble.delete()
#             data = {
#                 "resultado" : True
#             }
#             return Response(data)
#         except Inmueble.DoesNotExist:
#             return Response({'no existe el inmueble que deseas eliminar'}, status=status.HTTP_404_NOT_FOUND)
