from .models import NomerForPismo
from django import forms

class FileForm(forms.Form):
    #title = forms.CharField(max_length=50)
    file = forms.FileField()


class PismoForm(forms.ModelForm):
    class Meta:
        model = NomerForPismo
        fields = ['trec','filefild' ]
        labels = { 'trec': ('Трек номер'),"filefild":('Файл')}


        
