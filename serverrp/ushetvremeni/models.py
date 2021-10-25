from django.db import models

# Create your models here.
from resurses.models import  Cotrudniri



class UshetResursov(models.Model):
    # Номер недели 
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    # Год 
    year = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    rezalt = models.CharField(
        max_length=200,
        default= '8,8,8,8,8,В,В'
    )
    cotrud = models.ForeignKey(
        Cotrudniri,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    objects = models.Manager()

    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )
    def __str__(self):
        return f'{self.title } {self.cotrud}'  


















