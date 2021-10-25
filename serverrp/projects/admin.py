from django.contrib import admin
from .models import Projects, Itap ,Zadania, Dopsog , Komanda , Zadachirp , Problems , Risk , Mani , Documents , Cost , ProductProd

# Register your models here.
admin.site.register(Projects)
admin.site.register(Itap)
admin.site.register(Komanda)
admin.site.register(Dopsog)
admin.site.register(Zadania)
admin.site.register(Zadachirp)
admin.site.register(Risk)
admin.site.register(Problems)
admin.site.register(Mani)
admin.site.register(Documents)
admin.site.register(Cost)
admin.site.register(ProductProd)