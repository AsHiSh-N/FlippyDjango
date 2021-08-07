# from api.view import deck_list
from django.urls import path 
from . import views 
 
urlpatterns = [ 
    path('card/', views.card_list),
    path('card/<uuid:pk>', views.card_detail),
    path('deck/', views.deck_list),
    # path('published/', views.card_list_published)
]
