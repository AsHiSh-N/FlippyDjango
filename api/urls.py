from django.urls import path 
from . import views 
 
urlpatterns = [ 
    path('', views.card_list),
    path('<uuid:pk>/', views.card_detail),
    # path('published/', views.card_list_published)
]
