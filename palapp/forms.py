from django import forms
from django.forms import ModelForm
from django.utils import timezone
from .models import Inmobiliaria, Jefe, Vendedor, Cliente, Terreno, Tramites, Notaria, Venta, Pagos


class InmobiliariaForm(ModelForm):

    ruc = forms.CharField(label="RUC", max_length=11, widget = forms.TextInput(attrs={'class':'form-control'}))
    rassoc = forms.CharField(label="Razón Social", max_length=80, widget = forms.TextInput(attrs={'class':'form-control'}))
    direccion = forms.CharField(max_length=150, widget = forms.TextInput(attrs={'class':'form-control'}))
    correo = forms.EmailField(max_length=150, widget = forms.TextInput(attrs={'class':'form-control'}))
    telfij = forms.CharField(label="Tel.Fijo", required=False, max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cel1 = forms.CharField(label="Nro.Celular 1", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cel2 = forms.CharField(label="Nro.Celular 2", required=False, max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_inicon = forms.DateField(label="Fecha de Inicio de Contrato", required=True, widget=forms.DateInput(attrs={'class': 'form-control'}))
    fecha_creacion = forms.DateTimeField(disabled=True, initial=timezone.now())

    class Meta:
        model = Inmobiliaria
        fields = ("ruc", "rassoc", "direccion", "correo", "telfij", "cel1", "cel2", "fecha_inicon",  "fecha_creacion")


class JefeForm(ModelForm):

    appat = forms.CharField(label="Apellido Paterno", max_length=150, widget = forms.TextInput(attrs={'class':'form-control'}))
    apmat = forms.CharField(label="Apellido Materno", max_length=150, widget = forms.TextInput(attrs={'class':'form-control'}))
    nomb = forms.CharField(label="Nombres", max_length=150, widget = forms.TextInput(attrs={'class':'form-control'}))
    correo = forms.EmailField(max_length=150, widget = forms.TextInput(attrs={'class':'form-control'}))
    telfij = forms.CharField(label="Tel.Fijo", required=False, max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cel1 = forms.CharField(label="Nro.Celular 1", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cel2 = forms.CharField(label="Nro.Celular 2", required=False, max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_creacion = forms.DateTimeField(disabled=True, initial=timezone.now())

    class Meta:
        model = Jefe
        fields = ("inmobiliaria", "appat", "apmat", "nomb", "correo", "telfij", "cel1", "cel2", "fecha_creacion")


class VendedorForm(ModelForm):

    appat = forms.CharField(label="Apellido Paterno", max_length=150, widget = forms.TextInput(attrs={'class':'form-control'}))
    apmat = forms.CharField(label="Apellido Materno", required=False, max_length=150, widget = forms.TextInput(attrs={'class':'form-control'}))
    nomb = forms.CharField(label="Nombres", max_length=150, widget = forms.TextInput(attrs={'class':'form-control'}))
    dni = forms.CharField(label="D.N.I.", max_length=8, widget = forms.TextInput(attrs={'class':'form-control'}))
    direccion = forms.CharField(label="Dirección", widget = forms.TextInput(attrs={'class':'form-control'}))
    codagente = forms.CharField(label="Cod.Agente", max_length=20, required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    correo = forms.EmailField(max_length=150, widget = forms.TextInput(attrs={'class':'form-control'}))
    telfij = forms.CharField(label="Tel.Fijo", required=False, max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cel1 = forms.CharField(label="Nro.Celular 1", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cel2 = forms.CharField(label="Nro.Celular 2", required=False, max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_ingreso = forms.DateField(label="Fecha de Ingreso", required=True, widget=forms.DateInput(attrs={'class': 'form-control'}))
    fecha_cese = forms.DateField(label="Fecha de Cese", required=False, widget=forms.DateInput(attrs={'class': 'form-control'}))
    fecha_creacion = forms.DateTimeField(disabled=True, initial=timezone.now())

    class Meta:
        model = Vendedor
        fields = ("jefe", "id_usuario_jefe", "dni", "appat", "apmat", "nomb", "direccion", "codagente", "correo", "telfij", "cel1", "cel2",
                  "fecha_ingreso", "fecha_cese",  "fecha_creacion")


class ClienteForm(ModelForm):

    appat = forms.CharField(label="Apellido Paterno", max_length=150, widget = forms.TextInput(attrs={'class':'form-control'}))
    apmat = forms.CharField(label="Apellido Materno", required=False, max_length=150, widget = forms.TextInput(attrs={'class':'form-control'}))
    nomb = forms.CharField(label="Nombres", max_length=150, widget = forms.TextInput(attrs={'class':'form-control'}))
    dni = forms.CharField(label="D.N.I.", max_length=8, widget = forms.TextInput(attrs={'class':'form-control'}))
    direccion = forms.CharField(label="Dirección Casa", widget = forms.TextInput(attrs={'class':'form-control'}))
    directra = forms.CharField(label="Dirección Trabajo", required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    pais = forms.CharField(label="Pais", max_length=80, widget = forms.TextInput(attrs={'class':'form-control'}))
    percon = forms.CharField(label="Persona de contacto", required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    correo = forms.EmailField(max_length=150, widget = forms.TextInput(attrs={'class':'form-control'}))
    telfij = forms.CharField(label="Tel.Fijo", required=False, max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cel1 = forms.CharField(label="Nro.Celular 1", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cel2 = forms.CharField(label="Nro.Celular 2", required=False, max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    celcon = forms.CharField(label="Celular Contacto", required=False, max_length=15, widget = forms.TextInput(attrs={'class':'form-control'}))
    ocupacion = forms.CharField(label="Ocupación", max_length=50, widget = forms.TextInput(attrs={'class':'form-control'}))
    observ = forms.CharField(label="Observaciones", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_creacion = forms.DateTimeField(disabled=True, initial=timezone.now())

    class Meta:
        model = Cliente
        fields = ("vendedor", "dni", "appat", "apmat", "nomb", "direccion", "directra", "pais",
                  "correo", "telfij", "cel1", "cel2", "ocupacion", "percon", "celcon", "observ",
                  "fecha_creacion")


class TerrenoForm(ModelForm):

    codigo = forms.CharField(label="Código", max_length=10, widget = forms.TextInput(attrs={'class':'form-control'}))
    manzana = forms.CharField(label="Manzana", max_length=2, widget = forms.TextInput(attrs={'class':'form-control'}))
    lote = forms.IntegerField(label="Lote", widget = forms.NumberInput(attrs={'class':'form-control'}))
    area = forms.DecimalField(label="Area m2", widget = forms.NumberInput(attrs={'class':'form-control'}))
    preciod = forms.DecimalField(label="Precio de Venta US$", widget = forms.NumberInput(attrs={'class':'form-control'}))
    precios = forms.DecimalField(label="Precio de Venta S/", required=False, initial=0, widget = forms.NumberInput(attrs={'class':'form-control'}))
    comision = forms.DecimalField(label="% Comisión", widget = forms.NumberInput(attrs={'class':'form-control'}))
    lfrente = forms.CharField(label="Limite de Frente", required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    mlfrente = forms.DecimalField(label="Mts Lin. de Frente", required=False, widget = forms.NumberInput(attrs={'class':'form-control'}))
    lder = forms.CharField(label="Limite Derecho",  required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    mlder = forms.CharField(label="Mts Lin. Derecha", required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    lizq = forms.CharField(label="Limite Izquierda",  required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    mlizq = forms.CharField(label="Mts Lin. Izquierda", required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    lfondo = forms.CharField(label="Limite Fondo",  required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    mlfondo = forms.CharField(label="Mts Lin. Fondo", required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    norte = forms.CharField(label="Norte", required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    sur = forms.CharField(label="Sur",  required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    este = forms.CharField(label="Este", required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    oeste = forms.CharField(label="Oeste", required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    observaciones = forms.CharField(label="Observaciones", required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    fecha_creacion = forms.DateTimeField(disabled=True, initial=timezone.now())

    class Meta:
        model = Terreno
        fields = ("vendedor", "cliente", "codigo", "manzana", "lote", "area", "preciod", "precios", "comision", "lfrente",
                  "mlfrente", "lder", "mlder", "lizq", "mlizq", "lfondo", "mlfondo", "norte", "sur", "este", "oeste",
                  "observaciones", "estado", "fecha_creacion")


class TramitesForm(ModelForm):

    descrip = forms.CharField(label="Descripción", widget = forms.TextInput(attrs={'class':'form-control'}))
    resultado = forms.CharField(label="Resultado",  widget = forms.TextInput(attrs={'class':'form-control'}))
    fec_prox = forms.DateTimeField(label="Fecha Próximo Trámite",  initial=timezone.now(), widget = forms.DateTimeInput(attrs={'class':'form-control'}))
    observ = forms.CharField(label="Observaciones", required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    fecha_creacion = forms.DateTimeField(disabled=True, initial=timezone.now())

    class Meta:
        model = Tramites
        fields = ("cliente", "terreno", "vendedor", "descrip", "resultado", "nivel", "por_hacer", "fec_prox",  "lugar",
                  "observ", "fecha_creacion")


class NotariaForm(ModelForm):

    ruc = forms.CharField(label="R.U.C", max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))
    rassoc = forms.CharField(label="Razon Social", max_length=150, widget = forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(label="Dirección", widget=forms.TextInput(attrs={'class': 'form-control'}))
    correo = forms.EmailField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telfij = forms.CharField(label="Tel.Fijo", required=False, max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cel1 = forms.CharField(label="Nro.Celular 1", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cel2 = forms.CharField(label="Nro.Celular 2", required=False, max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_creacion = forms.DateTimeField(disabled=True, initial=timezone.now())

    class Meta:
        model = Notaria
        fields = ("ruc", "rassoc", "direccion",  "correo", "telfij", "cel1", "cel2", "fecha_creacion")


class VentaForm(ModelForm):

    banco = forms.CharField(label="Banco", required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    nro_cont = forms.CharField(label="Nro.Contrato",  widget = forms.TextInput(attrs={'class':'form-control'}))
    fec_con = forms.DateTimeField(label="Fecha Contrato",  initial=timezone.now(), widget = forms.DateTimeInput(attrs={'class':'form-control'}))
    preciod = forms.DecimalField(label="Precio de Venta US$", widget = forms.NumberInput(attrs={'class':'form-control'}))
    precios = forms.DecimalField(label="Precio de Venta S/", required=False, initial=0, widget = forms.NumberInput(attrs={'class':'form-control'}))
    comision = forms.DecimalField(label="% Comisión", widget = forms.NumberInput(attrs={'class':'form-control'}))
    observ = forms.CharField(label="Observaciones", required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    aprobado = forms.Select(attrs={'class':'form-control'})
    fecha_creacion = forms.DateTimeField(disabled=True, initial=timezone.now())

    class Meta:
        model = Venta
        fields = ("cliente", "terreno", "vendedor", "notaria", "banco", "condvta", "nro_cont", "fec_con", "preciod",  "precios",
                  "comision", "observ", "aprobado", "fecha_creacion")


class PagosForm(ModelForm):

    fec_vcto = forms.DateTimeField(label="Fecha Vencimiento",  initial=timezone.now(), widget = forms.DateTimeInput(attrs={'class':'form-control'}))
    fec_pago = forms.DateTimeField(label="Fecha Pago",  initial=timezone.now(), widget = forms.DateTimeInput(attrs={'class':'form-control'}))
    preciod = forms.DecimalField(label="Pago US$", widget = forms.NumberInput(attrs={'class':'form-control'}))
    precios = forms.DecimalField(label="Pago S/", required=False, initial=0, widget = forms.NumberInput(attrs={'class':'form-control'}))
    gastosd = forms.DecimalField(label=" Gastos US$", widget = forms.NumberInput(attrs={'class':'form-control'}))
    gastoss = forms.DecimalField(label=" Gastos S/", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    nrooper = forms.CharField(label="Nro.Operación",  widget = forms.TextInput(attrs={'class':'form-control'}))
    banco = forms.CharField(label="Banco",  widget = forms.TextInput(attrs={'class':'form-control'}))
    efectivo = forms.BooleanField(label="Efectivo",  widget = forms.CheckboxInput(attrs={'class':'form-control'}))
    observ = forms.CharField(label="Observaciones", required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    fecha_creacion = forms.DateTimeField(disabled=True, initial=timezone.now())

    class Meta:
        model = Pagos
        fields = ("venta", "cuota", "fec_vcto", "fec_pago", "preciod",  "precios", "gastosd", "gastoss", "nrooper",
                  "banco", "observ", "efectivo", "fecha_creacion")
