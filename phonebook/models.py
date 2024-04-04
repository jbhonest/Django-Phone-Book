from django.db import models
from django.conf import settings


class Contact(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    photo = models.ImageField(
        upload_to='contact_photos/', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT)

    def delete(self):
        # Delete the image file from the storage
        if self.photo:
            storage, path = self.photo.storage, self.photo.path
            storage.delete(path)

        # Call the parent class's delete method to remove the model instance from the database
        super().delete()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class MembershipPlan(models.Model):
    name = models.CharField(max_length=100)
    contact_limit = models.IntegerField()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    membership_plan = models.ForeignKey(
        MembershipPlan, on_delete=models.CASCADE)
    contacts_created = models.IntegerField(default=0)
