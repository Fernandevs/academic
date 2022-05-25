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
from django.conf.urls.static import static
from django.urls import path

from academic import settings
from users.views import *

urlpatterns = [
    path('users/login/', login, name='login'),
    path('users/create/', UserCreateView.as_view(), name='create_user'),
    path('users/list/', UserListView.as_view(), name='list_users'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='update_user'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='delete_user'),
    path('users/logout/', logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
