from django.contrib import admin

# Register your models here.
from .models import Login,Home,Registration

admin.site.register(Login)
admin.site.register(Home)
admin.site.register(Registration)