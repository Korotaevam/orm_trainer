from django.db import models


class Product(models.Model):
    maker = models.CharField(max_length=10, verbose_name='Производитель')
    model = models.CharField(primary_key=True, max_length=50, verbose_name='Модель')
    type = models.CharField(max_length=50, verbose_name='Тип')

    def __str__(self):
        return f'{self.maker} {self.model} {self.type}'


class Laptop(models.Model):
    code = models.IntegerField(primary_key=True, verbose_name='Код')
    model = models.ForeignKey(Product, on_delete=models.PROTECT, max_length=50, verbose_name='Модель')
    speed = models.SmallIntegerField(verbose_name='Скорость')
    ram = models.SmallIntegerField(verbose_name='Память')
    hd = models.SmallIntegerField(verbose_name='Жесткий')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.0, verbose_name='Цена')
    screen = models.SmallIntegerField(verbose_name='Экран')

    def __str__(self):
        return f'{self.code} {self.model} {self.speed} {self.ram} {self.hd} {self.price} {self.screen}'


class PC(models.Model):
    code = models.IntegerField(primary_key=True, verbose_name='Код')
    model = models.ForeignKey(Product, on_delete=models.PROTECT, max_length=50, verbose_name='Модель')
    speed = models.SmallIntegerField(verbose_name='Скорость')
    ram = models.SmallIntegerField(verbose_name='Память')
    hd = models.SmallIntegerField(verbose_name='Жесткий')
    cd = models.CharField(max_length=10, verbose_name='привод')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.0, verbose_name='Цена')

    def __str__(self):
        return f'{self.code} {self.model} {self.speed} {self.ram} {self.hd} {self.cd} {self.price}'


class Printer(models.Model):
    code = models.IntegerField(primary_key=True, verbose_name='Код')
    model = models.ForeignKey(Product, on_delete=models.PROTECT, max_length=50, verbose_name='Модель')
    color = models.CharField(max_length=1, verbose_name='Цвет')
    type = models.CharField(max_length=10, verbose_name='Тип')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.0, verbose_name='Цена')

    def __str__(self):
        return f'{self.code} {self.model} {self.color} {self.type} {self.price}'
