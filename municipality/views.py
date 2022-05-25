from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from municipality.forms import MunicipalityForm
from municipality.models import Municipality

# Create your views here.


class MunicipalityListView(LoginRequiredMixin, ListView):
    model = Municipality
    login_url = reverse_lazy('login')
    template_name = 'municipalities/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de municipios'

        return context


class MunicipalityCreateView(LoginRequiredMixin, CreateView):
    model = Municipality
    form_class = MunicipalityForm
    login_url = reverse_lazy('login')
    template_name = 'municipalities/create.html'
    success_url = reverse_lazy('list_municipality')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear municipio'

        return context


class MunicipalityUpdateView(LoginRequiredMixin, UpdateView):
    model = Municipality
    form_class = MunicipalityForm
    login_url = reverse_lazy('login')
    template_name_suffix = '_update_form'
    template_name = 'municipalities/update.html'
    success_url = reverse_lazy('list_municipality')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar municipio'

        return context


class MunicipalityDeleteView(LoginRequiredMixin, DeleteView):
    model = Municipality
    login_url = reverse_lazy('login')
    template_name = 'municipalities/delete.html'
    success_url = reverse_lazy('list_municipality')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar municipio'

        return context
