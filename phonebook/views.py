from django.shortcuts import render, redirect
from django_filters.rest_framework import DjangoFilterBackend
from django.db import models
from rest_framework import viewsets, filters, permissions
from .serializers import ContactSerializer
from .models import Contact
from .forms import ContactForm


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Contact.objects.order_by('-pk')
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    search_fields = ('first_name', 'last_name', 'phone_number', 'address')

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user.id).order_by('-pk')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


def contact_list(request):
    contacts = Contact.objects.filter(user=request.user.id).order_by('-pk')
    return render(request, 'phonebook/contact_list.html', {'contacts': contacts})


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()

    return render(request, 'phonebook/add_contact.html', {'form': form})


def update_contact(request, contact_id):
    try:
        contact = Contact.objects.get(id=contact_id)
    except Contact.DoesNotExist:
        return redirect('contact_list')

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)

    return render(request, 'phonebook/update_contact.html', {'form': form, 'contact': contact})


def delete_contact(request, contact_id):
    try:
        contact = Contact.objects.get(id=contact_id)
        contact.delete()
    except Contact.DoesNotExist:
        pass

    return redirect('contact_list')


def search_contact(request):
    if 'q' in request.GET:
        search_query = request.GET['q']
        contacts = Contact.objects.filter(
            models.Q(first_name__icontains=search_query) |
            models.Q(last_name__icontains=search_query) |
            models.Q(phone_number__icontains=search_query) |
            models.Q(address__icontains=search_query)
        )
    else:
        contacts = []

    return render(request, 'phonebook/search_contact.html', {'contacts': contacts})
