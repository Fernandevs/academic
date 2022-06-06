from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'groups',
            'user_image'
        ]

        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre(s)',
            'last_name': 'Apellidos',
            'email': 'Correo',
            'groups': 'Rol',
            'user_image': 'Imagen de perfil'
        }


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User

        fields = [
            'username',
            'last_name',
            'email',
            'groups',
            'user_image',
            'is_superuser'
        ]

        labels = {
            'username': 'Nombre de usuario',
            'last_name': 'Apellidos',
            'email': 'Correo',
            'groups': 'Rol',
            'user_image': 'Imagen de perfil',
            'is_superuser': 'Es administrador'
        }
