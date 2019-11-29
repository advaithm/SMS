from django.db import models
from django_tables2 import tables
#from chem_lab.models import student
# Create your models here.
class bio_broken_eq(models.Model):
  bio_eq_id = models.IntegerField(primary_key = True)
  student = models.ForeignKey("chem_lab.student", verbose_name=("student"), on_delete=models.CASCADE)
  bio_eq_name = models.CharField(max_length=50)
  bio_eq_number = models.IntegerField()
  bio_eq_cost = models.IntegerField()

class bio_eq(models.Model):
  bio_eq_id = models.IntegerField(primary_key=True)
  bio_eq_name = models.CharField(max_length=50)
  bio_eq_amount = models.PositiveIntegerField()

class ContactTable(tables.Table):
    #edit_entries = tables.LinkColumn('<a href="/equipment/{{record.id}}">Edit</a>')

    class Meta:
        model = bio_eq
        attrs = {"class": "paleblue"}