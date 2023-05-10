from rest_framework import serializers
from Api.models import BooksApiModel


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksApiModel
        fields = '__all__'
