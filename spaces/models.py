from django.db import models


class Location(models.Model):
    location_name = models.CharField(max_length=200)

    def __str__(self):
        return self.location_name
    
    def __repr__(self):
        return self.location_name

class Space(models.Model):

    SPACE_TYPE = [
        ("cafe", "cafe"),
        ("coworking space", "coworking space"),
        ("open area", "open area"),
        ("hostel", "hostel"),
    ]

    space_name = models.CharField(max_length=200)
    is_type = models.CharField(max_length=25,choices=SPACE_TYPE)
    has_internet = models.BooleanField(default=False)
    is_meeting_friendly = models.BooleanField(default=False)
    location = models.ManyToManyField(Location)
    url = models.URLField(max_length=200, null=True, blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.space_name
    
    def __repr__(self):
        return self.space_name
    
