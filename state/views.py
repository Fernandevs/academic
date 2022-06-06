import csv

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from state.forms import StateForm
from state.models import State

# Create your views here.


class StateListView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ListView
):
    model = State
    login_url = reverse_lazy('login')
    template_name = 'states/read.html'
    permission_required = 'state.view_state'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de estados'

        return context


class StateCreateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    CreateView
):
    model = State
    form_class = StateForm
    login_url = reverse_lazy('login')
    template_name = 'states/create.html'
    success_url = reverse_lazy('list_state')
    permission_required = 'state.add_state'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear localidad'

        return context


class StateUpdateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UpdateView
):
    model = State
    form_class = StateForm
    login_url = reverse_lazy('login')
    template_name_suffix = '_update_form'
    template_name = 'states/update.html'
    success_url = reverse_lazy('list_state')
    permission_required = 'state.change_state'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar localidad'

        return context


class StateDeleteView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DeleteView
):
    model = State
    login_url = reverse_lazy('login')
    template_name = 'states/delete.html'
    success_url = reverse_lazy('list_state')
    permission_required = 'state.delete_state'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar localidad'

        return context


class StateMassiveTemplateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    TemplateView
):
    login_url = reverse_lazy('login')
    template_name = 'states/massive.html'
    permission_required = 'state.add_state'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inserción masiva de estados'

        return context

    def post(self, request, *args, **kwargs):
        try:
            file_name = request.FILES['file_name']
        except Exception as e:
            print(e.__str__())

        decoded_file = file_name.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        for row in reader:
            clave: str = row['Cve_Ent']
            nombre: str = row['Nom_Ent']
            clave.zfill(2)

            state = State(
                state_id=clave,
                state_name=nombre
            )

            try:
                state.save()
            except Exception as e:
                print(e.__str__())
                continue

        return redirect('list_state')
