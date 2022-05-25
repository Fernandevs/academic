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

from state.views import *


urlpatterns = [
    path('states/list/', StateListView.as_view(), name='list_state'),
    path('states/create/', StateCreateView.as_view(), name='create_state'),
    path('states/update/<int:pk>/', StateUpdateView.as_view(), name='update_state'),
    path('states/delete/<int:pk>/', StateDeleteView.as_view(), name='delete_state'),
]
