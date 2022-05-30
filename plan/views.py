# from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer,PartnerSerializer,PlansSerializer,PromotionSerializer,CustomerGoalsSerializer
from .models import Partner, Plans, Promotion,CustomerGoals
from rest_framework import status
import json
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



# APIS

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])  
def welcome(request):
    content = {"message": "Welcome to the torotise!"}
    return JsonResponse(content)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['username', 'email']
    ordering_fields = ['username', 'email']
    search_fields =['username', 'email']

class PartnerViewSet(viewsets.ModelViewSet):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['name', 'email','created_by']
    ordering_fields = ['name', 'email','created_by']
    search_fields =['name', 'email','created_by']

class PlansViewSet(viewsets.ModelViewSet):
    serializer_class = PlansSerializer
    queryset = Plans.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['plan_name', 'amount_options','tenure_options','benefit_percentage','benefit_type']
    ordering_fields = ['plan_name', 'amount_options','tenure_options','benefit_percentage','benefit_type']
    search_fields =['plan_name', 'amount_options','tenure_options','benefit_percentage','benefit_type']

class PromotionViewSet(viewsets.ModelViewSet):
    serializer_class = PromotionSerializer
    queryset = Promotion.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['no_of_user', 'benefit_percentage']
    ordering_fields = ['no_of_user', 'benefit_percentage']
    search_fields =['no_of_user', 'benefit_percentage']

class CustomerGoalsViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerGoalsSerializer
    queryset = CustomerGoals.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['selected_amount', 'deposited_amount','benefit_percentage','benefit_type']
    ordering_fields = ['selected_amount', 'deposited_amount','benefit_percentage','benefit_type']
    search_fields =['selected_amount', 'deposited_amount','benefit_percentage','benefit_type']