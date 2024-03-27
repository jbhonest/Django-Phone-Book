from django.urls import path, include
from rest_framework import routers
from .views import ContactViewSet
from . import views

contact_router = routers.DefaultRouter()
contact_router.register('', ContactViewSet)

urlpatterns = [
    path('', views.ContactListView.as_view(), name='contact_list'),
    path('add/', views.ContactCreateView.as_view(), name='add_contact'),
    path('update/<int:pk>/',
         views.ContactUpdateView.as_view(), name='update_contact'),
    path('delete/<int:pk>/',
         views.ContactDeleteView.as_view(), name='delete_contact'),
    path('search/', views.search_contact, name='search_contact'),
    path('contacts/', include(contact_router.urls)),
]
