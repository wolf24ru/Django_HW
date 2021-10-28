from django.urls import path
from .views import dishes, home

app_name = 'calculator'
urlpatterns = [
    path('', home, name='home'),
    path('<str:dish>', dishes, name='dishes'),
]
