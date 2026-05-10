from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import FoodItem


def index(request):
    """
    Main page — shows today's food items and total calories.
    Also handles adding a new food item via POST request.
    """
    today = timezone.now().date()
    food_items = FoodItem.objects.filter(date_added=today)  # only today's items
    total_calories = sum(item.calories for item in food_items)  # add them all up

    if request.method == 'POST':
        name = request.POST.get('name')
        calories = request.POST.get('calories')

        if name and calories:
            FoodItem.objects.create(name=name, calories=int(calories), date_added=today)
        return redirect('index')  # refresh the page after adding

    return render(request, 'calorie_tracker/index.html', {
        'food_items': food_items,
        'total_calories': total_calories,
        'today': today,
    })


def delete_item(request, item_id):
    """Remove a specific food item by its ID"""
    item = get_object_or_404(FoodItem, id=item_id)
    item.delete()
    return redirect('index')


def reset(request):
    """Delete all food items for today"""
    today = timezone.now().date()
    FoodItem.objects.filter(date_added=today).delete()
    return redirect('index')