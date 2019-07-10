from django.urls import path

from . import views

urlpatterns = [
    # ex: /personal/
    path('', views.index, name='index'),

    # for contact page http://127.0.0.1:8000/contact/
    path('contact/', views.contact, name='contact'),
]