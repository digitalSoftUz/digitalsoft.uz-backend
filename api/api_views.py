from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

@api_view(['GET'])
def homePageApi(request):
    mainTitle = MainTitle.objects.filter(is_active=True).last()
    mainAboutUs = MainAboutUsTitle.objects.filter(is_active=True).last()
    mainAboutUsImages = MainAboutUsImage.objects.filter(is_active=True)[:5]
    mainAboutUsStatistics = MainAboutUsStatistic.objects.filter(is_active=True)[0:4]
    mainOurServiceText = MainOurServiceText.objects.filter(is_active=True).last()
    mainSeriveces = Service.objects.filter(is_active=True, is_show_main=True).order_by("order")[:6]
    mainTechnologyCard = MainTechnologyCard.objects.filter(is_active=True).order_by('order')
    partners = Partner.objects.filter(is_active=True)
    partnerFeedbackTitle = PartnerFeedbackTitle.objects.filter(is_active=True).last()
    partnerFeedback = PartnerFeedback.objects.filter(is_active=True).order_by('order')[:8]
    contactInfo = ContactInfo.objects.filter(is_active=True).last()

    context = {
        "mainTitle":MainTitleSerializer(mainTitle).data,
        "mainAboutUs":MainAboutUsTitleSerializer(mainAboutUs).data,
        "mainAboutUsImages":MainAboutUsImageSerializer(mainAboutUsImages, many=True).data,
        "mainAboutUsStatistics": MainAboutUsStatisticSerializer(mainAboutUsStatistics, many=True).data,
        "mainOurServiceText": MainOurServiceTextSerializer(mainOurServiceText).data,
        "mainSeriveces": ServiceSerializer(mainSeriveces, many=True).data,
        "mainTechnologyCard": MainTechnologyCardSerializer(mainTechnologyCard, many=True).data,
        "partners": PartnerSerializer(partners, many=True).data,
        "partnerFeedbackTitle": PartnerFeedbackTitleSerializer(partnerFeedbackTitle).data,
        "partnerFeedback": PartnerFeedbackSerializer(partnerFeedback, many=True).data,
        "contactInfo": ContactInfoSerializer(contactInfo).data
    }

    return Response(context)