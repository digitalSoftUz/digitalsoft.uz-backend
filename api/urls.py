from django.urls import path
from api import api_views

urlpatterns = [
    path('home/', api_views.homePageApi),
    path('portifolio-category/', api_views.portifolioCategoryView),
    path('portifolio/', api_views.portifolioView),
    path('about/', api_views.aboutPageView),
    path('feadback/', api_views.feadbackView),
    path('vacansy/', api_views.vacancyView),
    path('service/', api_views.serviceView),
    path('form-content/', api_views.formContentView),
    path('client-message/', api_views.postClientMessageView),
    path('resume/', api_views.postResumeView),

]
