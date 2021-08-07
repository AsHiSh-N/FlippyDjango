from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from api.serializers import DeckSerializer
from api.models import Deck
from rest_framework.decorators import api_view

# Create your views here.
# find card with id
@api_view(['GET', 'PUT', 'DELETE'])

def deck_detail(request, pk):
    deck =Deck.objects.get(pk=pk)
 
    if request.method == 'GET': 
        deck_serializer = DeckSerializer(deck) 
        return JsonResponse(deck_serializer.data) 

    # to update card using id    
    elif request.method == 'PUT': 
        deck_data = JSONParser().parse(request) 
        deck_serializer = DeckSerializer(deck, data=deck_data) 
        if deck_serializer.is_valid():
            deck_serializer.save() 
            return JsonResponse(deck_serializer.data) 
        return JsonResponse(deck_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    #to delete a card using id    
    elif request.method == 'DELETE': 
        deck.delete() 
        return JsonResponse({'message': 'Deck was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST', 'DELETE'])
def deck_list(request):
    deck = Deck.objects.all()

    if request.method == 'GET': 
        deck_serializer = DeckSerializer(deck, many = True) 
        # print(card)
        return JsonResponse(deck_serializer.data, safe=False)
 
    elif request.method == 'POST':
        deck_data = JSONParser().parse(request)
        deck_serializer = DeckSerializer(data=deck_data)
        if deck_serializer.is_valid():
            deck_serializer.save()
            return JsonResponse(deck_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(deck_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Deck.objects.all().delete()
        return JsonResponse({'message': '{} Decks were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


