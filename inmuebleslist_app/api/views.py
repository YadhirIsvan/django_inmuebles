from rest_framework.response import Response
from inmuebleslist_app.models import Edificacion, Empresa, Comentario
from inmuebleslist_app.api.serializer import EdificacionSerializer, EmpresasAV, ComentarioSerializer
from rest_framework.decorators import api_view
from rest_framework import  status
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

class ComentarioCreate(generics.CreateAPIView):
    serializer_class = ComentarioSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        inmueble = Edificacion.objects.get(pk=pk)
        serializer.save(Edificacion=inmueble)

class ComentarioList(generics.ListCreateAPIView):
    serializer_class =  ComentarioSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comentario.objects.filter(edificacion=pk)

class ComentarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


# class ComentarioList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Comentario.objects.all()
#     serializer_class = ComentarioSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class ComentarioDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Comentario.objects.all()
#     serializer_class = ComentarioSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

class EmpresaVS(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresasAV

# class EmpresaVS(viewsets.ViewSet):
#     def list(request, self):
#         queryset = Empresa.objects.all()
#         serializer = EmpresasAV(queryset, many = True)
#         return Response(serializer.data)

#     def retrive(request, self , pk=None):
#         queryset = Empresa.objects.all()
#         edificacion = get_object_or_404(queryset, pk = pk)
#         serializer = EmpresasAV(edificacion)
#         return  Response(serializer.data)

#     def create(self, request):
#         serializer = EmpresasAV(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def update(self, request, pk):
#         try:
#             empresa = Empresa.objects.get(pk=pk)
#         except Empresa.DoesNotExist:
#             return Response({'error' : 'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = EmpresasAV(empresa, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk):
#         try:
#             empresa  = Empresa.objects.get(pk=pk)            
#         except Empresa.DoesNotExist:
#             return Response({'error': 'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)

#         empresa.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


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

class EmpresaAVdetalle(APIView):
    def get(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk = pk)            
        except Empresa.DoesNotExist:
            return Response({'no se encuntra el inmueble que buscaste'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmpresasAV(empresa, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):

        try:
            empresa = Empresa.objects.get(pk = pk)            
        except Empresa.DoesNotExist:
            return Response({'el inmueble a actulizar no exite'}, status=status.HTTP_404_NOT_FOUND)

        de_serializer = EmpresasAV(empresa, data=request.data, context={'request': request})
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk = pk)
        except Empresa.DoesNotExist:
            return Response({'el inmueble a eliminar no exite'}, status=status.HTTP_404_NOT_FOUND)

        empresa.delete()
        return Response({'elemento eliminado'}, status=status.HTTP_204_NO_CONTENT)

    

    

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
