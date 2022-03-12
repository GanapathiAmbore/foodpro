from django.contrib import admin
from foodapp.models import Category, FoodItem

models = [Category, FoodItem]
admin.site.register(models)
# Register your models here.
