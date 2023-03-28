from django.urls import path

from web import views

urlpatterns = [
    path('', views.django, name='index'),
]
