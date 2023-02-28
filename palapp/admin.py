from django.contrib import admin

from .models import Bancos, TipoDoc, Inmobiliaria, Jefe, Vendedor
from .models import Cliente, Terreno, Tramites, Notaria, Venta, Pagos

from import_export.admin import ImportExportModelAdmin
from import_export import resources

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'vendedor', 'dni', 'appat', 'apmat', 'nomb', 'direccion', 'telfij', 'cel1', 'cel2',
                    'directra', 'pais', 'correo', 'ocupacion', 'percon', 'celcon', 'observ', 'activo', 'usuario_crea']


class InmobiliariaAdmin(admin.ModelAdmin):
    list_display = ['id', 'ruc', 'rassoc', 'direccion', 'correo', 'cel1', 'cel2', 'fecha_inicon', 'activo', 'usuar',
    'fecha_creacion', 'fecha_act']


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


class BancosAdmin(admin.ModelAdmin):
    list_display = ['id', 'rassoc', 'activo', 'fecha_creacion']


class TipoDocAdmin(admin.ModelAdmin):
    list_display = ['id', 'tipodoc', 'activo', 'fecha_creacion']


class VentaAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'y_o', 'doc_cotitular', 'nom_cotitular',  'terreno', 'vendedor', 'notaria', 'banco', 'condvta', 'nro_cont', 'fec_con',
                    'plan_generado', 'preciod', 'precios', 'comision', 'observ', 'usuario_crea', 'foto_pago_com', 'fecha_pago_com',
                    'bco_pag_com', 'tdoc_sun_com', 'doc_pag_com', 'com_pag', 'd_contrato']


class PagosAdmin(admin.ModelAdmin):
    list_display = ['id', 'venta', 'cuota', 'fec_vcto', 'fec_pago', 'preciod', 'precios', 'gastosd', 'gastoss', 'nrooper',
                    'banco', 'observ', 'estado', 'foto_vouc', 'usuario_crea']


class TerrenoResource(resources.ModelResource):
    class Meta:
        model = Terreno


class TerrenoAdmin(ImportExportModelAdmin):
    resource_class = TerrenoResource


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Inmobiliaria, InmobiliariaAdmin)
admin.site.register(Jefe, JefeAdmin)
admin.site.register(Vendedor, VendedorAdmin)
admin.site.register(Terreno, TerrenoAdmin)
admin.site.register(Tramites, TramitesAdmin)
admin.site.register(Notaria, NotariaAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Pagos, PagosAdmin)
admin.site.register(Bancos, BancosAdmin)
admin.site.register(TipoDoc, TipoDocAdmin)