from django.db import models
# Create your models here.
class Medicines(models.Model):
    bookName   = models.CharField(max_length=255, blank=True, null=True)
    medName    = models.CharField(max_length=255, blank=True, null=True)
    medDetails = models.TextField(blank=True, null=True)
    
   