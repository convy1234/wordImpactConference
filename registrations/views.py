# registrations/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .form import RegistrationForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration received. See you at Word Impact ’25!")
            return redirect("registration_success")  # go to success page
    else:
        form = RegistrationForm()
    return render(request, "registrations/register.html", {"form": form})


def registration_success(request):
    return render(request, "registrations/registration_success.html")
