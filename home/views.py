import django.contrib.auth

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.


def login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user is not None:
            django.contrib.auth.login(request, user)
            return HttpResponseRedirect(reverse_lazy('dashboard'))

    return render(request, 'login.html')


def not_found(request):
    return render(
        request=request,
        template_name='404.html'
    )


@login_required
def logout(request):
    django.contrib.auth.logout(request)

    return HttpResponseRedirect(reverse_lazy('login'))
