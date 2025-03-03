from django.contrib import admin
from django.urls import path
# from inmuebleslist_app.api.views import inmueble_list, inmueble_detalle
from inmuebleslist_app.api.views import EdificacionListAV, EdificacionDetalleAV, EmpresaAV

urlpatterns = [
    path('list/', EdificacionListAV.as_view() , name='listaInmuebles'),
    path('empresa/', EmpresaAV.as_view() , name='empresa'),
    path('<int:pk>', EdificacionDetalleAV.as_view(), name='detalles')
]
 