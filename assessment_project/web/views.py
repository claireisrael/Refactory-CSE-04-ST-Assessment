from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PassengerForm

def register(request):
    if request.method == "POST":
        form = PassengerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Form has been submitted successfully!")
            return redirect("register")  # reloads the form page cleanly
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PassengerForm()

    return render(request, "register.html", {"form": form})
