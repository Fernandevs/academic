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

from locality.views import *


urlpatterns = [
    path('localities/list/', LocalityListView.as_view(), name='list_locality'),
    path('localities/create/', LocalityCreateView.as_view(), name='create_locality'),
    path('localities/massive/', LocalityMassiveTemplateView.as_view(), name='massive_locality'),
    path('localities/update/<int:pk>/', LocalityUpdateView.as_view(), name='update_locality'),
    path('localities/delete/<int:pk>/', LocalityDeleteView.as_view(), name='delete_locality'),
]
