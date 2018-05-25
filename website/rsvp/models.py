from django.db import models

# Create your models here.

class Guest(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    rsvp = models.BooleanField
    additions = models.IntegerField(null=True, blank=True)
    message = models.CharField(max_length=1020)
    created = models.DateTimeField
    
    def __str__(self):
        return self.name
