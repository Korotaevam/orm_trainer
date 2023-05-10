from django.contrib import admin

from app_orm_trainer.models import Product, Laptop, PC, Printer


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('maker', 'model', 'type')


class LaptopAdmin(admin.ModelAdmin):
    list_display = ('code', 'model', 'speed', 'ram', 'hd', 'price', 'screen')


class PCAdmin(admin.ModelAdmin):
    list_display = ('code', 'model', 'speed', 'ram', 'hd', 'price', 'cd')


class PrinterAdmin(admin.ModelAdmin):
    list_display = ('code', 'model', 'color', 'type', 'price')


admin.site.register(Product)
admin.site.register(Laptop)
admin.site.register(PC)
admin.site.register(Printer)
