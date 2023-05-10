from django.shortcuts import render
from django.views.generic import ListView

from app_orm_trainer.models import Product, Laptop, PC, Printer


class Solution(ListView):
    model = Product
    template_name = 'app_orm_trainer/index.html'
    context_object_name = 'solution'

        #Solution 1
    def get_queryset(self):
        # queryset = super().get_queryset()
        queryset = Laptop.objects.all()
        # queryset = queryset.filter(type='Printer')
        return queryset
