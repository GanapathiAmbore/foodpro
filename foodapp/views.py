from django.shortcuts import render
from foodapp.models import FoodItem


def home(request):
    items = FoodItem.objects.all()
    return render(request, 'base.html', {'items':items})

