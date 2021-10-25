from django.db import models

# Create your models here.

class NomerForPismo(models.Model):
    # Предприятие
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default='',
    )
    # Нименование предприятия 
    komy = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default='',
    )
    # Номер письма 
    nomer = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        default='',
    )
    # первичный номер 
    pernom = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    # О чет 
    ochem = models.TextField(
        default='',
        blank=True,
        null=True,
    )
    # отвецтвеннсоть 
    otvetstven = models.CharField(
        max_length=200,
        default='',
        blank=True,
        null=True,
    )
    #трек номер 
    trec = models.CharField(
        max_length=200,
        default='',
        blank=True,
        null=True,
    )
    # Дата 
    data = models.TextField(
        default='',
        blank=True,
        null=True,
    )
    # Письмо 
    filefild = models.FileField(
        upload_to='leters/',
        blank=True,
        null=True,
        default='',
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
        return self.title

    class Meta:
        ordering = ['-modified',]