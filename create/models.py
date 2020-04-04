from django.conf import settings
from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    college = models.CharField(max_length=50)
    university_roll = models.CharField(max_length=15)
    contact = models.CharField(max_length=15)
    certificate = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    
    def publish(self):
        #self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.email
