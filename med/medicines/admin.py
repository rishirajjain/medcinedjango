from django.contrib import admin

# Register your models here.
from .models import Medicines,BoerickConv
admin.site.register(Medicines)
admin.site.register(BoerickConv)

