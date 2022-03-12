from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    price = models.FloatField()
    comments = models.TextField()

    def __str__(self):
        return self.name