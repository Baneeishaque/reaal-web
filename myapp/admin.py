from django.contrib import admin

# Register your models here.
from .models import Login,Home

admin.site.register(Login)
admin.site.register(Home)