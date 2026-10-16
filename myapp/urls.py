from django.urls import path
from .views import *

urlpatterns = [
    path('',index_view,name='index_page'),
    path('search/',search_menu,name='search_form'),
    path('search/<str:menu>/',search,name='search'),
]
