from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from egress.forms import EgressForm
from egress.models import Egress


# Create your views here.

class EgressListView(LoginRequiredMixin, ListView):
    model = Egress
    login_url = reverse_lazy('login')
    template_name = 'egress/read.html'
    success_url = reverse_lazy('list_users')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de usuarios'

        return context


class EgressCreateView(LoginRequiredMixin, CreateView):
    model = Egress
    form_class = EgressForm
    login_url = reverse_lazy('login')
    template_name = 'egress/create.html'
    success_url = reverse_lazy('list_users')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear usuarios'

        return context


class EgressUpdateView(LoginRequiredMixin, UpdateView):
    model = Egress
    form_class = EgressForm
    login_url = reverse_lazy('login')
    template_name_suffix = '_update_form'
    template_name = 'egress/update.html'
    success_url = reverse_lazy('list_users')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar usuarios'

        return context


class EgressDeleteView(LoginRequiredMixin, DeleteView):
    model = Egress
    login_url = reverse_lazy('login')
    template_name = 'egress/delete.html'
    success_url = reverse_lazy('list_users')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar usuarios'

        return context
