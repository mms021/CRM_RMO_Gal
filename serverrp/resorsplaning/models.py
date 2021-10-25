from django.db import models

# Create your models here.
from django.db import models

from projects.models import Projects , Itap 
from resurses.models import  Cotrudniri

# Create your models here.
class OtMonf(models.Model):
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

class PlanForMyWok(models.Model):
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
        OtMonf,
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

