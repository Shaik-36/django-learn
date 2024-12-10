from django.contrib import admin
from django.urls import path
from . import views


# localhost:8000/chai
# localhost:8000/chai/order
urlpatterns = [
    path('', views.all_chai, name='all_chai'),
    path('<int:chai_id>/', views.chai_details, name='chai_details'),
    path('order/', views.order, name='order'),
]

