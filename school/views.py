from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from school.forms import SchoolForm
from school.models import School


# Create your views here.

class SchoolListView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ListView
):
    model = School
    login_url = reverse_lazy('login')
    template_name = 'schools/read.html'
    permission_required = 'school.view_school'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de escuelas'

        return context


class SchoolCreateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    CreateView
):
    model = School
    form_class = SchoolForm
    login_url = reverse_lazy('login')
    template_name = 'schools/create.html'
    success_url = reverse_lazy('list_school')
    permission_required = 'school.add_school'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear escuelas'

        return context


class SchoolUpdateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UpdateView
):
    model = School
    form_class = SchoolForm
    login_url = reverse_lazy('login')
    template_name_suffix = '_update_form'
    template_name = 'schools/update.html'
    success_url = reverse_lazy('list_school')
    permission_required = 'school.change_school'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar escuelas'

        return context


class SchoolDeleteView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DeleteView
):
    model = School
    login_url = reverse_lazy('login')
    template_name = 'schools/delete.html'
    success_url = reverse_lazy('list_school')
    permission_required = 'school.delete_school'
    permission_denied_message = 'No cuenta con los permisos para realizar esta acción'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar escuelas'

        return context
