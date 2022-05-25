from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from students.forms import StudentForm
from students.models import Student


# Create your views here.

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    login_url = reverse_lazy('login')
    template_name = 'students/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de estudiantes'

        return context


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    login_url = reverse_lazy('login')
    template_name = 'students/create.html'
    success_url = reverse_lazy('list_students')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear estudiantes'

        return context


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    login_url = reverse_lazy('login')
    template_name_suffix = '_update_form'
    template_name = 'students/update.html'
    success_url = reverse_lazy('list_students')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar estudiantes'

        return context


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    login_url = reverse_lazy('login')
    template_name = 'students/delete.html'
    success_url = reverse_lazy('list_students')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar estudiantes'

        return context
