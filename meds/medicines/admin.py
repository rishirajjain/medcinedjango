from django.contrib import admin

# Register your models here.
from .models import Medicines,BoerickeJoints
admin.site.register(Medicines)
admin.site.register(BoerickeJoints)

