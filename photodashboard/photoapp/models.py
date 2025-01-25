
from django.db import models

class EventPhoto(models.Model):
    event_name = models.CharField(max_length=255)
    photo = models.BinaryField()

    def __str__(self):
        return self.event_name

