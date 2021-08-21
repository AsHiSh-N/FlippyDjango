from django.db import models
from django.contrib.auth.models import User


import uuid
# Create your models here.

class Deck(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # owner = models.ForeignKey(User, default='aasu', blank = True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # owner = models.ForeignKey(User,default = 'aasu', blank = True,on_delete=models.CASCADE)
    front = models.CharField(max_length=40, blank=True, default='')
    back = models.CharField(max_length=50, blank=False, default='')
    desc = models.TextField(max_length=100, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deck = models.ForeignKey(Deck,related_name = "cards", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)