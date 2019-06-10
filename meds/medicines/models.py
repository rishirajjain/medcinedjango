from django.db import models
# Create your models here.
class Medicines(models.Model):
    bookName   = models.CharField(max_length=255, blank=True, null=True)
    medName    = models.CharField(max_length=255, blank=True, null=True)
    medDetails = models.TextField(blank=True, null=True)
    Section    = models.CharField(max_length=255, blank=True, null=True)
 

class BoerickeJoints(models.Model):
    medicine = models.CharField(max_length=75, blank=True, null=True)
    section = models.CharField(max_length=100, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    wrd = models.CharField(max_length=5, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'boericke_joints'