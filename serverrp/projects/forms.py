from django import forms
from django.forms.formsets import formset_factory
from django.forms import ModelForm

from .models import Projects ,Itap


class ItapApdete(forms.Form):
    
    komentrp = forms.CharField(widget=forms.Textarea, required=False)

    act = forms.CharField(widget=forms.Textarea, required=False)

    oplata = forms.CharField(widget=forms.Textarea, required=False)

    
class ItapAP(ModelForm):
    class Meta:
        model = Itap
        fields = ['komentrp']    

    
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    