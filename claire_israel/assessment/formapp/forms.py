from django import forms
from .models import Passenger
from django.core.validators import RegexValidator

class PassengerForm(forms.ModelForm):
    # Validators
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', 
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    class Meta:
        model = Passenger
        fields = '__all__'  
    
    
    full_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Full Name'
    )
    gender = forms.ChoiceField(
        required=True,
        choices=[('Male', 'Male'), ('Female', 'Female')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Gender'
    )
    date_of_birth = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label='Date of Birth'
    )
    nationality = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Nationality'
    )
    phone_number = forms.CharField(
        required=True,
        validators=[phone_regex],
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Phone Number'
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        label='Email'
    )
    po_box = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='P.O. Box'
    )
    emergency_phone_number = forms.CharField(
        required=True,
        validators=[phone_regex],
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Emergency Phone Number'
    )
    passport_number = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Passport Number'
    )
    departure_city = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Departure City'
    )
    destination_city = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Destination City'
    )
    visa_document = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        label='Visa Document'
    )
