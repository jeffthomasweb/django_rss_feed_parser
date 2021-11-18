from django.urls import path

from . import views

urlpatterns = [
    path('mysite/', views.index, name='index'),
    path('news/', views.news),
]
