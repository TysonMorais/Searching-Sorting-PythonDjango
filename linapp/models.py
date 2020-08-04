from django.db import models

# Create your models here.
class Datas(models.Model):
    user_name = models.CharField(max_length=100)
    guardian_name = models.CharField(max_length=100)
    house_no = models.IntegerField()
    house_name = models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Others'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()
    id_card_no = models.CharField(max_length=100)
    booth_no = models.IntegerField()