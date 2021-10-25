from django.db import models


# Create your models here.
OTSHET = [
    ('Н','Нет'),
    ('Д','Да')
]

ACT = [('П','Подписан'),('В','Выставлен'),('Н','Не Cформирован'),('Р','В работе')]

PLATA = [('З','Задолжность'),('О','Оплачен'),('Ж','Ожидаем')]

class ProductProd(models.Model):
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
    def __str__(self):
        return self.title


class Projects(models.Model):
    # Название проекта 
    title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    # Название преприятия 
    galactikanaumenovanie = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    # Название преприятия
    galactikaID = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    # Продукт 
    products = models.ManyToManyField(
        ProductProd,
        blank=True,
    )
    # Название проекта для системы  галактика 
    galactikatitle = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    # Руковоитель проекта
    rpproecta = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    ) 
    # Руководитель группы
    rucgrup = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    ) 
    # Кто коментирует 
    glavkoment = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    ) 
    compani = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    ) 
    
    # тип договора 
    tipdogovora= models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    # полное название сиситемы 
    polnoenazvanie = models.TextField(
        blank=True,
        null=True,
    )
    # название системы
    sistema = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    # Бюджет проекта
    prisepr = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    # бюджетзатрат
    prisezatrat = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    # щсвоено бюджета
    osvoeno= models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    # активный договор 
    activedog =  models.CharField(
        max_length=100,
        default="В работе"
        )
    # включение в итоговый отчет 
    otchtetm = models.CharField(
        max_length=100, 
        choices=OTSHET,
        blank=True,
        null=True,
    )
    # номер договора
    nomerdogovora= models.CharField(
        max_length=100,
        blank=True,
        null=True,
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

class Dopsog(models.Model):
    # ДС №
    title = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    # о чем
    prof = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )
    projects = models.ForeignKey(
        Projects,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    objects = models.Manager()
    
    def __str__(self):
        return self.title

#Risk
class Risk(models.Model):
    #проблема
    title = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    # серьезность 
    serios = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    #статус 
    status = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    #коментарий 
    koment = models.TextField(
        blank=True,
        null=True,
    )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )
    projects = models.ForeignKey(
        Projects,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    objects = models.Manager()
    
    def __str__(self):
        return self.title

class Cost(models.Model):
    title = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    # затраты  
    serios = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )
    projects = models.ForeignKey(
        Projects,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    objects = models.Manager()
    
    def __str__(self):
        return self.title

#Problems
class Problems(models.Model):
    #проблема
    title = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    # серьезность 
    serios = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    #статус 
    status = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    #коментарий 
    koment = models.TextField(
        blank=True,
        null=True,
    )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )
    projects = models.ForeignKey(
        Projects,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    objects = models.Manager()
    
    def __str__(self):
        return self.title

class Zadachirp(models.Model):
    # имя исполнителя зададчи 
    title = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    # статус задаи (выполенно не выполенно если да то убирается в старое )
    statshard = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    # дата задачи 
    data = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    # задача 
    zadatha = models.TextField(
        blank=True,
        null=True,
    )
    # результат 
    rezultate = models.TextField(
        blank=True,
        null=True,
    )
    # статус задачит 
    statuszad = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )
    projects = models.ForeignKey(
        Projects,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    objects = models.Manager()
    

    def __str__(self):
        return self.title

class Komanda(models.Model):
    # фио 
    title = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    # должность 
    prof = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )
    # мейл
    mail = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    objects = models.Manager()

    projects = models.ForeignKey(
        Projects,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    def __str__(self):
        return self.title

class Itap(models.Model):
    # этап №
    title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    # Название этапа
    itapnaim= models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )
    # Коментарий РП
    komentrp = models.TextField(
        blank=True,
        null=True,
    )
    # Коментарий  старый РП
    oldkomentrp = models.TextField(
        blank=True,
        null=True,
    )
    # Коментарий Степановой 
    komentstep = models.TextField(
        blank=True,
        null=True,
    )
    #  Акт 
    act = models.CharField(
        max_length=100, 
        blank=True,
        null=True,
        )
    # Оплата
    oplata = models.CharField(
        max_length=100, 
        blank=True,
        null=True,
        )
    
    # Задолжность 
    zadolkjnost = models.TextField(
        blank=True,
        null=True,
    )
    # авагс 
    avanse = models.CharField(
        max_length=100, 
        blank=True,
        null=True,
    )
    # оплата 
    oplataok = models.CharField(
        max_length=100, 
        blank=True,
        null=True,
    )
    #  общая стоимость 
    obshaystoimost = models.CharField(
        max_length=100, 
        blank=True,
        null=True,
    )
    # дата начала
    datastart = models.DateField(
        blank=True,
        null=True,
    )
    # дата конца 
    datastop = models.DateField(
        blank=True,
        null=True,
    )
    # плановая дата начала
    plandatastart = models.DateField(
        blank=True,
        null=True,
    )
    # плановая дата конца 
    plandatastop = models.DateField(
        blank=True,
        null=True,
    )

    projects = models.ForeignKey(
        Projects,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
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
        return f" {self.title }  {self.projects}"

class HistoriOfTheOtchet(models.Model):
    title = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    oldkomentrp = models.TextField(
        blank=True,
        null=True,
    )
    projects = models.ForeignKey(
        Projects,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
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


class Zadania(models.Model):
    #  наименование документа 
    title = models.CharField(
        max_length=500,
        blank=True,
        null=True,
    )

    # 
    prozes = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    rezult = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    documentrez = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    vexa = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    otvetst = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    # уровень 
    level = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    # статуст
    status = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    # дата 
    data = models.DateField(
        blank=True,
        null=True,
    )

    dataend = models.DateField(
        blank=True,
        null=True,
    )

    itap = models.ForeignKey(
        Itap,
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

class Documents(models.Model):
    title = models.CharField(
        max_length=500,
        blank=True,
        null=True,
    )

    # 
    status = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    
    documentrez = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    # уровень 
    level = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    
    data = models.DateField(
        blank=True,
        null=True,
    )

    itap = models.ForeignKey(
        Itap,
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

class Mani(models.Model):
    # общая стоимотсь 
    title = models.CharField(
        max_length=500,
        blank=True,
        null=True,
    )
    # Аванс
    avanse = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    # статсус
    status = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    # дней на оплату
    dneyleft = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    # ожидаем оплату 
    data = models.DateField(
        blank=True,
        null=True,
    )

    itap = models.ForeignKey(
        Itap,
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

        