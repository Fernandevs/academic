from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from egress.forms import EgressForm
from egress.models import Egress


# Create your views here.

class EgressListView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ListView
):
    model = Egress
    login_url = reverse_lazy('login')
    template_name = 'egress/read.html'
    success_url = reverse_lazy('list_users')
    permission_required = 'egress.view_egress'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de usuarios'

        return context


class EgressCreateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    CreateView
):
    model = Egress
    form_class = EgressForm
    login_url = reverse_lazy('login')
    template_name = 'egress/create.html'
    success_url = reverse_lazy('list_users')
    permission_required = 'egress.add_egress'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear usuarios'

        return context


class EgressUpdateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UpdateView
):
    model = Egress
    form_class = EgressForm
    login_url = reverse_lazy('login')
    template_name_suffix = '_update_form'
    template_name = 'egress/update.html'
    success_url = reverse_lazy('list_users')
    permission_required = 'egress.change_egress'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar usuarios'

        return context


class EgressDeleteView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DeleteView
):
    model = Egress
    login_url = reverse_lazy('login')
    template_name = 'egress/delete.html'
    success_url = reverse_lazy('list_users')
    permission_required = 'egress.delete_egress'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar usuarios'

        return context
