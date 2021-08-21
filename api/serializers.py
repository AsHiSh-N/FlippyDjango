from django.db import models
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Card, Deck

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = (
            'id',
            # 'owner',
            'front',
            'back',
            'desc',
            'deck',
            'created_at',
            'updated_at'
        )


class DeckSerializer(serializers.ModelSerializer):
    # cards = serializers.SerializerMethodField('get_cards')
    cards = CardSerializer(read_only=True, many=True)
    # cards = serializers.PrimaryKeyRelatedField(many = True, read_only = True )
   

    class Meta:
        model = Deck
        fields =(
            'id',
            # 'owner',
            'title',
            'desc',
            'cards'
        )

    # def get_cards(self, obj,pk):
    #    data = CardSerializer(Card.objects.filter(deck__id=pk), many=True).data
    #    return data
