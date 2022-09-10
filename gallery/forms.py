from django import forms
from django.forms import ModelForm

class ImagesForm(ModelForm):
    
    class Meta:
        model = Images
        fields = ("user",'image', 'caption')