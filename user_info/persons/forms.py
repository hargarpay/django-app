from django import forms, core
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["fullname", "email"]
        widgets = {
            'email': forms.EmailInput(),
            'fullname': forms.TextInput()
        }

    def clean_email(self):
        email = self.cleaned_data['email']

        if Person.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

