from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from djangoql.admin import DjangoQLSearchMixin

from .models import User

admin.site.register(User, UserAdmin)
