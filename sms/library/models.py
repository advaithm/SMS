from django.db import models

# Create your models here.
class book_copy(models.Model):
    book_name = models.CharField(max_length=500)
    num_copy =  models.PositiveIntegerField()
    copies_available = models.PositiveIntegerField()
class book(models.Model):
    book_id = models.PositiveIntegerField(primary_key = True)
    book_name = models.CharField(max_length=500)
    availabity = models.BooleanField(default=True)
class issues(models.Model):
    book_id = models.PositiveIntegerField(primary_key = True)
    student_id = models.PositiveIntegerField()
    issue_date = models.DateField()
    return_date = models.DateField()