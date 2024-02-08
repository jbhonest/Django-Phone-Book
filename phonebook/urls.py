from django.urls import path, include
from rest_framework import routers
from .views import ContactViewSet
from . import views

contact_router = routers.DefaultRouter()
contact_router.register('', ContactViewSet)

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('add/', views.add_contact, name='add_contact'),
    path('update/<int:contact_id>/',
         views.update_contact, name='update_contact'),
    path('delete/<int:contact_id>/',
         views.delete_contact, name='delete_contact'),
    path('search/', views.search_contact, name='search_contact'),
    path('contacts/', include(contact_router.urls)),
]
