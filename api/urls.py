# from api.view import deck_list
from django.urls import path 
from api.views.card import CardList, CardDetail
from api.views.deck import DeckList, DeckDetail

urlpatterns = [ 
    path('card/', CardList.as_view()),
    path('card/<uuid:pk>', CardDetail.as_view()),
    path('deck/', DeckList.as_view()),
    path('deck/<uuid:pk>', DeckDetail.as_view())
    # path('published/', views.card_list_published)
]
