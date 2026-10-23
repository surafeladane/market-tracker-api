from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from rest_framework import serializers
from .models import Crop, Market, PriceEntry

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'

class PriceEntrySerializer(serializers.ModelSerializer):
    submitted_by_name = serializers.CharField(source='submitted_by.username', read_only=True)

    class Meta:
        model = PriceEntry
        fields = '__all__'
        read_only_fields = ['submitted_by']

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )