from django.db import models

import uuid
# Create your models here.
class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    front = models.CharField(max_length=30, blank=True, default='')
    back = models.CharField(max_length=30, blank=False, default='')
    desc = models.TextField(max_length=100, blank=True, default='')
    # published = models.BooleanField(default=False)


    def __str__(self):
        return str(self.id)