from django.urls import path
from api import api_views

urlpatterns = [
    path('home/', api_views.homePageApi)
]