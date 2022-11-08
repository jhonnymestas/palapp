from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Inmobiliaria(models.Model):
    id = models.AutoField(primary_key=True)
    ruc = models.CharField("RUC",max_length=11, unique=True)
    rassoc = models.CharField("Razón Social", max_length=80, default="", unique=True)
    direccion = models.CharField("Dirección", max_length=150, default="AREQUIPA")
    correo = models.EmailField("eMail", default="@")
    telfij = models.CharField("Teléfono Fijo", max_length=15, null=True, default="", blank=True)
    cel1 = models.CharField("Celular 1", max_length=15, default="")
    cel2 = models.CharField("Celular 2", max_length=15, null=True, default="", blank=True)
    fecha_inicon = models.DateTimeField("Fecha Inicio de Contrato", default=timezone.now, null=False)
    activo = models.BooleanField(null=False, default=1)

    fecha_creacion = models.DateTimeField(
        default=timezone.now)
    fecha_act = models.DateTimeField(auto_now=True,
        blank=True, null=True)
    usuar=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario Creación")

    def clean(self):
        if not len(self.ruc) >= 11:
            raise ValidationError(
                {'ruc': "RUC NO VALIDO"})
        if not len(self.cel1) >= 9:
            raise ValidationError(
                {'cel1': "Celular 1 NO VALIDO"})

    def save(self, *args, **kwargs):
        self.rassoc = (self.rassoc).upper()
        self.direccion = (self.direccion).upper()
        return super(Inmobiliaria, self).save(*args, **kwargs)

    def fecact(self):
        self.fecha_act = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.ruc} {self.rassoc} {self.direccion}"


class Notaria(models.Model):
    id = models.AutoField(primary_key=True)
    rassoc = models.CharField("Razón Social", max_length=50, null=True)
    ruc = models.CharField("RUC", max_length=11, default="", null=True)
    direccion = models.TextField("Dirección", default="AREQUIPA")
    correo = models.EmailField("eMail", default="@")
    telfij = models.CharField("Teléfono Fijo", max_length=15, default="", null=True, blank=True)
    cel1 = models.CharField("Celular 1", max_length=15, default="")
    cel2 = models.CharField("Celular 2", max_length=15, default="", null=True, blank=True)
    activo = models.BooleanField(null=False, default=True)
    fecha_creacion = models.DateTimeField(
        default=timezone.now)
    fecact = models.DateTimeField(
        default=timezone.now,
        blank=True, null=True)
    usuario_crea = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario Coordinador", default=1,
                                     null=True)

    def clean(self):
        if not len(self.cel1) >= 9:
            raise ValidationError(
                {'cel1': "Celular 1 NO VALIDO"})

    def save(self, *args, **kwargs):
        self.rassoc = (self.rassoc).upper()
        self.direccion = (self.direccion).upper()
        return super(Notaria, self).save(*args, **kwargs)

    def fact(self):
        self.fecact = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.rassoc} {self.ruc}"


class Jefe(models.Model):
    id = models.AutoField(primary_key=True)
    inmobiliaria = models.ForeignKey(Inmobiliaria, on_delete=models.CASCADE, verbose_name="Inmobiliaria",)
    appat = models.CharField("Apellido Paterno", max_length=50, null=True)
    apmat = models.CharField("Apellido Materno", max_length=50, null=True)
    nomb = models.CharField("Nombre", max_length=50)
    correo = models.EmailField("eMail", default="@")
    telfij = models.CharField("Teléfono Fijo", max_length=15, null=True, default="" , blank=True)
    cel1 = models.CharField("Celular 1", max_length=15, default="")
    cel2 = models.CharField("Celular 2", max_length=15, null=True, default="" , blank=True)
    activo = models.BooleanField(null=False, default=True)
    fecha_creacion = models.DateTimeField(
        default=timezone.now)
    fecact = models.DateTimeField(
        default=timezone.now,
        blank=True, null=True)
    usuario_crea = models.ForeignKey(User, on_delete=models.CASCADE, default=1,)

    def clean(self):
        if not len(self.cel1) >= 9:
            raise ValidationError(
                {'cel1': "Celular 1 NO VALIDO"})

    def save(self, *args, **kwargs):
        self.appat = (self.appat).upper()
        self.apmat = (self.apmat).upper()
        self.nomb = (self.nomb).upper()
        return super(Jefe, self).save(*args, **kwargs)

    def fact(self):
        self.fecact = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.appat} {self.apmat} {self.nomb}"

    class Meta:
        verbose_name = 'encargado'
        verbose_name_plural = 'encargados'


class Vendedor(models.Model):
    id = models.AutoField(primary_key=True)
    jefe = models.ForeignKey(Jefe, on_delete=models.CASCADE, verbose_name="Nombre Coordinador", default=1)
    appat = models.CharField("Apellido Paterno", max_length=50, null=True)
    apmat = models.CharField("Apellido Materno", max_length=50, null=True)
    nomb = models.CharField("Nombre", max_length=50)
    dni = models.CharField("DNI", max_length=8, default="")
    ruc = models.CharField("RUC", max_length=11, default="", null=True, blank=True)
    codagente = models.CharField("Cod.Agente Inmobiliario", max_length=20, default="")
    direccion = models.TextField("Dirección Casa", default="AREQUIPA")
    correo = models.EmailField("eMail", default="@")
    telfij = models.CharField("Teléfono Fijo", max_length=15, default="", blank=True)
    cel1 = models.CharField("Celular 1", max_length=15, default="")
    cel2 = models.CharField("Celular 2", max_length=15, default="", blank=True)
    activo = models.BooleanField(null=False, default=True)
    fecha_ingreso = models.DateTimeField("Fecha de Ingreso",
        default=timezone.now)
    fecha_cese = models.DateTimeField("Fecha de Cese", null=True, blank=True)
    fecha_creacion = models.DateTimeField(
        default=timezone.now, null=False)
    fecact = models.DateTimeField(
        default=timezone.now,
        blank=True, null=True)
    id_usuario_jefe = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario Coordinador", default=1, null=True)

    def clean(self):
        if not len(self.cel1) >= 9:
            raise ValidationError(
                {'cel1': "Celular 1 NO VALIDO"})


    def save(self, *args, **kwargs):
        self.appat = (self.appat).upper()
        self.apmat = (self.apmat).upper()
        self.nomb = (self.nomb).upper()
        self.direccion = (self.direccion).upper()
        return super(Vendedor, self).save(*args, **kwargs)


    def fact(self):
        self.fecact = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.appat} {self.apmat} {self.nomb} {'-'} {self.dni}"

    class Meta:
        ordering = ['appat', 'apmat', 'nomb']


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, verbose_name="Vendedor",)
    appat = models.CharField("Apellido Paterno", max_length=50, null=True)
    apmat = models.CharField("Apellido Materno", max_length=50, null=True)
    nomb = models.CharField("Nombre", max_length=50)
    dni = models.CharField("DNI", max_length=8, default=" ")
    direccion = models.TextField("Dirección Casa", default="AREQUIPA")
    directra = models.TextField("Dirección Trabajo", default="AREQUIPA", blank=True)
    pais = models.CharField("Nacionalidad", max_length=50, default="PERU")
    correo = models.EmailField("eMail", default="@")
    telfij = models.CharField("Teléfono Fijo", max_length=15, default="", blank=True)
    cel1 = models.CharField("Celular 1", max_length=15, default="")
    cel2 = models.CharField("Celular 2", max_length=15, default="", blank=True)
    ocupacion = models.CharField("Ocupación", max_length=100, default="")
    percon = models.TextField("Persona de contacto", default="", blank=True)
    celcon = models.CharField("Numero contacto", max_length=15, default="", blank=True)
    activo = models.BooleanField(null=False, default=True)
    observ = models.TextField("Observaciones", null=True, default="", blank=True)
    fecha_creacion = models.DateTimeField(
        default=timezone.now)
    fecact = models.DateTimeField(
        default=timezone.now,
        blank=True, null=True)
    usuario_crea=models.ForeignKey(User, on_delete=models.CASCADE, default=1,)

    def clean(self):
        if not len(self.cel1) >= 9:
            raise ValidationError(
                {'cel1': "Celular 1 NO VALIDO"})

    def save(self, *args, **kwargs):
        self.appat = (self.appat).upper()
        self.apmat = (self.apmat).upper()
        self.nomb = (self.nomb).upper()
        self.pais = (self.pais).upper()
        self.ocupacion = (self.ocupacion).upper()
        self.direccion = (self.direccion).upper()
        self.directra = (self.directra).upper()
        self.percon = (self.percon).upper()
        self.observ = (self.observ).upper()
        return super(Cliente, self).save(*args, **kwargs)

    def fact(self):
        self.fecact = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.appat} {self.apmat} {self.nomb}"

    class Meta:
        ordering = ['appat', 'apmat', 'nomb']


class Terreno(models.Model):
    ESTD = (
        ('L', 'Libre'),
        ('S', 'Separado'),
        ('V', 'Vendido'),
    )

    id = models.AutoField(primary_key=True)
    codigo = models.CharField("Código", max_length=10, unique=True)
    manzana = models.CharField("Manzana", max_length=2,default="A")
    lote = models.IntegerField("Lote", null=True)
    area = models.DecimalField("Area m2", max_digits=8, decimal_places=2, default=100)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, verbose_name="Vendedor",)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente",)
    preciod = models.DecimalField("P.Venta US$", max_digits=10, decimal_places=2, default=0)
    precios = models.DecimalField("P.Venta S/", max_digits=10, decimal_places=2, default=0)
    comision = models.DecimalField("Comisión %", max_digits=5, decimal_places=2, default=0)
    lfrente = models.TextField("Limite de Frente", default="", null=True)
    mlfrente = models.TextField("Mts Lin. de Frente", default="", null=True)
    lder = models.TextField("Limite Derecho", default="", null=True)
    mlder = models.TextField("Mts Lin. Derecha", default="", null=True)
    lizq = models.TextField("Limite Izquierda", default="", null=True)
    mlizq = models.TextField("Mts Lin. Izquierda", default="", null=True)
    lfondo = models.TextField("Limite Fondo", default="", null=True)
    mlfondo = models.TextField("Mts Lin. Fondo", default="", null=True)
    norte = models.TextField("Norte", default="", null=True)
    sur = models.TextField("Sur", default="", null=True)
    este = models.TextField("Este", default="", null=True)
    oeste = models.TextField("Oeste", default="", null=True)
    observaciones = models.TextField("Observaciones", blank=True)
    estado = models.CharField("Estado", choices=ESTD, max_length=1, default='L')
    fecha_creacion = models.DateTimeField(
        default=timezone.now)
    fecact = models.DateTimeField(
        blank=True, null=True)
    usuario_crea = models.ForeignKey(User, on_delete=models.CASCADE, default=1, )

    def fact(self):
        self.fecact = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        self.codigo = (self.codigo).upper()
        self.manzana = (self.manzana).upper()
        self.lfrente = (self.lfrente).upper()
        self.lder = (self.lder).upper()
        self.lizq = (self.lizq).upper()
        self.lfondo = (self.lfondo).upper()
        self.norte = (self.norte).upper()
        self.sur = (self.sur).upper()
        self.este = (self.este).upper()
        self.oeste = (self.oeste).upper()
        self.observaciones = (self.observaciones).upper()
        return super(Terreno, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.manzana} {'-'} {self.lote} {'/'} {self.codigo}"

    class Meta:
        verbose_name = 'terreno'
        verbose_name_plural = 'terrenos'
        ordering = ['manzana', 'lote']

class Tramites(models.Model):
    POR_HACER = (
        ('L', 'Llamar'),
        ('R', 'Reunirse'),
        ('C', 'Correo'),
        ('W', 'Whatsapp'),
        ('M', 'Messenger'),
    )
    LUGAR = (
        ('C', 'Casa'),
        ('O', 'Oficina'),
        ('V', 'Otro lugar'),
    )
    INTERES =(
        ('B', 'Bajo'),
        ('R', 'Regular'),
        ('I', 'Interesado'),
        ('M', 'Muy Interesado'),
        ('T', 'Totalmente Convencido'),
    )

    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente", default=0)
    terreno = models.ForeignKey(Terreno, on_delete=models.CASCADE, verbose_name="Terreno", default=0)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, verbose_name="Vendedor", default=0)
    descrip = models.TextField("Detalle")
    por_hacer = models.CharField("Via", choices=POR_HACER, max_length=1)
    resultado = models.TextField("Resultado Gestión")
    fec_prox = models.DateTimeField("Fecha proximo trámite", default=timezone.now)
    lugar = models.CharField("Donde", choices=LUGAR, max_length=1)
    nivel = models.CharField("Nivel de Interes", choices=INTERES, max_length=1)
    observ = models.TextField("Observaciones", blank=True)
    fecha_creacion = models.DateTimeField(
        default=timezone.now)
    fecact = models.DateTimeField(
        blank=True, null=True)
    usuario_crea = models.ForeignKey(User, on_delete=models.CASCADE, default=1,)

    def fact(self):
        self.fecact = timezone.now()
        self.save()

    def clean(self):
        if not (self.fec_prox) >= timezone.now():
            raise ValidationError(
                {'fec_prox': "Fecha de Proxima actividad debe ser mayor a HOY!"})

    def save(self, *args, **kwargs):
        self.por_hacer = (self.por_hacer).upper()
        self.descrip = (self.descrip).upper()
        self.resultado = (self.resultado).upper()
        self.lugar = (self.lugar).upper()
        self.observ = (self.observ).upper()
        return super(Tramites, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'tramite'
        verbose_name_plural = 'tramites'


class Venta(models.Model):
    CONDICION = (
        ('C', 'Contado'),
        ('B', 'Financ.Banco'),
        ('P', 'FInanc.Propio Efectivo'),
        ('L', 'FInanc.Propio Letras'),
    )

    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente", default=0)
    terreno = models.ForeignKey(Terreno, on_delete=models.CASCADE, verbose_name="Terreno", default=0, unique=True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, verbose_name="Vendedor", default=0)
    notaria = models.ForeignKey(Notaria, on_delete=models.CASCADE, verbose_name="Notaria", default=0)
    banco = models.TextField("Banco", max_length=40, null=True, default="", blank=True)
    condvta = models.CharField("Condición Venta", choices=CONDICION, max_length=1, default='C')
    nro_cont = models.TextField("Número de Contrato", null=False, unique=True)
    fec_con = models.DateTimeField("Fecha Contrato", default=timezone.now, null=False)
    preciod = models.DecimalField("P.Venta US$", max_digits=10, decimal_places=2, default=0)
    precios = models.DecimalField("P.Venta S/", max_digits=10, decimal_places=2, default=0)
    comision = models.DecimalField("Comisión %", max_digits=5, decimal_places=2, default=0)
    observ = models.TextField("Observaciones", blank=True)
    fecha_creacion = models.DateTimeField(
        default=timezone.now)
    fecact = models.DateTimeField(
        blank=True, null=True)
    usuario_crea = models.ForeignKey(User, on_delete=models.CASCADE, default=1, )
    aprobado = models.BooleanField("Aprobado", default=False)
    plan_generado = models.BooleanField("Plan de Pago Generado", default=False)
    foto_contrato = models.ImageField("Foto Voucher", blank=True)

    def fact(self):
        self.fecact = timezone.now()
        self.save()

    def clean(self):
        if not (self.precios+self.preciod > 0):
            raise ValidationError(
                {'preciod': "Debe llenar precio de Venta en Soles o Dólares"})

    def save(self, *args, **kwargs):
        self.condvta = (self.condvta).upper()
        self.nro_cont = (self.nro_cont).upper()
        self.banco = (self.banco).upper()
        self.observ = (self.observ).upper()
        return super(Venta, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nro_cont} {'/'} {self.cliente} {'/'} {self.terreno}"

    class Meta:
        verbose_name = 'venta'
        verbose_name_plural = 'ventas'


class Pagos(models.Model):
    ESTADO = (
        ('P', 'Pendiente'),
        ('C', 'Cancelado'),
    )

    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Contrato", default=0)
    cuota = models.IntegerField("Cuota No.", default=1)
    fec_vcto = models.DateTimeField("Fecha Vencimiento", default=timezone.now, null=False)
    fec_pago = models.DateTimeField("Fecha Pago", null=False, blank=True)
    preciod = models.DecimalField("Pago US$", max_digits=10, decimal_places=2, default=0)
    precios = models.DecimalField("Pago S/", max_digits=10, decimal_places=2, default=0)
    gastosd = models.DecimalField("Gastos US$", max_digits=5, decimal_places=2, default=0)
    gastoss = models.DecimalField("Gastos S/", max_digits=5, decimal_places=2, default=0)
    nrooper = models.CharField("Numero Operación", max_length=30)
    banco = models.CharField("Banco", max_length=40, blank=True)
    observ = models.TextField("Observaciones", blank=True)
    efectivo = models.BooleanField("Efectivo?", default=True)
    estado = models.CharField("Estado", choices=ESTADO, max_length=1, default="P")
    foto_vouc = models.ImageField("Foto Voucher", blank=True)
    fecha_creacion = models.DateTimeField(
        default=timezone.now)
    fecact = models.DateTimeField(
        blank=True, null=True)
    usuario_crea = models.ForeignKey(User, on_delete=models.CASCADE, default=1, )

    def fact(self):
        self.fecact = timezone.now()
        self.save()

    def clean(self):
        if not (self.precios+self.preciod > 0):
            raise ValidationError(
                {'preciod': "Debe llenar Importe a Pagar de Cuota Soles o Dólares"})

    def save(self, *args, **kwargs):
        self.estado = (self.estado).upper()
        self.observ = (self.observ).upper()
        return super(Pagos, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'pago'
        verbose_name_plural = 'pagos'


class Question(models.Model):
      question_text = models.CharField(max_length=200)
      pub_date = models.DateTimeField('date published')

class Choice(models.Model):
      question = models.ForeignKey(Question, on_delete=models.CASCADE)
      choice_text = models.CharField(max_length=200)
      votes = models.IntegerField(default=0)


