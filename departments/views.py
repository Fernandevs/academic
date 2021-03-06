from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from departments.forms import DepartmentForm
from departments.models import Department


# Create your views here.

class DepartmentListView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ListView
):
    model = Department
    login_url = reverse_lazy('login')
    template_name = 'departments/read.html'
    permission_required = 'departments.view_department'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de departamentos'

        return context


class DepartmentCreateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    CreateView
):
    model = Department
    form_class = DepartmentForm
    login_url = reverse_lazy('login')
    template_name = 'departments/create.html'
    success_url = reverse_lazy('list_department')
    permission_required = 'departments.add_department'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear departamento'

        return context


class DepartmentUpdateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UpdateView
):
    model = Department
    form_class = DepartmentForm
    login_url = reverse_lazy('login')
    template_name_suffix = '_update_form'
    template_name = 'departments/update.html'
    success_url = reverse_lazy('list_department')
    permission_required = 'departments.change_department'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar departamento'

        return context


class DepartmentDeleteView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DeleteView
):
    model = Department
    login_url = reverse_lazy('login')
    template_name = 'departments/delete.html'
    success_url = reverse_lazy('list_department')
    permission_required = 'departments.delete_department'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar departamentos'

        return context
