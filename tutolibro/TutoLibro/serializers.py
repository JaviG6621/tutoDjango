from .models import Developer
from rest_framework import serializers

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ("nick", "email", "first_name", "last_name", "programming_language")