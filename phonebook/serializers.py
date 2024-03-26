from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name',
                  'phone_number', 'address', 'user')

    def get_fields(self):
        fields = super().get_fields()
        if 'user' in fields:
            # Hide user field in the browsable API
            fields['user'].read_only = True
        return fields
