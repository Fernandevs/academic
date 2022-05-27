from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from users.forms import UserCreateForm, UserUpdateForm
from users.models import User

# Create your views here.


class UserListView(LoginRequiredMixin, ListView):
    model = User
    login_url = reverse_lazy('login')
    template_name = 'users/read.html'
    success_url = reverse_lazy('list_users')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de usuarios'

        return context


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserCreateForm
    login_url = reverse_lazy('login')
    template_name = 'users/create.html'
    success_url = reverse_lazy('list_users')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear usuarios'

        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    login_url = reverse_lazy('login')
    template_name_suffix = '_update_form'
    template_name = 'users/update.html'
    success_url = reverse_lazy('list_users')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar usuarios'

        return context


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    login_url = reverse_lazy('login')
    template_name = 'users/delete.html'
    success_url = reverse_lazy('list_users')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar usuarios'

        return context
