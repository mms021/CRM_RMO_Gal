from .models import BazaZnaniy
from django import forms


class NewBazaForm(forms.ModelForm):
    class Meta:
        model = BazaZnaniy
        fields = ['title','tip', 'opisan', "products", 'filefild']
        labels = { 'title': ('Название документа'), 'tip': ('Категория') , 'opisan' :('Описание'),'products': ('Продукты '),  "filefild":('Документ ') }
        





