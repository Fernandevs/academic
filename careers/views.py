from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from careers.forms import CareerCreateForm, CareerUpdateForm
from careers.models import Career

# Create your views here.


class CareerListView(
    ListView,
    LoginRequiredMixin
):
    model = Career
    template_name = 'careers/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de carreras'

        return context


class CareerCreateView(
    CreateView,
    LoginRequiredMixin
):
    model = Career
    form_class = CareerCreateForm
    template_name = 'careers/create.html'
    success_url = reverse_lazy('list_careers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear carreras'

        return context


class CareerUpdateView(
    UpdateView,
    LoginRequiredMixin
):
    model = Career
    form_class = CareerUpdateForm
    template_name_suffix = '_update_form'
    template_name = 'careers/update.html'
    success_url = reverse_lazy('list_careers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar carreras'

        return context


class CareerDeleteView(
    DeleteView,
    LoginRequiredMixin
):
    model = Career
    template_name = 'careers/delete.html'
    success_url = reverse_lazy('list_careers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar carreras'

        return context
