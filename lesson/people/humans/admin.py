from django.contrib import admin

# Register your models here.
from .models import Man, Passport

admin.site.register(Man, Passport)