# forms.py
from django import forms
from .models import Items,News

class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'category', 'description', 'price', 'Img', 'is_delivery_available']
        

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['Title','desc','Imag']

