from django.db import models

from projects.models import Projects , Itap 

from django.contrib.auth.models import User
# Create your models here.
import uuid 


class Compani(models.Model):
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    opisanie = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default='',
    )
    director = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default='',
    )
    naimvsisteme = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default='',
    ) 
    telefon = models.CharField(
        max_length=400,
        blank=True,
        null=True,
        default='',
    )
    email = models.CharField(
        max_length=400,
        blank=True,
        null=True,
        default='',
    )
    sait = models.CharField(
        max_length=400,
        blank=True,
        null=True,
        default='',
    )
    otraasal = models.CharField(
        max_length=400,
        blank=True,
        null=True,
        default='',
    )
    inn = models.CharField(
        max_length=400,
        blank=True,
        null=True,
        default='',
    )
    kontakt = models.CharField(
        max_length=400,
        blank=True,
        null=True,
        default='',
    )
    adres = models.CharField(
        max_length=400,
        blank=True,
        null=True,
        default='',
    )
    main_comp = models.ForeignKey(
        "Compani",
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
        return self.title

class Otdel(models.Model):
    title = models.CharField(
        max_length=500,
        blank=True,
        null=True,
    )

    level = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    opisanie = models.CharField(
        max_length=500,
        blank=True,
        null=True,
    )
    rpotdela = models.CharField(
        max_length=250,
        blank=True,
        null=True,
    )
    rpmail = models.CharField(
        max_length=250,
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
        return self.title
    
    class Meta:
        ordering = ["title"]

class Contacts(models.Model):
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
   
    doljnost = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default='',
    )
    compani = models.CharField(
        max_length=250,
        blank=True,
        null=True,
    )
    priseday = models.CharField(
        max_length=250,
        blank=True,
        null=True,
    )
    mail = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        default='',
    )

    telnomder = models.CharField(
        max_length=250,
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
        return self.title

# django.db.utils.OperationalError: foreign key mismatch - "resurses_zaiyvka" referencing "resurses_contacts"

class Zaiyvka(models.Model):
    title = models.CharField(
        max_length=500,
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
        return self.title

class Zadatha(models.Model):
    title = models.CharField(
        max_length=500,
        blank=True,
        null=True,
    )
    chec = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    zada = models.TextField(
        blank=True,
        null=True,
    )

    
    projects = models.ForeignKey(
        Projects,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    prior = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )


    srok = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    otvet = models.CharField(
        max_length=150,
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
        return self.title

    class Meta:
        ordering = ['-modified',]

class Cotrudniri(models.Model):
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    index = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID ")
    #Г  URL
    urlform = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    statusof = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        default='',
    )
    podraz = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default='',
    )

    tip = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    doljnost = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default='',
    )
    compan = models.ForeignKey(
        Compani,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    compani = models.CharField(
        max_length=250,
        blank=True,
        null=True,
    )
    priseday = models.CharField(
        max_length=250,
        blank=True,
        null=True,
    )
    mail = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        default='',
    )

    telnomder = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        default='',
    )
    
    ondel = models.ForeignKey(
        Otdel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    projects = models.ManyToManyField(
        Projects,
        blank=True,
    )
    datafilds = models.DateTimeField(
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
        return self.title

    class Meta:
        ordering = ["title"]

class OtchetforMonf(models.Model):
    # месяц 
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    # дней в месяце
    daysinmonf = models.CharField(
        max_length=200,
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
        return self.title

class PriseofmyWok(models.Model):
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    soglos = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    rezalt = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    itap = models.ForeignKey(
        Itap,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    otch = models.ForeignKey(
        OtchetforMonf,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    projects = models.ForeignKey(
        Projects,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
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






""" 
БД 

ЗАЯВКА 
Дата (месяц)
Процент (План)
Процент (Факт)
Проект - ПРОЕКТ 
Работник -РАБОТНИК 
Согласование 
Статус задчи


ОТДЕЛ 
Название отдела
Информация по отделу



РАБОТНИК / КОНТАКТЫ 
ФИО 
Должность 
Компания 
Почта
Телефон 
Отдел -ОТДЕЛ
Цена (дня-часа)

"""