from django.db import models
# Create your models here.
class Medicines(models.Model):
    bookName   = models.CharField(max_length=255, blank=True, null=True)
    medName    = models.CharField(max_length=255, blank=True, null=True)
    medDetails = models.TextField(blank=True, null=True)
    Section    = models.CharField(max_length=255, blank=True, null=True)
 

class BoerickConv(models.Model):
    no_items = models.IntegerField(primary_key=True)
    no_meds = models.IntegerField()
    book_name = models.CharField(max_length=8)
    med_name = models.CharField(max_length=41)
    section = models.CharField(max_length=22)
    med_details = models.CharField(max_length=3856)

    class Meta:
        managed = False
        db_table = 'boerick_conv'