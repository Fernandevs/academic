import django.contrib.auth

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from users.forms import UserCreateForm, UserUpdateForm
from users.models import User


# Create your views here.

def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            django.contrib.auth.login(request, user)
            return HttpResponseRedirect(reverse_lazy('dashboard'))

    return render(request, 'login.html')


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


@login_required
def logout(request):
    django.contrib.auth.logout(request)

    return HttpResponseRedirect(reverse_lazy('login'))
