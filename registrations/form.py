from django import forms
from .models import Registration


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Registration
        fields = [
            "title",
            "first_name",
            "last_name",
            "email",
            "gender",
            "phone",
            "attendance",
            "church",
            "city",
            "expectation"
        ]
        widgets = {
            "title": forms.Select(attrs={"class": "form-select"}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email Address"}),
            "gender": forms.Select(attrs={"class": "form-select"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone Number"}),
            "attendance": forms.Select(attrs={"class": "form-select"}),
            "church": forms.TextInput(attrs={"class": "form-control", "placeholder": "Church Name"}),
            "city": forms.TextInput(attrs={"class": "form-control", "placeholder": "City"}),
            "expectation": forms.Textarea(attrs={"class": "form-control", "placeholder": "Your Expectations", "rows": 3}),
        }

