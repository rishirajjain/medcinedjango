from django.shortcuts import render
from .models import Medicines,BoerickConv
# Create your views here.

def home_view(request):
    obj= Medicines.objects.all()
    context={
        'object':obj,
       
    }
    return render(request,"list_meds.html",context)


def med_view(request):
    ob= BoerickConv.objects.all()
    context={
        'object':ob,
       
    }
    return render(request,"med.html",context)

