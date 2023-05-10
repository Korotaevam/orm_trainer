from django.shortcuts import render
from django.views.generic import ListView
from app_orm_trainer.models import Product, Laptop, PC, Printer
from django.db.models import Q, Max, Avg, Func, Count, Min, Sum
import logging


# logger = logging.getLogger(__name__)


class Solution(ListView):
    model = Product
    template_name = 'app_orm_trainer/index.html'
    context_object_name = 'solution'

    # Solution 1 Найдите номер модели, скорость и размер жесткого диска для всех ПК стоимостью менее 500 дол. Вывести: model, speed и hd
    # def get_queryset(self):
    #     queryset = PC.objects.filter(price__lte=500)
    #     return queryset

    # Solution 2 Найдите производителей принтеров. Вывести: maker
    # def get_queryset(self):
    #     queryset = Product.objects.filter(type='Printer').values('maker').distinct()
    #     return queryset

    # Solution 3 Найдите номер модели, объем памяти и размеры экранов ПК-блокнотов, цена которых превышает 1000 дол
    # def get_queryset(self):
    #     queryset = Laptop.objects.filter(price__gt=1000).order_by('model')
    #     return queryset

    # Solution 4 Найдите все записи таблицы Printer для цветных принтеров.
    # def get_queryset(self):
    #     queryset = Printer.objects.filter(color__contains='y').order_by('-code')
    #     return queryset

    # Solution 5 Найдите номер модели, скорость и размер жесткого диска ПК, имеющих 12x или 24x CD и цену менее 600 дол.
    # def get_queryset(self):
    # queryset = PC.objects.filter(cd__in=['12x', '24x']).filter(price__lt=600).order_by('hd', 'model')
    # return queryset

    # Solution 6 Для каждого производителя, выпускающего ПК-блокноты c объёмом жесткого диска не менее 10 Гбайт, найти скорости таких ПК-блокнотов. Вывод: производитель, скорость.
    # def get_queryset(self):
    #     queryset = Laptop.objects.filter(hd__gte=10).order_by('model__maker', 'speed')
    #     return queryset

    # Solution 7 Найдите номера моделей и цены всех имеющихся в продаже продуктов (любого типа) производителя B (латинская буква).
    # def get_queryset(self):
    #     pc = PC.objects.all().select_related('model__maker').values('model', 'price', 'model__maker').filter(model__maker='B')
    #     lap = Laptop.objects.all().select_related('model__maker').values('model', 'price', 'model__maker').filter(model__maker='B')
    #     prin = Printer.objects.all().select_related('model__maker').values('model', 'price', 'model__maker').filter(model__maker='B')
    #     queryset = prin.union(lap, pc)
    #     return queryset

    # Solution 8  Найдите производителя, выпускающего ПК, но не ПК-блокноты
    # def get_queryset(self):
    #     pp = Product.objects.filter(type='Laptop').values('maker')
    #     queryset = Product.objects.filter(type='PC').exclude(maker__in=[i['maker'] for i in pp]).values('maker').distinct()
    #     return queryset

    # Solution 9  Найдите производителей ПК с процессором не менее 450 Мгц. Вывести: Maker
    # def get_queryset(self):
    #     queryset = PC.objects.filter(speed__gte=450).values('model__maker').distinct()
    #     return queryset

    # Solution 10  Найдите модели принтеров, имеющих самую высокую цену. Вывести: model, price
    # def get_queryset(self):
    #     max_price = Printer.objects.aggregate(Max('price'))
    #     queryset = Printer.objects.filter(price__gte=max_price['price__max'])
    #     return queryset

    # Solution 11  Найдите среднюю скорость ПК.
    # def get_queryset(self):
    #     queryset = PC.objects.aggregate(Avg('speed'))
    #     return queryset

    # Solution 12  Найдите среднюю скорость ПК-блокнотов, цена которых превышает 1000 дол.
    # def get_queryset(self):
    #     queryset = Laptop.objects.filter(price__gte=1000).aggregate(Avg('speed'))
    #     return queryset

    # Solution 13  Найдите среднюю скорость ПК, выпущенных производителем A.
    # def get_queryset(self):
    #     queryset = PC.objects.filter(model__maker='A').aggregate(Avg('speed'))
    #     return queryset

    # Solution 15  Найдите размеры жестких дисков, совпадающих у двух и более PC. Вывести: HD
    # def get_queryset(self):
    #     queryset = PC.objects.values('hd').annotate(Count('hd')).filter(hd__count__gte=2)
    #     return queryset

    # Solution 16  Найдите пары моделей PC, имеющих одинаковые скорость и RAM. В результате каждая пара указывается только один раз, т.е. (i,j), но не (j,i), Порядок вывода: модель с большим номером, модель с меньшим номером, скорость и RAM
    # def get_queryset(self):
        # сырой запрос
        # queryset = PC.objects.raw(
        #     'SELECT DISTINCT pc_1.code, pc_1.model_id as model1, pc_2.model_id as model2, pc_1.speed, pc_1.ram '
        #     'FROM app_orm_trainer_pc as pc_1, app_orm_trainer_pc as pc_2 '
        #     'WHERE pc_1.speed = pc_2.speed AND pc_1.ram = pc_2.ram AND pc_1.model_id > pc_2.model_id '
        #     'ORDER BY pc_1.speed DESC'
        #     )
        # queryset_1 = PC.objects.values('speed', 'ram', 'model')
        # queryset_2 = PC.objects.values('speed', 'ram', 'model')
        # d = dict()
        # queryset = []
        # for i in queryset_1:
        #     for j in queryset_2:
        #         if i['speed'] == j['speed'] and i['ram'] == j['ram'] and i['model'] > j['model']:
        #             d['model1'] = i['model']
        #             d['model2'] = j['model']
        #             d['speed'] = i['speed']
        #             d['ram'] = i['ram']
        #             queryset.append(d)
        #             d = dict()
        # queryset = sorted(queryset, key=lambda x: x['model2'])
        # print(queryset)
        #
        # return queryset

    # Solution 17  Найдите модели ПК-блокнотов, скорость которых меньше скорости каждого из ПК. Вывести: type, model, speed
    # def get_queryset(self):
    #     queryset = Laptop.objects.filter(speed__lt=PC.objects.aggregate(Min('speed'))['speed__min'])
    #     return queryset

    # Solution 18  Найдите производителей самых дешевых цветных принтеров. Вывести: maker, price
    # def get_queryset(self):
    #     min_price = Printer.objects.filter(color='y').aggregate(min_price=Min('price'))['min_price']
    #     queryset = Printer.objects.filter(price__lte=min_price, color='y')
    #     return queryset


    # Solution 19  Для каждого производителя, имеющего модели в таблице Laptop, найдите средний размер экрана выпускаемых им ПК-блокнотов.
    # Вывести: maker, средний размер экрана.
    # def get_queryset(self):
    #     queryset = Laptop.objects.values('model__maker').annotate(Avg('screen'))
    #     return queryset


    # Solution 20  Найдите производителей, выпускающих по меньшей мере три различных модели ПК. Вывести: Maker, число моделей ПК.
    # def get_queryset(self):
    #     queryset = Product.objects.filter(type='PC').values('maker').annotate(Count('maker')).filter(maker__count__gte=3)
    #     return queryset


    # Solution 21  Найдите максимальную цену ПК, выпускаемых каждым производителем, у которого есть модели в таблице PC.
    # Вывести: maker, максимальная цена
    # def get_queryset(self):
    #     queryset = PC.objects.values('model__maker').annotate(Max('price'))
    #     return queryset


    # Solution 22 Для каждого значения скорости ПК, превышающего 600 МГц, определите среднюю цену ПК с такой же скоростью. Вывести: speed, средняя цена
    # def get_queryset(self):
    #     queryset = PC.objects.filter(speed__gt=600).values('speed').annotate(Avg('price'))
    #     return queryset


    # Solution 23 Найдите производителей, которые производили бы как ПК
    # со скоростью не менее 750 МГц, так и ПК-блокноты со скоростью не менее 750 МГц.
    # Вывести: Maker
    # def get_queryset(self):
    #     queryset = Product.objects.filter(Q(pc__speed__gte=750) | Q(laptop__speed__gte=750)).values('maker').distinct().order_by('maker')
    #     return queryset



    # Solution 24 Перечислите номера моделей любых типов, имеющих самую высокую цену по всей имеющейся в базе данных продукции.
    # def get_queryset(self):
    #     max_pc_price = PC.objects.aggregate(max_pc_price=Max('price'))['max_pc_price']
    #     max_laptop_price = Laptop.objects.aggregate(max_laptop_price=Max('price'))['max_laptop_price']
    #     max_printer_price = Printer.objects.aggregate(max_printer_price=Max('price'))['max_printer_price']
    #     max_price = max(max_pc_price, max_laptop_price, max_printer_price)
    #     queryset = Product.objects.filter(Q(pc__price__gte=max_price) | Q(laptop__price__gte=max_price) | Q(printer__price__gte=max_price))
    #     return queryset


        # Solution 25 Найдите производителей принтеров, которые производят ПК с наименьшим объемом RAM и с самым быстрым процессором среди всех ПК, имеющих наименьший объем RAM. Вывести: Maker
    # def get_queryset(self):
    #     printer_maker = Product.objects.filter(type='Printer').values('maker').distinct()
    #     low_ram = PC.objects.aggregate(low_ram=Min('ram'))['low_ram']
    #     max_speed = PC.objects.filter(ram=low_ram).aggregate(max_speed=Max('speed'))['max_speed']
    #     queryset = PC.objects.filter(ram=low_ram).filter(model__maker__in=[i['maker'] for i in printer_maker], speed=max_speed)
    #     return queryset

        # Solution 26 Найдите среднюю цену ПК и ПК-блокнотов, выпущенных производителем A (латинская буква). Вывести: одна общая средняя цена.
    # def get_queryset(self):
    #     queryset = Product.objects.filter(maker='A').filter(type__in=['PC', 'Laptop'])\
    #         .aggregate(avg_price=(Sum('pc__price')+Sum('laptop__price'))/(Count('pc__price')+Count('laptop__price')))
    #     print(queryset)
    #     return queryset

        # Solution 27 Найдите средний размер диска ПК каждого из тех производителей, которые выпускают и принтеры. Вывести: maker, средний размер HD.
    # def get_queryset(self):
    #     printer_maker = Product.objects.filter(type='Printer').values('maker').distinct()
    #     queryset = PC.objects.filter(model__maker__in=[i['maker'] for i in printer_maker])\
    #         .values('model__maker').annotate(Avg('hd'))
    #     return queryset


        # Solution 28 Используя таблицу Product, определить количество производителей, выпускающих по одной модели.
    # def get_queryset(self):
    #     queryset = Product.objects.values('maker').annotate(Count('maker')).filter(maker__count__lt=2)
    #     return queryset


        # Solution 35 В таблице Product найти модели, которые состоят только из цифр или только из латинских букв (A-Z, без учета регистра).
    # Вывод: номер модели, тип модели.
    # def get_queryset(self):
    #     queryset = Product.objects.filter(~Q(model__contains='[^0-9]') | ~Q(model__contains='[^A-Z]')).order_by('model')
    #     return queryset

        # Solution 40 Найти производителей, которые выпускают более одной модели, при этом все выпускаемые производителем модели являются продуктами одного типа.
    # Вывести: maker, type
    # def get_queryset(self):
    #     one_type = Product.objects.values('maker').annotate(Count('type', distinct=True)).filter(type__count__lte=1)
    #     queryset = Product.objects.filter(maker__in=[i['maker'] for i in one_type]).values('maker', 'type').annotate(Count('type')).filter(type__count__gt=1)
    #     return queryset


        # Solution 41 Для каждого производителя, у которого присутствуют модели хотя бы в одной из таблиц PC, Laptop или Printer,
    # определить максимальную цену на его продукцию.
    # Вывод: имя производителя, если среди цен на продукцию данного производителя присутствует NULL, то выводить для этого производителя NULL,
    # иначе максимальную цену.
    # def get_queryset(self):
    #     queryset1 = Product.objects.values_list('maker').annotate(Max('pc__price', default=0))\
    #         .annotate(Max('laptop__price', default=0)).annotate(Max('printer__price', default=0))
    #     queryset = [{'maker': i[0], 'price': max(i[1:])} for i in queryset1]
    #     return queryset




