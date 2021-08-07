from django.db import models
from rest_framework import serializers
from .models import Card, Deck

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = (
            'id',
            'front',
            'back',
            'desc',
            'created_at',
            'updated_at'
        )


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = (
            'id',
            'title',
            'desc'
        )
