from rest_framework import serializers
#from .models import Itinerary, Event, Group, Member, Conflict, FoodRestriction, Diet, Gathering, Availability, Attendance, EmailTemplate, EmailLog
from . import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class ItinerarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Itinerary
        fields = ['url','name','description','start_date','end_date','default_gathering_size']
        extra_kwargs = {
            'name':{'required':True},
            'start_date':{'required':True},
            'end_date':{'required':True},
        }

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Event
        fields = ['url','itinerary','name','description','start_date','end_date','cancelled_date','cancelled_reason']
        extra_kwargs = {
            'itinerary':{'required':True},
            'name':{'required':True},
            'start_date':{'required':True},
        }

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Group
        fields = ['url','name','is_active']
        extra_kwargs = {
            'name':{'required':True},
        }

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Member
        fields = ['url','preferred_name','first_name','middle_name','last_name','pronouns','email','phone','street_address','zip_code','host_note','attendee_note','is_active']
        extra_kwargs = {
            'preferred_name':{'required':True},
        }

class ConflictSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Conflict
        fields = ['url','conflicted_a','conflicted_b']
        extra_kwargs = {
            'conflicted_a':{'required':True},
            'conflicted_b':{'required':True},
        }

class FoodRestrictionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.FoodRestriction
        fields = ['url','member','restriction']
        extra_kwargs = {
            'member':{'required':True},
            'restriction':{'required':True},
        }

class DietSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Diet
        fields = ['url','member','diet']
        extra_kwargs = {
            'member':{'required':True},
            'diet':{'required':True},
        }

class GatheringSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Gathering
        fields = ['url','event','host_group','host_member','cancelled_date','cancelled_reason']
        extra_kwargs = {
            'event':{'required':True},
            'host_group':{'required':True},
        }

class AvailabilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Availability
        fields = ['url','group','event','can_attend','can_host']
        extra_kwargs = {
            'event':{'required':True},
            'group':{'required':True},
        }

class AttendanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Attendance
        fields = ['url','group','gathering','attendance_type']
        extra_kwargs = {
            'gathering':{'required':True},
            'group':{'required':True},
        }

class EmailTemplateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.EmailTemplate
        fields = ['url','name','description','subject','body']
        extra_kwargs = {
            'name':{'required':True},
            'subject':{'required':True},
            'body':{'required':True},
        }

class EmailLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.EmailLog
        fields = ['url','template','to_addresses','from_addresses','cc_addresses']
        extra_kwargs = {
            'to_addresses':{'required':True},
            'from_addresses':{'required':True},
        }

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','password']
        extra_kwargs = {
            'password':{'required':True, 'write_only':True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

