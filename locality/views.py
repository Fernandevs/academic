from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from locality.forms import LocalityForm
from locality.models import Locality

# Create your views here.


class LocalityListView(LoginRequiredMixin, ListView):
    model = Locality
    login_url = reverse_lazy('login')
    template_name = 'localities/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de localidades'

        return context


class LocalityCreateView(LoginRequiredMixin, CreateView):
    model = Locality
    form_class = LocalityForm
    login_url = reverse_lazy('login')
    template_name = 'localities/create.html'
    success_url = reverse_lazy('list_locality')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear localidad'

        return context


class LocalityUpdateView(LoginRequiredMixin, UpdateView):
    model = Locality
    form_class = LocalityForm
    login_url = reverse_lazy('login')
    template_name_suffix = '_update_form'
    template_name = 'localities/update.html'
    success_url = reverse_lazy('list_locality')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar localidad'

        return context


class LocalityDeleteView(LoginRequiredMixin, DeleteView):
    model = Locality
    login_url = reverse_lazy('login')
    template_name = 'localities/delete.html'
    success_url = reverse_lazy('list_locality')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar localidad'

        return context
