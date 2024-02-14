from django.urls import path
from .views import phonebook,add_contact, edit_contact, delete_contact , search_view

urlpatterns = [
    path('', phonebook, name='phonebook'),
    path('add/', add_contact, name='add_contact'),
    path('edit/<int:pk>/', edit_contact, name='edit_contact'),
    path('search/', search_view, name='search_view'),
    path('delete_contact/<int:pk>/', delete_contact, name='delete_contact')
    
]


