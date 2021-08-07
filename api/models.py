from django.db import models


import uuid
# Create your models here.
class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    front = models.CharField(max_length=30, blank=True, default='')
    back = models.CharField(max_length=30, blank=False, default='')
    desc = models.TextField(max_length=100, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

# class Deck(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

