from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                        # home page
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),  # delete one item
    path('reset/', views.reset, name='reset'),                  # reset today
]