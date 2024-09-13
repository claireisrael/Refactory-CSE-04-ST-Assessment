from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from datetime import date
import re

# Create your models here.

def clean_date_of_birth(self):
        dob = self.cleaned_data.get('date_of_birth')
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if age < 18 or age > 99:
            raise ValidationError('Passenger must be between 18 and 99 years old.')
        return dob



def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if not re.match(r"^[a-zA-Z]+(\s[a-zA-Z]+)*$", full_name):
            raise ValidationError('Full name must contain only letters and spaces.')
        return full_name

class Passenger(models.Model):
    gender = [('Male', 'Male'),('Female', 'Female')]
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=gender)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField()
    po_box = models.CharField(max_length=100, blank=True, null=True)
    emergency_phone_number = models.CharField(max_length=15)
    passport_number = models.CharField(max_length=20)
    passport_number = models.CharField(null=True, max_length=20)
    departure_city = models.CharField(max_length=50)
    destination_city = models.CharField(max_length=50)
    visa_document = models.ImageField() 

    def __str__(self):
        return self.full_name

