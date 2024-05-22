from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_contact, name='add_contact'),
    path('', views.list_contacts, name='list_contacts'),
    path('<int:contact_id>/', views.contact_details, name='contact_details'),
]
