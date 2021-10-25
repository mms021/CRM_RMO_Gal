from django.contrib import admin

# Register your models here.

from preseil.models import PresailProjects, StadiiProdaj ,KomentForPresail  , ProductOf ,PresProjNew

admin.site.register(PresailProjects)
admin.site.register(StadiiProdaj)
admin.site.register(KomentForPresail)
admin.site.register(ProductOf)
admin.site.register(PresProjNew)