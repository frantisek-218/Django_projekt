from django import forms
from .models import Klub


class MatFotbalForm(forms.ModelForm):
    class Meta:
        model = Klub
        fields = ['nazev', 'zalozeni', 'zeme',
                  'trener', 'liga', 'foto_klubu',
                  'turnaje']
        
        