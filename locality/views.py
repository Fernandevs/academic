import csv

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from locality.forms import LocalityForm
from locality.models import Locality

from municipality.models import Municipality
from state.models import State

# Create your views here.


class LocalityListView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ListView
):
    model = Locality
    login_url = reverse_lazy('login')
    template_name = 'localities/read.html'
    paginate_by = 20
    permission_required = 'locality.view_locality'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de localidades'

        return context


class LocalityCreateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    CreateView
):
    model = Locality
    form_class = LocalityForm
    login_url = reverse_lazy('login')
    template_name = 'localities/create.html'
    success_url = reverse_lazy('list_locality')
    permission_required = 'locality.add_locality'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear localidad'

        return context


class LocalityUpdateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UpdateView
):
    model = Locality
    form_class = LocalityForm
    login_url = reverse_lazy('login')
    template_name_suffix = '_update_form'
    template_name = 'localities/update.html'
    success_url = reverse_lazy('list_locality')
    permission_required = 'locality.change_locality'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar localidad'

        return context


class LocalityDeleteView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DeleteView
):
    model = Locality
    login_url = reverse_lazy('login')
    template_name = 'localities/delete.html'
    success_url = reverse_lazy('list_locality')
    permission_required = 'locality.delete_locality'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar localidad'

        return context


class LocalityMassiveTemplateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    TemplateView
):
    login_url = reverse_lazy('login')
    template_name = 'localities/massive.html'
    permission_required = 'locality.add_locality'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inserción masiva de localidades'

        return context

    def post(self, request, *args, **kwargs):
        file_name = request.FILES['file_name']
        decoded_file = file_name.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        for row in reader:
            try:
                state: str = row['Cve_Ent']
                municipality: str = row['Cve_Mun']
                locality_id: str = row['Cve_Loc']
                locality_name: str = row['Nom_Loc']
            except KeyError as e:
                print(e.__str__())
                break

            state.zfill(2)
            municipality.zfill(3)
            locality_id.zfill(4)

            try:
                municipality = Municipality.objects.all().filter(pk=municipality).get()
                state = State.objects.all().filter(pk=state).get()
            except Exception as e:
                print(e.__str__())
                continue

            locality = Locality(
                state=state,
                municipality=municipality,
                locality_id=locality_id,
                locality_name=locality_name
            )

            try:
                print(locality)
                locality.save()
            except Exception as e:
                print(e.__str__())
                continue

        return redirect('list_municipality')
