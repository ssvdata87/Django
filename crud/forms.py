from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}))
    description=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Description'}))
    class Meta:
        model = Item
        fields = ['name', 'description']
