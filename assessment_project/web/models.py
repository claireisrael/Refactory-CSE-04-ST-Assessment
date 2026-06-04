from django.db import models

# Create your models here.
class Passenger(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female')
    ]
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    po_box_number = models.CharField("P.O.BOX Number", max_length=50, blank=True, null=True)
    emergency_phone_number = models.CharField(max_length=20, blank=True, null=True)
    passport_number = models.CharField(max_length=50, blank=True, null=True)
    visa_document = models.CharField(max_length=50, blank=True, null=True)
    departure_city = models.CharField(max_length=50)
    destination_city = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name

    
