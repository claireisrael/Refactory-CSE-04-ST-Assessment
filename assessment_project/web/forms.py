from django import forms
from .models import Passenger
class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = '__all__'

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),      
            'gender': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Gender'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control','type': 'email'}),
            'po_box_number': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_phone_number': forms.TextInput(attrs={'class': 'form-control'}),         
            'passport_number': forms.TextInput(attrs={'class': 'form-control'}),
            'visa_document': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Upload File'}),
            'departure_city': forms.TextInput(attrs={'class': 'form-control'}),
            'destination_city': forms.TextInput(attrs={'class': 'form-control'}),   
        }

        error_messages = {
        'full_name': { 'required': 'Invalid Field' },
        'gender': { 'required': 'Invalid Field' },
        'date_of_birth': { 'required': 'Invalid Field' },          
        'nationality': { 'required': 'Invalid Field' },
        'phone_number': { 'required': 'Invalid Field' },
        'email_address': { 'required': 'Invalid Field' },
        'po_box_number': { 'required': 'Invalid Field' },
        'emergency_phone_number': { 'required': 'Invalid Field' },
        'passport_number': { 'required': 'Invalid Field' },
        'visa_document': { 'required': 'Invalid Field' },
        'departure_city': { 'required': 'Invalid Field' },  
        'destination_city': { 'required': 'Invalid Field' },
        }       