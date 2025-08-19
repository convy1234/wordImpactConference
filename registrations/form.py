from django import forms
from .models import Registration


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Registration
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "attendance",
            "church",
            "city"
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email Address"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone Number"}),
            "attendance": forms.Select(attrs={"class": "form-select"}),
            "church": forms.TextInput(attrs={"class": "form-control", "placeholder": "Church Name"}),
            "city": forms.TextInput(attrs={"class": "form-control", "placeholder": "City"}),
        }
