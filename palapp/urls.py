
from django.urls import path

from . import views
from .views import Inmoblistar, Jefelistar, Vendedorlistar, Clientelistar, Terrenolistar, Tramiteslistar, Notarialistar
from .views import Pagoslistar, Ventalistar
from .views import UpdtInmobiliaria, UpdtCliente, UpdtJefe, UpdtVendedor, UpdtTerreno, UpdtTramite, UpdtNotaria
from .views import UpdtVenta, UpdtPagos
from .views import InmobiliariaNuevo, InmobiliariaDetalle, JefeDetalle, VendedorDetalle, ClienteDetalle, TerrenoDetalle
from .views import TramitesDetalle, NotarioDetalle, VentaDetalle, PagosDetalle

app_name = 'palapp'

# path('search/', views.search, name='search')

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    # Inmobiliaria
    path('inmlist', Inmoblistar.as_view(template_name="palapp/inmlist.html"), name='inmlist'),
    path('padd', views.add_inmobiliaria, name='padd'),
    path('detalle/<int:pk>', InmobiliariaDetalle.as_view(template_name="palapp/detalle.html"), name='detalle'),
    path('editar/<int:pk>', UpdtInmobiliaria.as_view(template_name="palapp/editar.html"), name='editar'),

    # Jefe
    path('jeflist', Jefelistar.as_view(template_name="palapp/jeflist.html"), name='jeflist'),
    path('addjef', views.add_jefe, name='addjef'),
    path('detjef/<int:pk>', JefeDetalle.as_view(template_name="palapp/detjef.html"), name='detjef'),
    path('edtjef/<int:pk>', UpdtJefe.as_view(template_name="palapp/edtjef.html"), name='edtjef'),

    # Vendedor
    path('venlist', Vendedorlistar.as_view(template_name="palapp/venlist.html"), name='venlist'),
    path('addven', views.add_vendedor, name='addven'),
    path('detven/<int:pk>', VendedorDetalle.as_view(template_name="palapp/detven.html"), name='detven'),
    path('edtven/<int:pk>', UpdtVendedor.as_view(template_name="palapp/edtven.html"), name='edtven'),

    # Cliente
    path('clilist', Clientelistar.as_view(template_name="palapp/clilist.html"), name='clilist'),
    path('addcli', views.add_cliente, name='addcli'),
    path('detcli/<int:pk>', ClienteDetalle.as_view(template_name="palapp/detcli.html"), name='detcli'),
    path('edtcli/<int:pk>', UpdtCliente.as_view(template_name="palapp/edtcli.html"), name='edtcli'),

    # Terrenos
    path('terlist', Terrenolistar.as_view(template_name="palapp/terlist.html"), name='terlist'),
    path('addter', views.add_terreno, name='addter'),
    path('deter/<int:pk>', TerrenoDetalle.as_view(template_name="palapp/deter.html"), name='deter'),
    path('plano', Terrenolistar.as_view(template_name="palapp/plano.html"), name='plano'),
    path('detmap/<int:pk>', TerrenoDetalle.as_view(template_name="palapp/detmap.html"), name='detmap'),
    path('edtterr/<int:pk>', UpdtTerreno.as_view(template_name="palapp/edtterr.html"), name='edtterr'),

    # Gestion de ventas
    path('tralist', Tramiteslistar.as_view(template_name="palapp/tralist.html"), name='tralist'),
    path('addtra', views.add_tramites, name='addtra'),
    path('dettra/<int:pk>', TramitesDetalle.as_view(template_name="palapp/dettra.html"), name='dettra'),
    path('edttra/<int:pk>', UpdtTramite.as_view(template_name="palapp/edttra.html"), name='edttra'),

    # Notarias
    path('lisnot', Notarialistar.as_view(template_name="palapp/lisnot.html"), name='lisnot'),
    path('addnot', views.add_notaria, name='addnot'),
    path('detnot/<int:pk>', NotarioDetalle.as_view(template_name="palapp/detnot.html"), name='detnot'),
    path('edtnot/<int:pk>', UpdtNotaria.as_view(template_name="palapp/edtnot.html"), name='edtnot'),

    # Cierre de Venta
    path('lisvta', Ventalistar.as_view(template_name="palapp/lisvta.html"), name='lisvta'),
    path('addvta', views.add_venta, name='addvta'),
    path('detvta/<int:pk>', VentaDetalle.as_view(template_name="palapp/detvta.html"), name='detvta'),
    path('edtvta/<int:pk>', UpdtVenta.as_view(template_name="palapp/edtvta.html"), name='edtvta'),

    # Pagos
    path('lispag', Pagoslistar.as_view(template_name="palapp/lispag.html"), name='lispag'),
    path('addpag', views.add_pagos, name='addpag'),
    path('detpag/<int:pk>', PagosDetalle.as_view(template_name="palapp/detpag.html"), name='detpag'),
    path('edtpag/<int:pk>', UpdtPagos.as_view(template_name="palapp/edtpag.html"), name='edtpag'),

    # Seguridad
    path('profile', views.Profile, name='profile'),
    path('change_password', views.Change_Password, name='change_password'),

    # Mostrar formulario de alta de nuevo registro///// sin uso


    path('nuevo', InmobiliariaNuevo.as_view(template_name='palapp/inmcrear.html'), name='nuevo'),

    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]