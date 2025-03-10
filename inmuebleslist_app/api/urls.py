from django.contrib import admin
from django.urls import path
# from inmuebleslist_app.api.views import inmueble_list, inmueble_detalle
from inmuebleslist_app.api.views import EdificacionListAV, EdificacionDetalleAV, EmpresaAV,EmpresaAVdetalle, ComentarioDetail, ComentarioList

urlpatterns = [
    path('inmueble/', EdificacionListAV.as_view() , name='listaInmuebles'),
    path('inmueble/<int:pk>', EdificacionDetalleAV.as_view(), name='detalles'),

    path('empresa/', EmpresaAV.as_view() , name='empresa'),
    path('empresa/<int:pk>', EmpresaAVdetalle.as_view(), name='empresa-detalle'),

    path('inmueble/<int:pk>/comentario/', EdificacionDetalleAV.as_view() , name='comentario-list'),
    path('inmueble/comentario/<int:pk>', ComentarioDetail.as_view(), name='comentario-detalle')
]
 