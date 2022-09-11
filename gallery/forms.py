from django import forms
from django.forms import ModelForm
from .models import Images

class ImagesForm(ModelForm):
    
    class Meta:
        model = Images
        fields = ('image', 'caption')