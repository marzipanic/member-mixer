from django.shortcuts import render
# from .serializers import ItinerarySerializer, EventSerializer, GroupSerializer, MemberSerializer, Confl
# from .models import Itinerary, Event, Group, Member, Conflict
from . import serializers
from . import models
from rest_framework import viewsets

# Create your views here.
class ItineraryViewSet(viewsets.ModelViewSet):
    queryset = models.Itinerary.objects.all()
    serializer_class = serializers.ItinerarySerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializer

class ConflictViewSet(viewsets.ModelViewSet):
    queryset = models.Conflict.objects.all()
    serializer_class = serializers.ConflictSerializer

class FoodRestrictionViewSet(viewsets.ModelViewSet):
    queryset = models.FoodRestriction.objects.all()
    serializer_class = serializers.FoodRestrictionSerializer

class DietViewSet(viewsets.ModelViewSet):
    queryset = models.Diet.objects.all()
    serializer_class = serializers.DietSerializer

class GatheringViewSet(viewsets.ModelViewSet):
    queryset = models.Gathering.objects.all()
    serializer_class = serializers.GatheringSerializer

class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = models.Availability.objects.all()
    serializer_class = serializers.AvailabilitySerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = models.Attendance.objects.all()
    serializer_class = serializers.AttendanceSerializer

class EmailTemplateViewSet(viewsets.ModelViewSet):
    queryset = models.EmailTemplate.objects.all()
    serializer_class = serializers.EmailTemplateSerializer

class EmailLogViewSet(viewsets.ModelViewSet):
    queryset = models.EmailLog.objects.all()
    serializer_class = serializers.EmailLogSerializer

