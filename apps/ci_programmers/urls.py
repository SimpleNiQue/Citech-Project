from django.urls import path
from . import views


app_name = 'ci_programmers'
urlpatterns = [
   path('', views.index, name='home'), 
]