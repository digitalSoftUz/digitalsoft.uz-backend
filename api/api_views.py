from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

@api_view(['GET'])
def homePageApi(request):
    mainTitle = MainTitle.objects.filter(is_active=True).last()
    