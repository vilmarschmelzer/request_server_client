from rest_framework import serializers
from requestapp.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category