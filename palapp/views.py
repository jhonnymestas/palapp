from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from django.utils import timezone

from .models import Pagos


from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib import messages

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . models import Inmobiliaria, Question, Choice, Jefe, Vendedor, Cliente, Terreno, Tramites
from . models import Notaria, Pagos, Venta
from .forms import InmobiliariaForm, JefeForm, VendedorForm, ClienteForm, TerrenoForm, TramitesForm, NotariaForm
from .forms import VentaForm, PagosForm

def is_in_multiple_groups(user):
    return user.groups.filter(name__in=['administrador', 'responsable']).exists()


# Seccion Listar
# #########################################

class Inmoblistar(ListView):
    model = Inmobiliaria
    paginate_by = 8
    ordering = ['rassoc']

    def get_queryset(self):

        if self.request.GET.get('buscar') is not None:
            q=self.request.GET.get('buscar')

            return Inmobiliaria.objects.filter(Q(ruc__icontains=q) | Q(direccion__icontains=q) |
                                               Q(rassoc__icontains=q) | Q(correo__icontains=q) |
                                               Q(cel1__icontains=q))

        return super().get_queryset()


class Jefelistar(ListView):
    model = Jefe
    paginate_by = 8
    ordering = ['appat', 'apmat', 'nomb']


class Vendedorlistar(ListView):
    model = Vendedor
    paginate_by = 8
    ordering = ['appat', 'apmat', 'nomb']


class Clientelistar(ListView):
    model = Cliente
    paginate_by = 8
    ordering = ['appat', 'apmat', 'nomb']

    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            q=self.request.GET.get('buscar')

            return Cliente.objects.filter(Q(dni__icontains=q) | Q(direccion__icontains=q) |
                                          Q(directra__icontains=q) | Q(correo__icontains=q) |
                                          Q(cel1__icontains=q) | Q(appat__icontains=q) |
                                          Q(apmat__icontains=q) | Q(nomb__icontains=q) |
                                          Q(percon__icontains=q) | Q(celcon__icontains=q) |
                                          Q(ocupacion__icontains=q))

        return super().get_queryset()


class Terrenolistar(ListView):
    model = Terreno
    paginate_by = 8
    ordering = ['estado', 'manzana', 'lote']

    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            q=self.request.GET.get('buscar')

            return Terreno.objects.filter(Q(codigo__icontains=q) | Q(manzana__icontains=q) |
                                          Q(preciod__icontains=q) | Q(area__icontains=q) |
                                          Q(lfrente__icontains=q) | Q(lder__icontains=q) |
                                          Q(lizq__icontains=q) | Q(lfondo__icontains=q) |
                                          Q(norte__icontains=q) | Q(sur__icontains=q) |
                                          Q(este__icontains=q) | Q(oeste__icontains=q) |
                                          Q(observaciones__icontains=q))
        return super().get_queryset()


class Tramiteslistar(ListView):
    model = Tramites
    paginate_by = 8
    ordering = ['-fecha_creacion']

    def get_queryset(self):
        if is_in_multiple_groups(self.request.user):

            if self.request.GET.get('buscar') is not None:
                q = self.request.GET.get('buscar')

                return Tramites.objects.filter(Q(descrip__icontains=q) | Q(lugar__icontains=q) |
                                              Q(resultado__icontains=q) | Q(por_hacer__icontains=q) |
                                              Q(nivel__icontains=q) | Q(observ__icontains=q) |
                                              Q(fec_prox__icontains=q))
        else:
            if self.request.GET.get('buscar') is not None:
                q = self.request.GET.get('buscar')

                return Tramites.objects.filter((Q(descrip__icontains=q) | Q(lugar__icontains=q) |
                                               Q(resultado__icontains=q) | Q(por_hacer__icontains=q) |
                                               Q(nivel__icontains=q) | Q(observ__icontains=q) |
                                               Q(fec_prox__icontains=q)) & Q(usuario_crea=self.request.user))
            else:
                return Tramites.objects.filter(Q(usuario_crea=self.request.user))

        return super().get_queryset()


class Notarialistar(ListView):
    model = Notaria
    paginate_by = 8
    ordering = ['rassoc']


class Ventalistar(ListView):
    model = Venta
    paginate_by = 8
    ordering = ['-nro_cont']

    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            q = self.request.GET.get('buscar')

            return Tramites.objects.filter(Q(nro_cont__icontains=q) | Q(cliente__icontains=q) |
                                           Q(fecha_con__icontains=q) | Q(terreno__icontains=q) |
                                           Q(vendedor__icontains=q) | Q(observ__icontains=q) |
                                           Q(banco__icontains=q) | Q(notaria__icontains=q) |
                                           Q(fec_con__icontains=q))
        return super().get_queryset()


class Pagoslistar(ListView):
    model = Pagos
    paginate_by = 8
    ordering = ['-nro_cont']

    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            q = self.request.GET.get('buscar')

            return Tramites.objects.filter(Q(nro_cont__icontains=q) | Q(cliente__icontains=q) |
                                           Q(fecha_con__icontains=q) | Q(terreno__icontains=q) |
                                           Q(vendedor__icontains=q) | Q(observ__icontains=q) |
                                           Q(banco__icontains=q) | Q(notaria__icontains=q) |
                                           Q(fec_con__icontains=q))
        return super().get_queryset()


# Para obtener todos los campos de un registro de la tablas

class InmobiliariaDetalle(DetailView):
    model = Inmobiliaria


class JefeDetalle(DetailView):
    model = Jefe


class VendedorDetalle(DetailView):
    model = Vendedor


class ClienteDetalle(DetailView):
    model = Cliente


class TerrenoDetalle(DetailView):
    model = Terreno


class TramitesDetalle(DetailView):
    model = Tramites


class NotarioDetalle(DetailView):
    model = Notaria


class VentaDetalle(DetailView):
    model = Venta


class PagosDetalle(DetailView):
    model = Pagos


# Para insertar un nuevo contacto en la tabla Inmobiliaria
class InmobiliariaNuevo(SuccessMessageMixin, CreateView):
    model = Inmobiliaria
    form = Inmobiliaria
    fields = "__all__"
    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Inmobiliaria añadida correctamente.'


    # Redirigimos a la página principal tras insertar el registro
    def get_success_url(self):
        return reverse_lazy('palapp:inmlist')


def add_inmobiliaria(request):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = InmobiliariaForm(request.POST) # Bound form

        if form.is_valid():
            
            new_inmobiliaria = form.save(commit=False) # Guardar los datos en la base de datos
            if form.is_valid():
                if request.user.is_authenticated:
                    new_inmobiliaria.usuar = request.user
                else:
                    new_inmobiliaria.usuar = AnonymousUser.get_username()
            new_inmobiliaria.save()
            return HttpResponseRedirect(reverse('palapp:inmlist'))
    else:
        form = InmobiliariaForm() # Unbound form

    return render(request, 'palapp/addinm.html', {'form': form})


def add_jefe(request):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form2 = JefeForm(request.POST) # Bound form
        if form2.is_valid():
            new_jefe = form2.save(commit=False) # Guardar los datos en la base de datos
            if form2.is_valid():
                if request.user.is_authenticated:
                    new_jefe.usuario_crea = request.user
                else:
                    new_jefe.usuario_crea = AnonymousUser.get_username()
            new_jefe.save()
            return HttpResponseRedirect(reverse('palapp:jeflist'))
    else:
        form2 = JefeForm() # Unbound form

    return render(request, 'palapp/addjef.html', {'form': form2})


def add_vendedor(request):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form2 = VendedorForm(request.POST) # Bound form
        if form2.is_valid():
            new_vendedor = form2.save() # Guardar los datos en la base de datos

            return HttpResponseRedirect(reverse('palapp:venlist'))
    else:
        form2 = VendedorForm() # Unbound form

    return render(request, 'palapp/addven.html', {'form': form2})


def add_cliente(request):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form2 = ClienteForm(request.POST) # Bound form
        if form2.is_valid():
            new_cliente = form2.save(commit=False)  # Guardar los datos en la base de datos
            if form2.is_valid():
                if request.user.is_authenticated:
                    new_cliente.usuario_crea = request.user
                else:
                    new_cliente.usuario_crea = AnonymousUser.get_username()
            new_cliente.save()
            return HttpResponseRedirect(reverse('palapp:clilist'))
    else:
        form2 = ClienteForm() # Unbound form

    return render(request, 'palapp/addcli.html', {'form': form2})


def add_terreno(request):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form2 = TerrenoForm(request.POST) # Bound form
        if form2.is_valid():
            new_terreno = form2.save(commit=False) # Guardar los datos en la base de datos
            if form2.is_valid():
                if request.user.is_authenticated:
                    new_terreno.usuario_crea = request.user
                else:
                    new_terreno.usuario_crea = AnonymousUser.get_username()
            new_terreno.save()
            return HttpResponseRedirect(reverse('palapp:terlist'))
    else:
        form2 = TerrenoForm() # Unbound form

    return render(request, 'palapp/addter.html', {'form': form2})


def add_tramites(request):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form2 = TramitesForm(request.POST) # Bound form
        if form2.is_valid():
            new_tramites = form2.save(commit=False) # Guardar los datos en la base de datos
            if form2.is_valid():
                if request.user.is_authenticated:
                    new_tramites.usuario_crea = request.user
                else:
                    new_tramites.usuario_crea = AnonymousUser.get_username()
            new_tramites.save()
            return HttpResponseRedirect(reverse('palapp:tralist'))
    else:
        form2 = TramitesForm() # Unbound form

    return render(request, 'palapp/addtra.html', {'form': form2})


def add_notaria(request):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form2 = NotariaForm(request.POST) # Bound form
        if form2.is_valid():
            new_notaria = form2.save(commit=False) # Guardar los datos en la base de datos
            if form2.is_valid():
                if request.user.is_authenticated:
                    new_notaria.usuario_crea = request.user
                else:
                    new_notaria.usuario_crea = AnonymousUser.get_username()
            new_notaria.save()
            return HttpResponseRedirect(reverse('palapp:lisnot'))
    else:
        form2 = NotariaForm() # Unbound form

    return render(request, 'palapp/addnot.html', {'form': form2})

def add_venta(request):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form2 = VentaForm(request.POST) # Bound form
        if form2.is_valid():
            new_venta = form2.save(commit=False) # Guardar los datos en la base de datos
            if form2.is_valid():
                if request.user.is_authenticated:
                    new_venta.usuario_crea = request.user
                else:
                    new_venta.usuario_crea = AnonymousUser.get_username()
            new_venta.save()
            return HttpResponseRedirect(reverse('palapp:lisvta'))
    else:
        form2 = VentaForm() # Unbound form

    return render(request, 'palapp/addvta.html', {'form': form2})


def add_pagos(request):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form2 = PagosForm(request.POST) # Bound form
        if form2.is_valid():
            new_pagos = form2.save(commit=False) # Guardar los datos en la base de datos
            if form2.is_valid():
                if request.user.is_authenticated:
                    new_pagos.usuario_crea = request.user
                else:
                    new_pagos.usuario_crea = AnonymousUser.get_username()
            new_pagos.save()
            return HttpResponseRedirect(reverse('palapp:lispag'))
    else:
        form2 = PagosForm() # Unbound form

    return render(request, 'palapp/addpag.html', {'form': form2})


# Actualizaciones


class UpdtInmobiliaria(SuccessMessageMixin, UpdateView):
    model = Inmobiliaria
    form = InmobiliariaForm
    fields = ("ruc", "rassoc", "direccion", "correo", "telfij", "cel1", "cel2", "fecha_inicon")

    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Inmobiliaria actualizada correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse_lazy('palapp:inmlist')


class UpdtJefe(SuccessMessageMixin, UpdateView):
    model = Jefe
    form = JefeForm
    fields = ("inmobiliaria", "appat", "apmat", "nomb", "correo", "telfij", "cel1", "cel2")
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Encargado actualizado correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse_lazy('palapp:jeflist')


class UpdtVendedor(SuccessMessageMixin, UpdateView):
    model = Vendedor
    form = VendedorForm
    fields = ("jefe", "id_usuario_jefe", "dni", "appat", "apmat", "nomb", "direccion", "codagente", "correo", "telfij",
              "cel1", "cel2", "fecha_ingreso", "fecha_cese")
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Vendedor actualizado correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse_lazy('palapp:venlist')


class UpdtCliente(SuccessMessageMixin, UpdateView):
    model = Cliente
    form = ClienteForm
    fields = ("vendedor", "dni", "appat", "apmat", "nomb", "direccion", "directra", "pais",
                  "correo", "telfij", "cel1", "cel2", "ocupacion", "percon", "celcon", "observ")

    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Cliente actualizado correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse_lazy('palapp:clilist')


class UpdtTerreno(SuccessMessageMixin, UpdateView):
    model = Terreno
    form = TerrenoForm
    fields = ("vendedor", "cliente", "codigo", "manzana", "lote", "area", "preciod", "precios", "comision", "lfrente",
                  "mlfrente", "lder", "mlder", "lizq", "mlizq", "lfondo", "mlfondo", "norte", "sur", "este", "oeste",
                  "observaciones", "estado")

    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Terreno actualizado correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse_lazy('palapp:terlist')


class UpdtTramite(SuccessMessageMixin, UpdateView):
    model = Tramites
    form = TramitesForm
    fields = ("cliente", "terreno", "vendedor", "descrip", "resultado", "nivel", "por_hacer", "fec_prox", "lugar",
              "observ")

    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Gestión actualizado correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse_lazy('palapp:tralist')


class UpdtNotaria(SuccessMessageMixin, UpdateView):
    model = Notaria
    form = NotariaForm
    fields = ("ruc", "rassoc",  "direccion", "correo", "telfij", "cel1", "cel2")

    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Notaría actualizado correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse_lazy('palapp:lisnot')


class UpdtVenta(SuccessMessageMixin, UpdateView):
    model = Venta
    form = VentaForm
    fields = ("cliente", "terreno", "vendedor", "notaria", "banco", "condvta", "nro_cont", "fec_con", "preciod", "precios",
              "comision", "observ", "inicial", "fecha_inicial", "fecha_1ervct", "cuotas", "aprobado", "fecha_creacion",
              "foto_contrato")

    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Cierre de Venta actualizado correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse_lazy('palapp:lisvta')


class UpdtPagos(SuccessMessageMixin, UpdateView):
    model = Pagos
    form = PagosForm
    fields = ("venta", "cuota", "fec_vcto", "fec_pago", "preciod", "precios", "gastosd", "gastoss", "nrooper",
              "banco", "observ", "efectivo", "fecha_creacion")

    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Pagos actualizados correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse_lazy('palapp:lispag')


def upd_jefe(request, id_jefe):
    jefe = Jefe.objects.get(id=id_jefe)
    if request.method == 'GET':
        form2 = JefeForm(instance=jefe)
    else:
        form2 = JefeForm(request.POST, instance=jefe)
        if form2.is_valid():
           form2.save() # Guardar los datos en la base de datos
           return HttpResponseRedirect(reverse('palapp:jeflist'))
        else:
           form2 = JefeForm() # Unbound form
    return render(request, 'palapp/edtjef.html', {'form': form2})


class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class IndexView(generic.ListView):
    template_name = 'palapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte = timezone.now()
                                       ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'palapp/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'palapp/results.html'


# Vista de la plantilla que muestra el perfil del usuario autenticado.

@login_required(login_url='login')
def Profile(request):
    user = request.user
    return render(request, 'palapp/profile.html', {'user':user})


# Vista de la plantilla que se muestra el formulario para cambiar la contraseña del usuario logeado.

@login_required(login_url='login')
def Change_Password(request):
    user = request.user
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            success_message = 'Contraseña cambiada Correctamente.'
            return HttpResponseRedirect('./')
        else:
            success_message = 'ERROR EN LAS CONTRASEÑAS PROPORCIONADAS.'
            return HttpResponseRedirect('change_password')
    return render(request, 'palapp/change_password.html', {'form': form})


# Define class for inserting multiple data
def gen_cron(request, pk):
    ventas = Venta.objects.get(id=pk)
    if request.method == 'GET':
        form2 = VentaForm(instance=ventas)
        print("paso 3")
    else:
        form2 = VentaForm(request.POST, instance=ventas)
        if form2.is_valid():
            print ("Paso ok")
         #  form2.save() # Guardar los datos en la base de datos
            return HttpResponseRedirect(reverse('palapp:lisvta'))
        else:
           form2 = VentaForm() # Unbound form
    print("paso 2")
    model = Pagos
    monto = ventas.preciod - ventas.inicial
    icuo = monto / ventas.cuotas
    saldo = monto
    for indice in cuotas:
        Pagos.objects.bulk_create([
            Pagos(venta=ventas.id,
                  cuota=indice,
                  fec_vcto=ventas.fecha_1ervct,
                  fec_pago=0,
                  preciod=icuo,
                  precios=0,
                  gastosd=0,
                  gastoss=0,
                  nrooper='',
                  banco='',
                  observ='',
                  efectivo=False,
                  estado='P',
                  fecha_creacion=timezone.now,
                  fecact=timezone.now(),
                  usuario_crea=request.user)])
        saldo = saldo - icuo
    return render(request, 'palapp/cplan.html', {'form': form2})



def ventasbulk(request, pk):
    model = Venta
    venta = Venta.objects.get(id=pk)
    form2 = VentaForm(request.POST, instance=venta)
    if form2.is_valid():
        if request.GET.get('inicial') is not None and request.GET.get('cuotas') is not None:
           inicial = request.GET.get('cini')
           cuotas = request.GET.get('cuotas')
           fvc = request.GET.get('fvc')

        # Insert 5 records in the books table at a time

           model = Pagos
           monto = venta.preciod-inicial
           icuo=monto/cuotas
           saldo=monto
           for indice in cuotas:
               Pagos.objects.bulk_create([
                        Pagos(venta=venta.id,
                            cuota=indice,
                            fec_vcto=fvc,
                            fec_pago=0,
                            preciod=icuo,
                            precios=0,
                            gastosd=0,
                            gastoss=0,
                            nrooper='',
                            banco='',
                            observ='',
                            efectivo=False,
                            estado='P',
                            fecha_creacion=timezone.now,
                            fecact=timezone.now(),
                            usuario_crea =request.user)])
               saldo=saldo-icuo
    else:
        form2 = VentaForm()  # Unbound form
    return HttpResponseRedirect(reverse('palapp:lisvta'))

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'palapp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('palapp:results', args=(question.id,)))



#def cliente_det(request, id):
#    try:
#        cliente=Cliente.objects.get(id=id)
#    except Cliente.doesNotExist:
#        raise Http404('Cliente NO EXISTE')
#    return render(request, 'palapp/cliente_det.html', {
#        'cliente': cliente,
#    })

