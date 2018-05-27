from django.db import models

# Create your models here.

class Guest(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    rsvp = models.BooleanField(default=False)
    additions = models.IntegerField(null=True, blank=True)
    message = models.CharField(max_length=1020)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
