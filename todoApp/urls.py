from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='home'),
     path('about/',views.about,name='about'),
     path('contact/',views.contact,name='contact'),
     path('delete/<itemID>',views.delete,name='delete'),
     path('changeCross/<itemID>',views.changeCross,name='changeCross')
]
