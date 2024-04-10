from django.http import HttpResponseBadRequest
from rest_framework import viewsets, filters, permissions
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.urls import reverse
from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db import models
from rest_framework import viewsets, filters, permissions
from .serializers import ContactSerializer
from .models import Contact, UserProfile


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
        try:
            user_profile = UserProfile.objects.get(user=self.request.user)
            if user_profile.contacts_created < user_profile.membership_plan.contact_limit or user_profile.membership_plan.contact_limit == -1:
                user_profile.contacts_created += 1
                user_profile.save()
                serializer.save(user=self.request.user)
        # except KeyError:
        #     return Response({'error': 'Contact limit exceeded!'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


@method_decorator(login_required, name="dispatch")
class ContactListView(ListView):
    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user.id).order_by('-id')


@method_decorator(login_required, name="dispatch")
class ContactCreateView(CreateView):
    model = Contact
    template_name_suffix = '_create_form'
    fields = ['first_name', 'last_name', 'phone_number', 'address', 'photo']

    def form_valid(self, form):
        user_profile = UserProfile.objects.get(user=self.request.user)
        if user_profile.contacts_created >= user_profile.membership_plan.contact_limit and user_profile.membership_plan.contact_limit != -1:
            return HttpResponseBadRequest("<h3>Contact limit exceeded!</h3>")

        user_profile.contacts_created += 1
        user_profile.save()
        # Continue with contact creation

        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contact_list')


@method_decorator(login_required, name="dispatch")
class ContactUpdateView(UpdateView):
    template_name_suffix = '_update_form'
    fields = ['first_name', 'last_name', 'phone_number', 'address', 'photo']

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user.id)

    def get_success_url(self):
        return reverse('contact_list')


@method_decorator(login_required, name="dispatch")
class ContactDeleteView(DeleteView):
    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user.id)

    def form_valid(self, form):
        user_profile = UserProfile.objects.get(user=self.request.user)
        user_profile.contacts_created -= 1
        user_profile.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contact_list')


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
