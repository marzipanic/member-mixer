from django.db import models
from django.contrib.auth.models import User

# TODO
#   Stubs for deleting members.
"""
def get_deleted_group():
    from models import Group
    from django.conf import settings
    deleted_group, created = Group.objects.get_or_create(
        name = 'DEFAULT_GROUP',
    )
    return deleted_group

def get_deleted_member():
    return get_deleted_member().objects.get_or_create(
        preferred_name = 'DEFAULT_MEMBER'
    )[0]
    """

# Consider adding a SoftDeleteModel to the BaseModel
# https://blog.usebutton.com/cascading-soft-deletion-in-django
# class BaseModel(models.Model):
#     created_date = models.DateTimeField(auto_now_add=True)
#     created_by = models.CharField(max_length=50, default='UNKNOWN')
#     modified_date = models.DateTimeField(auto_now=True)
#     modified_by = models.CharField(max_length=50, default='UNKNOWN')

#     class Meta:
#         abstract = True

class Itinerary(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    default_gathering_size = models.IntegerField(default=8)

    class Meta:
        ordering = ['-start_date']

class Event(models.Model):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)
    cancelled_date = models.DateTimeField(null=True)
    cancelled_reason = models.TextField(null=True, max_length=500)
#    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['itinerary','start_date']

class Member(models.Model):
    PRONOUNS = (
        (0,'Unspecified'),
        (1,'He/Him'),
        (2,'She/Her'),
        (3,'Them/They'),
    )
    # group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)
    preferred_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, null=True)
    middle_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    pronouns = models.IntegerField(choices=PRONOUNS, default=0)
    email = models.EmailField(max_length=150, null=True)
    phone = models.IntegerField(null=True)
    street_address = models.CharField(max_length=150, null=True)
    zip_code = models.IntegerField(null=True)
    host_note = models.TextField(max_length=500, null=True)
    attendee_note = models.TextField(max_length=500, null=True)
    # is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['last_name','preferred_name','first_name']

class Group(models.Model):
    name = models.CharField(max_length=150)
    host_member = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)
    # is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

class GroupMembership(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    group_is_primary = models.BooleanField(default=True)
    # is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['group','group_is_primary','member']
    
# https://docs.djangoproject.com/en/1.10/topics/db/models/#be-careful-with-related-name-and-related-query-name
class Conflict(models.Model):
    conflicted_a = models.ForeignKey(Group, related_name='%(class)s_conflicted_a', on_delete=models.CASCADE)
    conflicted_b = models.ForeignKey(Group, related_name='%(class)s_conflicted_b', on_delete=models.CASCADE)
#    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ['conflicted_a','conflicted_b']
        # constraints = [
        #     models.UniqueConstraint(fields=['belligerant_a', 'belligerant_b'], name='uq_group_conflict')
        # ]

class FoodRestriction(models.Model):
    FOOD_RESTRICTIONS = (
        (0,'Other'), # Tuple -> (INTEGER KEY, STRING VALUE)
        (1,'Peanut'),
        (2,'Milk'),
        (3,'Egg'),
        (4,'Wheat'),
        (5,'Soy'),
        (6,'Fish'),
        (7,'Shellfish'),
        (8,'Alcohol'),
        (9,'Caffeine'),
    )
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    restriction = models.IntegerField(choices=FOOD_RESTRICTIONS)

    class Meta:
        ordering = ['member','restriction']


class Diet(models.Model):
    DIETS = (
        (0,'Other'),
        (1,'Raw'),
        (2,'Vegan'),
        (3,'Vegetarian'),
        (4,'Low-Acid'),
        (5,'Low-Carb'),
        (6,'Low-Fat'),
        (7,'Low-Sodium'),
        (8,'Ketogenic'),
        (9,'Gluten Free'),
        (10,'Sugar Free'),
        (11,'Soft Diet'),
        (12,'Liquid Diet'),
        (13,'Kosher'),
        (14,'Halal'),
    )
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    diet = models.IntegerField(choices=DIETS)

    class Meta:
        ordering = ['member','diet']

class Gathering(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    # TODO
    #   host_group = models.ForeignKey(Group, on_delete=models.SET(get_deleted_roup))
    #   host_member = models.ForeignKey(Member, on_delete=models.SET(get_deleted_member))
    host_group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)
    host_member = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)
    cancelled_date = models.DateTimeField(null=True)
    cancelled_reason = models.TextField(null=True, max_length=500)

    class Meta:
        ordering = ['event', 'host_group']

class Availability(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    can_attend = models.BooleanField(default=True)
    can_host = models.BooleanField(default=True)

    class Meta:
        ordering = ['event', 'group']

class Attendance(models.Model):
    ATTENDANCE_TYPE = (
        (0,'Cancelled'),
        (1,'Attendee'),
        (2,'Host')
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    gathering = models.ForeignKey(Gathering, on_delete=models.CASCADE)
    attendance_type = models.IntegerField(choices=ATTENDANCE_TYPE)

    class Meta:
        ordering = ['gathering','-attendance_type','group']

class EmailTemplate(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500, null=True)
    subject = models.CharField(max_length=255)
    body = models.TextField()

    class Meta:
        ordering = ['name']

class EmailLog(models.Model):
    template = models.ForeignKey(EmailTemplate, null=True, on_delete=models.SET_NULL)
    to_addresses = models.TextField()
    from_addresses = models.TextField()
    cc_addresses = models.TextField(null=True)
    sent_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-sent_date']

