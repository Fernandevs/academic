from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from state.forms import StateForm
from state.models import State

# Create your views here.


class StateListView(LoginRequiredMixin, ListView):
    model = State
    login_url = reverse_lazy('login')
    template_name = 'states/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de estados'

        return context


class StateCreateView(LoginRequiredMixin, CreateView):
    model = State
    form_class = StateForm
    login_url = reverse_lazy('login')
    template_name = 'states/create.html'
    success_url = reverse_lazy('list_state')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear localidad'

        return context


class StateUpdateView(LoginRequiredMixin, UpdateView):
    model = State
    form_class = StateForm
    login_url = reverse_lazy('login')
    template_name_suffix = '_update_form'
    template_name = 'states/update.html'
    success_url = reverse_lazy('list_state')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar localidad'

        return context


class StateDeleteView(LoginRequiredMixin, DeleteView):
    model = State
    login_url = reverse_lazy('login')
    template_name = 'states/delete.html'
    success_url = reverse_lazy('list_state')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar localidad'

        return context
