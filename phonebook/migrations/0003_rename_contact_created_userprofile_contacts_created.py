# Generated by Django 4.2 on 2024-04-04 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0002_membershipplan_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='contact_created',
            new_name='contacts_created',
        ),
    ]
