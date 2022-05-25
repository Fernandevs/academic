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

from egress.views import *

urlpatterns = [
    path('egress/list/', EgressListView.as_view(), name='list_egress'),
    path('egress/create/', EgressCreateView.as_view(), name='create_egress'),
    path('egress/update/<int:pk>/', EgressUpdateView.as_view(), name='update_egress'),
    path('egress/delete/<int:pk>/', EgressDeleteView.as_view(), name='delete_egress'),
]
