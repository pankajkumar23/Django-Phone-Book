from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'email']

class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=255, required=False)
