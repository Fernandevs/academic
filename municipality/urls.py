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

from municipality.views import *


urlpatterns = [
    path('municipalities/list/', MunicipalityListView.as_view(), name='list_municipality'),
    path('municipalities/create/', MunicipalityCreateView.as_view(), name='create_municipality'),
    path('municipalities/update/<int:pk>/', MunicipalityUpdateView.as_view(), name='update_municipality'),
    path('municipalities/delete/<int:pk>/', MunicipalityDeleteView.as_view(), name='delete_municipality'),
]
