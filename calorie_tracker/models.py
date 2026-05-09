from django.db import models
from django.utils import timezone


class FoodItem(models.Model):
    """
    Represents a single food item added by the user.
    Each food item has a name and its calorie count.
    """
    name = models.CharField(max_length=200)       # the food name e.g "Banana"
    calories = models.PositiveIntegerField()       # must be a positive number
    date_added = models.DateField(default=timezone.now)  # defaults to today

    def __str__(self):
        """What shows in Django admin and shell when you print this object"""
        return f"{self.name} - {self.calories} kcal"

    class Meta:
        ordering = ['-date_added']  # newest items show first