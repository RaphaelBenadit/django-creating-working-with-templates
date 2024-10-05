from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.odd_even_checker, name='odd_even_checker'),
    path('filter/', views.name_filter, name='name_filter'),
]