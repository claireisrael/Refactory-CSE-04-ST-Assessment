from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import  PassengerForm
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        form =  PassengerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form has been submitted successfully')
            return redirect('index')
        else:
            messages.error(request, 'Form is not valid')
    else:
        form =  PassengerForm()
    return render(request, 'index.html', {'form': form})

