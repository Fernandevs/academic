from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from school.forms import SchoolForm
from school.models import School


# Create your views here.

class SchoolListView(LoginRequiredMixin, ListView):
    model = School
    login_url = reverse_lazy('login')
    template_name = 'schools/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de escuelas'

        return context


class SchoolCreateView(LoginRequiredMixin, CreateView):
    model = School
    form_class = SchoolForm
    login_url = reverse_lazy('login')
    template_name = 'schools/create.html'
    success_url = reverse_lazy('list_students')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear escuelas'

        return context


class SchoolUpdateView(LoginRequiredMixin, UpdateView):
    model = School
    form_class = SchoolForm
    login_url = reverse_lazy('login')
    template_name_suffix = '_update_form'
    template_name = 'schools/update.html'
    success_url = reverse_lazy('list_students')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar escuelas'

        return context


class SchoolDeleteView(LoginRequiredMixin, DeleteView):
    model = School
    login_url = reverse_lazy('login')
    template_name = 'schools/delete.html'
    success_url = reverse_lazy('list_students')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar escuelas'

        return context
