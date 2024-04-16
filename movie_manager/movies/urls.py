from django.urls import path
from . import views

urlpatterns=[
    path('create/',views.create,name='create'),
    path('list/<pk>', views.list, name='list'),
    path('delete/<pk>', views.delete, name='delete'),
    path('edit/<pk>', views.edit, name='edit'),
    path('', views.list, name='list'),
]
