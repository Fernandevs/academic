"""academic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from careers.views import *

urlpatterns = [
    path('careers/list/', CareerListView.as_view(), name='list_careers'),
    path('careers/create/', CareerCreateView.as_view(), name='create_career'),
    path('careers/update/<int:pk>/', CareerUpdateView.as_view(), name='update_career'),
    path('careers/delete/<int:pk>/', CareerDeleteView.as_view(), name='delete_career'),
]
