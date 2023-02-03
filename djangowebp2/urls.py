from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/', views.about, name='about'),
    path('info/', views.info, name='info'),
    path('services/', views.services, name='services'),
    path('contact', views.contact, name='contact'),
]