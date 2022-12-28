from django import forms 
from .models import Postingmodel

class Postform(forms.ModelForm):

#    Name = 'Postform'
    class Meta:
        model = Postingmodel
        fields = ("Title",)





