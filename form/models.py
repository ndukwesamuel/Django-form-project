from django.db import models
from django.db.models.fields import CharField

class myModel(models.Model):
    first_name = models.CharField(max_length=40, default='Mofe')
    last_name = models.CharField(max_length=40, default='Mofe')
    other_names = models.CharField(max_length=30, default='Mofe')
    a_k_a = models.CharField(max_length=20, default='Mofe')
    SEX_CHOICES = (
        ('m', 'male'),
        ('f', 'female')
    )
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='m')
    AGE_RANGE = (
        ('A', '<10'),
        ('B', '10 - 20'),
        ('C', '21 - 30')
    )
    age = models.CharField(max_length=1, choices=AGE_RANGE, default='A')
    height = models.CharField(max_length=10, default=12)
    date_declared_missing = models.DateField(default=12/12/2021)
    image_upload = models.ImageField()
    last_known_address = models.CharField(max_length=40, default='akjdfk')
    area = models.CharField(max_length=30, default='Mofe')
    city = models.CharField(max_length=30, default='Mofe')
    state = models.CharField(max_length=30, default='Mofe')
    email = models.CharField(max_length=30, default='Mofe@gmail.com')
    contact_name = models.CharField(max_length=40, default='Mofe')
    phone_number = models.CharField(max_length=11, default='08020310445')
    contact_person_email = models.CharField(max_length=30, default='django@gmail.com')
    contact_person_address = models.CharField(max_length=40, default='Mofe')
