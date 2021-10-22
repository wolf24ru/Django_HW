from django.urls import path
from .views import home, current_item, workdir

# app_name = 'app'
urlpatterns = [
    path('', home, name='home'),
    path('current_item/', current_item, name='current'),
    path('workdir/', workdir, name='workdir'),
    ]
