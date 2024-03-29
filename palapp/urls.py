
from django.urls import path

from . import views
from .views import Inmoblistar, Jefelistar, Vendedorlistar, Clientelistar, Terrenolistar, Tramiteslistar, Notarialistar
from .views import Pagoslistar, Ventalistar, Bancoslistar, TipoDoclistar
from .views import UpdtInmobiliaria, UpdtCliente, UpdtJefe, UpdtVendedor, UpdtTerreno, UpdtTramite, UpdtNotaria
from .views import UpdtVenta, UpdtPagos, UpdtBanco, UpdtTipoDoc
from .views import InmobiliariaNuevo, InmobiliariaDetalle, JefeDetalle, VendedorDetalle, ClienteDetalle, TerrenoDetalle
from .views import TramitesDetalle, NotarioDetalle, VentaDetalle, gen_cron, ventasbulk, PagosDetalle
from .views import BancosDetalle, TipoDocDetalle, UpdtClientem, Pagosl


app_name = 'palapp'


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
    path('clilistm', Clientelistar.as_view(template_name="palapp/clilistm.html"), name='clilistm'),
    path('addcli', views.add_cliente, name='addcli'),
    path('detcli/<int:pk>', ClienteDetalle.as_view(template_name="palapp/detcli.html"), name='detcli'),
    path('edtcli/<int:pk>', UpdtCliente.as_view(template_name="palapp/edtcli.html"), name='edtcli'),
    path('edtclim/<int:pk>', UpdtClientem.as_view(template_name="palapp/edtclim.html"), name='edtclim'),

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
    path('edtvta/cplan/<int:pk>', gen_cron, name='cplan'),
    # path('lisdpag/<int:pk>', PagosDetalle.as_view(template_name="palapp/lisdpag.html"), name='lisdpag')

    # Pagos x contrato
    path('lispag/<int:id>', views.Pagosl, name='lispag'),
    path('lispag/detpag/<int:pk>', PagosDetalle.as_view(template_name="palapp/detpag.html"), name='detpag'),
    path('lispag/edtpag/<int:pk>', UpdtPagos.as_view(template_name="palapp/edtpag.html"), name='edtpag'),

    # Pagos TODO
    path('lispagt/', Pagoslistar.as_view(template_name="palapp/lispagt.html"), name='lispagt'),
    path('addpag', views.add_pagos, name='addpag'),
    path('detpagt/<int:pk>', PagosDetalle.as_view(template_name="palapp/detpagt.html"), name='detpagt'),
    path('edtpagt/<int:pk>', UpdtPagos.as_view(template_name="palapp/edtpagt.html"), name='edtpagt'),

    # Bancos
    path('lisbco', Bancoslistar.as_view(template_name="palapp/lisbco.html"), name='lisbco'),
    path('addbco', views.add_bancos, name='addbco'),
    path('detbco/<int:pk>', BancosDetalle.as_view(template_name="palapp/detbco.html"), name='detbco'),
    path('edtbco/<int:pk>', UpdtBanco.as_view(template_name="palapp/edtbco.html"), name='edtbco'),

    # Tipos de Documento
    path('listdoc', TipoDoclistar.as_view(template_name="palapp/listdoc.html"), name='listdoc'),
    path('addtdoc', views.add_tipodoc, name='addtdoc'),
    path('dettdoc/<int:pk>', TipoDocDetalle.as_view(template_name="palapp/dettdoc.html"), name='dettdoc'),
    path('edttdoc/<int:pk>', UpdtTipoDoc.as_view(template_name="palapp/edttdoc.html"), name='edttdoc'),

    # Seguridad
    path('profile', views.Profile, name='profile'),
    path('change_password', views.Change_Password, name='change_password'),

    # Mostrar formulario de alta de nuevo registro///// sin uso


    path('nuevo', InmobiliariaNuevo.as_view(template_name='palapp/inmcrear.html'), name='nuevo'),

    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]

