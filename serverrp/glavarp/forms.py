from django import forms


class UploadDocumentForm(forms.Form):
    file = forms.FileField()

class UploadFileForm(forms.Form):
    file = forms.FileField()

class UploadImageForm(forms.Form):
    image = forms.ImageField()