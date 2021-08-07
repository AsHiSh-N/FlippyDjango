from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from api.serializers import CardSerializer
from api.models import Card
from rest_framework.decorators import api_view


# Create your views here.
# find card with id
@api_view(['GET', 'PUT', 'DELETE'])

def card_detail(request, pk):
    card =Card.objects.get(pk=pk)
 
    if request.method == 'GET': 
        card_serializer = CardSerializer(card) 
        return JsonResponse(card_serializer.data) 

    # to update card using id    
    elif request.method == 'PUT': 
        card_data = JSONParser().parse(request) 
        card_serializer = CardSerializer(card, data=card_data) 
        if card_serializer.is_valid(): 
            card_serializer.save() 
            return JsonResponse(card_serializer.data) 
        return JsonResponse(card_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    #to delete a card using id    
    elif request.method == 'DELETE': 
        card.delete() 
        return JsonResponse({'message': 'Card was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST', 'DELETE'])
def card_list(request):
    card = Card.objects.all()

    if request.method == 'GET': 
        card_serializer = CardSerializer(card, many = True) 
        print(card)
        return JsonResponse(card_serializer.data, safe=False)
 
    elif request.method == 'POST':
        card_data = JSONParser().parse(request)
        card_serializer = CardSerializer(data=card_data)
        if card_serializer.is_valid():
            card_serializer.save()
            return JsonResponse(card_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(card_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Card.objects.all().delete()
        return JsonResponse({'message': '{} Cards were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


