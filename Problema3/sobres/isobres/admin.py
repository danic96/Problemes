from django.contrib import admin

# Register your models here.
from isobres.models import Empresa, Sobre
admin.site.register(Sobre)
admin.site.register(Empresa)
