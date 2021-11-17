from django.db import models
from django.db.models.fields import CharField

class myModel(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    other_names = models.CharField(max_length=30)
    a_k_a = models.CharField(max_length=20)
    SEX_CHOICES = (
        ('m', 'male'),
        ('f', 'female')
    )
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    AGE_RANGE = (
        ('A', '<10'),
        ('B', '10 - 20'),
        ('C', '21 - 30')
    )
    age = models.CharField(max_length=1, choices=AGE_RANGE)
    height = models.CharField(max_length=10)
    date_declared_missing = models.DateField()
    image_upload = models.ImageField()
    last_known_address = models.CharField(max_length=40)
    area = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    contact_name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=11)
    contact_person_email = models.CharField(max_length=30)
    contact_person_address = models.CharField(max_length=40)
