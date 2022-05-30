from rest_framework import serializers
from .models import Partner, Plans, Promotion,CustomerGoals
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PartnerSerializer(serializers.ModelSerializer):
    created_by  = serializers.CharField(read_only=True)
    updated_by = serializers.CharField(read_only=True)
    class Meta:
        model = Partner
        fields = '__all__'

class PlansSerializer(serializers.ModelSerializer):
    created_by  = serializers.CharField(read_only=True)
    updated_by = serializers.CharField(read_only=True)
    class Meta:
        model = Plans
        fields = '__all__'

class PromotionSerializer(serializers.ModelSerializer):
    created_by  = serializers.CharField(read_only=True)
    updated_by = serializers.CharField(read_only=True)
    class Meta:
        model = Promotion
        fields = '__all__'

class CustomerGoalsSerializer(serializers.ModelSerializer):
    created_by  = serializers.CharField(read_only=True)
    updated_by = serializers.CharField(read_only=True)
    class Meta:
        model = CustomerGoals
        fields = '__all__'
