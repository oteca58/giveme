from django.shortcuts import get_object_or_404
from rest_framework import generics, status, viewsets, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny

#import django_filters

from core.api.serializers import ActivitiesSerializer

from core.models import Activities
from django_filters.rest_framework import DjangoFilterBackend

class ActivitiesListApiView(generics.ListAPIView):
    search_fields = ['description','client_code','due_date','assignment','status','billable_to','invoiced']
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = {'due_date':('gte','gt','lt','lte')}
    #all().order_by("due_date")
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer
    permission_classes = [AllowAny]

class ActivityCreateAPIView(generics.CreateAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer
    permission_classes = [AllowAny]

    #def perform_create(self, serializer):
    #    serializer.save()
    
class ActivityRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer
    permission_classes = [IsAuthenticated]

        
