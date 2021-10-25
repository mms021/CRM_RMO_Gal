from django.db import models
from projects.models import Projects , ProductProd
# Create your models here.
CHOI = [
    ('СЗ','Служебная записка '),
    ('ПНП','Приказ о назначении пресейл-команды'),
    ('ПО','Проектный отчет'),
    ('НДА','NDA'),
    ('ПРС','Пресейл'),
    ('ЭО','Экспресс-обслеование'),
    ('ПРЕ','Презентации'),
    ('ОРГ','Организацонные предприятия'),
    ('ОБС','Обследование'),
    ('ТЗ','Техническое задание'),
    ('ПР','Проектное решение'),
    ('СД','Сбор данных'),
    ('РЕА','Реализация'),
    ('ОЭ','Опытная эксплуотация'),
    ('ТИР','Тиражирование'),
    ('ПЗП','Презентация завершения проекта'),
    ('АЗ','Аналитическая записка'),
    ('ШСА','Шаблон статус отчета'),
    ('ШП','Шаблон протокотла'),
    ('РР','Реестр рисков'),
    ('ШПГ','Шаблон Плана-гарфика преокта'),
    ('ШПИ','Шаблон писем'),
    ('ПРОЧ','Прочее'),

]

class BazaZnaniy(models.Model):
    # Название Документа
    title = models.CharField(
        max_length=100,
    )
    #Тип документа
    tip =  models.CharField(
        max_length=10,
        choices=CHOI,
    )
    #Описание
    opisan = models.TextField(
        default='',
        blank=True,
        null=True,
    )
    # документ
    filefild = models.FileField(
        upload_to='baza',
    )
    # ТЭГИ ДОКУМЕНТОВ  
    products = models.ManyToManyField(
        ProductProd,
        blank=True,
    )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )
    
    objects = models.Manager()

    def __str__(self):
        return self.title









