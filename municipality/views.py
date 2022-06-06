import csv

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from municipality.forms import MunicipalityForm
from municipality.models import Municipality

from state.models import State

# Create your views here.


class MunicipalityListView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ListView
):
    model = Municipality
    login_url = reverse_lazy('login')
    template_name = 'municipalities/read.html'
    paginate_by = 20
    permission_required = 'municipality.vie_municipalityw'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de municipios'

        return context


class MunicipalityCreateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    CreateView
):
    model = Municipality
    form_class = MunicipalityForm
    login_url = reverse_lazy('login')
    template_name = 'municipalities/create.html'
    success_url = reverse_lazy('list_municipality')
    permission_required = 'municipality.add_municipality'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear municipio'

        return context


class MunicipalityUpdateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UpdateView
):
    model = Municipality
    form_class = MunicipalityForm
    login_url = reverse_lazy('login')
    template_name_suffix = '_update_form'
    template_name = 'municipalities/update.html'
    success_url = reverse_lazy('list_municipality')
    permission_required = 'municipality.cha_municipalitynge'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar municipio'

        return context


class MunicipalityDeleteView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DeleteView
):
    model = Municipality
    login_url = reverse_lazy('login')
    template_name = 'municipalities/delete.html'
    success_url = reverse_lazy('list_municipality')
    permission_required = 'municipality.del_municipalityete'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar municipio'

        return context


class MunicipalityMassiveTemplateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    TemplateView
):
    login_url = reverse_lazy('login')
    template_name = 'states/massive.html'
    permission_required = 'municipality.add_municipality'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inserción masiva de municipios'

        return context

    def post(self, request, *args, **kwargs):
        file_name = request.FILES['file_name']
        decoded_file = file_name.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        for row in reader:
            print(row)

            try:
                state: str = row['Cve_Ent']
                municipality_id: str = row['Cve_Mun']
                municipality_name: str = row['Nom_Mun']
            except KeyError as e:
                print(e.__str__())
                break

            municipality_id.zfill(3)
            state.zfill(2)

            try:
                state = State.objects.all().filter(pk=state).get()
            except Exception as e:
                print(e.__str__())
                continue

            municipality = Municipality(
                municipality_id=municipality_id,
                municipality_name=municipality_name,
                state=state
            )

            try:
                municipality.save()
            except Exception as e:
                print(e.__str__())
                continue

        return redirect('list_municipality')
