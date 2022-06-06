from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from careers.forms import CareerCreateForm, CareerUpdateForm
from careers.models import Career

# Create your views here.


class CareerListView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ListView
):
    model = Career
    template_name = 'careers/read.html'
    permission_required = 'careers.view_career'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de carreras'

        return context


class CareerCreateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    CreateView
):
    model = Career
    form_class = CareerCreateForm
    template_name = 'careers/create.html'
    success_url = reverse_lazy('list_careers')
    permission_required = 'careers.add_career'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear carreras'

        return context


class CareerUpdateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UpdateView
):
    model = Career
    form_class = CareerUpdateForm
    template_name_suffix = '_update_form'
    template_name = 'careers/update.html'
    success_url = reverse_lazy('list_careers')
    permission_required = 'careers.change_career'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar carreras'

        return context


class CareerDeleteView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DeleteView
):
    model = Career
    template_name = 'careers/delete.html'
    success_url = reverse_lazy('list_careers')
    permission_required = 'careers.delete_career'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar carreras'

        return context
