#from django.urls import url, include
from django.conf.urls import include, url
from rest_framework import routers
from . import views
#from .views import MemberView

router = routers.DefaultRouter()

router.register(r'itineraries', views.ItineraryViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'gatherings', views.GatheringViewSet)

router.register(r'members', views.MemberViewSet)
router.register(r'groups', views.GroupViewSet)

router.register(r'conflicts', views.GatheringViewSet)
router.register(r'food-restrictions', views.FoodRestrictionViewSet)
router.register(r'diets', views.DietViewSet)

router.register(r'availabilities', views.AvailabilityViewSet)
router.register(r'attendances', views.AttendanceViewSet)

router.register(r'email-template', views.EmailTemplateViewSet)
router.register(r'email-log', views.EmailLogViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
