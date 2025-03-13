from django.contrib import admin
from django.urls import path
# from inmuebleslist_app.api.views import inmueble_list, inmueble_detalle
from inmuebleslist_app.api.views import (EdificacionListAV, EdificacionDetalleAV, EmpresaAV,EmpresaAVdetalle,
ComentarioDetail, ComentarioList, ComentarioCreate)

urlpatterns = [
    path('inmueble/', EdificacionListAV.as_view() , name='listaInmuebles'),
    path('inmueble/<int:pk>', EdificacionDetalleAV.as_view(), name='detalles'),

    path('empresa/', EmpresaAV.as_view() , name='empresa'),
    path('empresa/<int:pk>', EmpresaAVdetalle.as_view(), name='empresa-detalle'),

    path('inmueble/<int:pk>/comentario-create/', ComentarioCreate.as_view() , name='comentario-create'),
    path('inmueble/<int:pk>/comentario/', ComentarioList.as_view() , name='comentario-list'),
    path('inmueble/comentario/<int:pk>', ComentarioDetail.as_view(), name='comentario-detalle')
]
 