
from django.urls import path
from app_orm_trainer.views import Solution

urlpatterns = [
    path('', Solution.as_view(), name='solution'),
]