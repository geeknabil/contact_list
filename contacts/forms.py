from django import forms
from .models import Contact, PhoneNumber
from django.forms.models import inlineformset_factory

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name']

PhoneNumberFormSet = inlineformset_factory(Contact, PhoneNumber, fields=['number'], extra=3)
