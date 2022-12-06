from django.urls import path
from api import api_views

urlpatterns = [
    path('home/<str:lng>/', api_views.homePageApi),
    path('portifolio-category/<str:lng>/', api_views.portifolioCategoryView),
    path('portifolio/<str:lng>/', api_views.portifolioView),
    path('about/<str:lng>/', api_views.aboutPageView),
    path('feadback/<str:lng>/', api_views.feadbackView),
    path('vacansy/<str:lng>/', api_views.vacancyView),
    path('service/<str:lng>/', api_views.serviceView),
    path('form-content/<str:lng>/', api_views.formContentView),
    path('client-message/', api_views.postClientMessageView),
    path('resume/', api_views.postResumeView),

]
