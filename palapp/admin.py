from django.contrib import admin

from .models import Cliente, Inmobiliaria, Jefe, Vendedor
from .models import Terreno, Tramites, Notaria, Venta, Pagos


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'vendedor', 'dni', 'appat', 'apmat', 'nomb', 'direccion', 'telfij', 'cel1', 'cel2',
                    'directra', 'pais', 'correo', 'ocupacion', 'percon', 'celcon', 'observ', 'activo', 'usuario_crea']


class InmobiliariaAdmin(admin.ModelAdmin):
    list_display = ['id', 'ruc', 'rassoc', 'direccion', 'correo', 'cel1', 'cel2', 'fecha_inicon', 'activo', 'usuar']


class JefeAdmin(admin.ModelAdmin):
    list_display = ['id', 'inmobiliaria', 'appat', 'apmat', 'nomb', 'cel1', 'cel2', 'correo', 'activo', 'usuario_crea']


class VendedorAdmin(admin.ModelAdmin):
    list_display = ['id', 'jefe', 'dni','appat', 'apmat', 'nomb', 'dni', 'codagente',  'cel1', 'cel2', 'telfij',
                    'direccion', 'correo', 'fecha_ingreso', 'fecha_cese', 'activo', 'id_usuario_jefe']


class TerrenoAdmin(admin.ModelAdmin):
    list_display = ['id', 'vendedor', 'cliente', 'codigo', 'manzana', 'lote', 'area', 'preciod', 'precios', 'comision', 'lfrente',
                    'mlfrente', 'lder', 'mlder', 'lizq', 'mlizq', 'lfondo', 'mlfondo', 'norte', 'sur', 'este', 'oeste',
                    'observaciones', 'estado', 'fecha_creacion', 'usuario_crea']


class TramitesAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'vendedor', 'descrip', 'por_hacer', 'resultado', 'fec_prox',
                    'lugar', 'nivel', 'observ', 'usuario_crea']


class NotariaAdmin(admin.ModelAdmin):
    list_display = ['id', 'rassoc', 'ruc', 'direccion', 'correo', 'cel1', 'cel2', 'telfij', 'activo',
                    'fecha_creacion', 'usuario_crea']


class VentaAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'terreno', 'vendedor', 'notaria', 'banco', 'condvta', 'nro_cont', 'fec_con',
                    'preciod', 'precios', 'comision', 'observ', 'usuario_crea']


class PagosAdmin(admin.ModelAdmin):
    list_display = ['id', 'venta', 'cuota', 'fec_vcto', 'fec_pago', 'preciod', 'precios', 'gastosd', 'gastoss', 'nrooper',
                    'banco', 'observ', 'estado', 'foto_vouc', 'usuario_crea']


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Inmobiliaria, InmobiliariaAdmin)
admin.site.register(Jefe, JefeAdmin)
admin.site.register(Vendedor, VendedorAdmin)
admin.site.register(Terreno, TerrenoAdmin)
admin.site.register(Tramites, TramitesAdmin)
admin.site.register(Notaria, NotariaAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Pagos, PagosAdmin)


