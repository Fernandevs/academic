from django.contrib import admin
from django.contrib.auth.models import Permission

from users.models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Permission)
