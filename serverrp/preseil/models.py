from django.db import models
from resurses.models import Compani , Cotrudniri
from projects.models import Projects
# Create your models here.
from django.contrib.auth.models import User

class ProductOf(models.Model):
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=100,
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

    summa = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )


    def __str__(self):
        return self.title

class PresailProjects(models.Model):
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    veroytnost = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    kanal = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    kontrok = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    polzvt = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    menedler = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    product = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    summa = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    products = models.ManyToManyField(
        ProductOf,
        blank=True,
    )
    menedjer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    vzaimodeistvie = models.ForeignKey(
        Cotrudniri,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    zakazchic = models.ForeignKey(
        Compani,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    holding = models.ForeignKey(
        Compani,
        on_delete=models.SET_NULL,
        related_name = 'holding',
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


class PresProjNew(Projects):
    veroytnost = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    
    kanal = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    kontrok = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    polzvt = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    summa = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title


class StadiiProdaj(models.Model):
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    # Первичное знакомство
    znacomstvostatus = models.CharField(
        default="Не начат",
        max_length=200,
        blank=True,
        null=True,
    )
    znacomstvo = models.TextField(
        default='',
        blank=True,
        null=True,
    )
    # Инициирующее письмо
    pismostatus = models.CharField(
        default="Не начат",
        max_length=200,
        blank=True,
        null=True,
    )
    pismo = models.TextField(
        blank=True,
        null=True,
        default='',
    )
    # Первая встреча, презентация
    vstrethastatus = models.CharField(
        default="Не начат",
        max_length=200,
        blank=True,
        null=True,
    )
    vstretha = models.TextField(
        blank=True,
        null=True,
        default='',
    )
    # Определены потенциальные направления
    napravleniastatus = models.CharField(
        default="Не начат",
        max_length=200,
        blank=True,
        null=True,
    )
    napravlenia = models.TextField(
        blank=True,
        null=True,
        default='',
    )
    # Согласована дорожная карта мероприятий
    kartadorogstatus = models.CharField(
        default="Не начат",
        max_length=200,
        blank=True,
        null=True,
    )
    kartadorog = models.TextField(
        blank=True,
        null=True,
        default='',
    )
    # Экспресс-обследование, подготовка предложения
    obsledstatus = models.CharField(
        default="Не начат",
        max_length=200,
        blank=True,
        null=True,
    )
    obsled = models.TextField(
        blank=True,
        null=True,
        default='',
    )
    # Pешение орг вопросов (письма, пропуска, план)
    orgvoprosstatus = models.CharField(
        default="Не начат",
        max_length=200,
        blank=True,
        null=True,
    )
    orgvopros = models.TextField(
        blank=True,
        null=True,
        default='',
    )
    # Проведение интервью
    interviustatus = models.CharField(
        default="Не начат",
        max_length=200,
        blank=True,
        null=True,
    )
    interviu = models.TextField(
        blank=True,
        null=True,
        default='',
    )
    # Формирование и согласование отчета
    otchetstatus = models.CharField(
        default="Не начат",
        max_length=200,
        blank=True,
        null=True,
    )
    otchet = models.TextField(
        blank=True,
        null=True,
        default='',
    )
    # Защита отчета
    zachitaotchstatus = models.CharField(
        default="Не начат",
        max_length=200,
        blank=True,
        null=True,
    )
    zachitaotch = models.TextField(
        blank=True,
        null=True,
        default='',
    )
    # Формирование предложения (бюджетной оценки)
    formirovaniepredstatus = models.CharField(
        default="Не начат",
        max_length=200,
        blank=True,
        null=True,
    )
    formirovaniepred = models.TextField(
        blank=True,
        null=True,
        default='',
    )
    # Согласование предложения
    predlojeniestatus = models.CharField(
        default="Не начат",
        max_length=200,
        blank=True,
        null=True,
    )
    predlojenie = models.TextField(
        blank=True,
        null=True,
        default='',
    )
    # Согласовано у нас
    soglosovaniezactatus = models.CharField(
        default="Не начат",
        max_length=200,
        blank=True,
        null=True,
    )
    soglosovanie = models.TextField(
        blank=True,
        null=True,
        default='',
    )
    # Передано на согласование Заказчику
    soglosovaniezacstatus = models.CharField(
        default="Не начат",
        max_length=200,
        blank=True,
        null=True,
    )
    soglosovaniezac = models.TextField(
        blank=True,
        null=True,
        default='',
    )
    # Получена обратная связь
    obratnazsvazstatus = models.CharField(
        default="Не начат",
        max_length=200,
        blank=True,
        null=True,
    )
    obratnazsvaz = models.TextField(
        blank=True,
        null=True,
        default='',
    )
    # Сформировано итоговое предложение
    predlojeniestatusitog = models.CharField(
        default="Не начат",
        max_length=200,
        blank=True,
        null=True,
    )
    predlojenieitog = models.TextField(
        blank=True,
        null=True,
        default='',
    )
    # Подготовка конкурсной документации
    konkyrsnazdocstatus = models.CharField(
        default="Не начат",
        max_length=200,
        blank=True,
        null=True,
    )
    konkyrsnazdoc = models.TextField(
        blank=True,
        null=True,
        default='',
    )

    # Конкурсные процедуры
    konkursstatus = models.CharField(
        default="Не начат",
        max_length=200,
        blank=True,
        null=True,
    )
    konkurs = models.TextField(
        blank=True,
        null=True,
        default='',
    )
    # priail = models.ForeignKey(
    #     PresailProjects,
    #     on_delete=models.CASCADE,
    #     blank=True,
    #     null=True,
    # )
    
    priailnnew = models.ForeignKey(
        PresProjNew,
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


class KomentForPresail(models.Model):
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    statuschek = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    koment = models.TextField(
        default='',
        blank=True,
        null=True,
    )
    plan = models.TextField(
        default='',
        blank=True,
        null=True,
    )
    # priail = models.ForeignKey(
    #     PresailProjects,
    #     on_delete=models.CASCADE,
    #     blank=True,
    #     null=True,
    # )
    priailnnew = models.ForeignKey(
        PresProjNew,
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

    class Meta:
        ordering = ['-modified',]
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    statuschek = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    koment = models.TextField(
        default='',
        blank=True,
        null=True,
    )
    plan = models.TextField(
        default='',
        blank=True,
        null=True,
    )
    priail = models.ForeignKey(
        PresailProjects,
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

    class Meta:
        ordering = ['-modified',]