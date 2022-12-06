from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .pagination import pagination_json


@api_view(['GET'])
def homePageApi(request):
    try:
        mainTitle = MainTitle.objects.filter(is_active=True).last()
        mainAboutUs = MainAboutUsTitle.objects.filter(is_active=True).last()
        mainAboutUsImages = MainAboutUsImage.objects.filter(is_active=True)[:5]
        mainAboutUsStatistics = MainAboutUsStatistic.objects.filter(is_active=True)[
            0:4]
        mainOurServiceText = MainOurServiceText.objects.filter(
            is_active=True).last()
        mainSeriveces = Service.objects.filter(
            is_active=True, is_show_main=True).order_by("order")[:6]
        mainTechnologyCard = MainTechnologyCard.objects.filter(
            is_active=True).order_by('order')
        partners = Partner.objects.filter(is_active=True)
        partnerFeedbackTitle = PartnerFeedbackTitle.objects.filter(
            is_active=True).last()
        partnerFeedback = PartnerFeedback.objects.filter(
            is_active=True).order_by('order')[:8]
        contactInfo = ContactInfo.objects.filter(is_active=True).last()

        context = {
            "mainTitle": MainTitleSerializer(mainTitle).data,
            "mainAboutUs": MainAboutUsTitleSerializer(mainAboutUs).data,
            "mainAboutUsImages": MainAboutUsImageSerializer(mainAboutUsImages, many=True).data,
            "mainAboutUsStatistics": MainAboutUsStatisticSerializer(mainAboutUsStatistics, many=True).data,
            "mainOurServiceText": MainOurServiceTextSerializer(mainOurServiceText).data,
            "mainSeriveces": ServiceSerializer(mainSeriveces, many=True).data,
            "mainTechnologyCard": MainTechnologyCardSerializer(mainTechnologyCard, many=True).data,
            "partners": PartnerSerializer(partners, many=True).data,
            "partnerFeedbackTitle": PartnerFeedbackTitleSerializer(partnerFeedbackTitle).data,
            "partnerFeedback": PartnerFeedbackSerializer(partnerFeedback, many=True).data,
            "contactInfo": ContactInfoSerializer(contactInfo).data
        }

        return Response({
            "success": True,
            "data": context
        })
    except Exception as err:
        return Response({
            "success": False,
            "error": f"{err}"
        })


@api_view(['GET'])
def portifolioCategoryView(request):
    try:
        category = PortifolioCategory.objects.filter(is_active=True)
        data = {
            "success": True,
            "data": PortifolioCategorySerializer(category, many=True).data
        }
        return Response(data)
    except Exception as err:
        return Response({
            "success": False,
            "error": f"{err}"
        })


@api_view(['GET'])
def portifolioView(request):
    try:
        category = request.GET.get('category', 0)
        count = int(request.GET.get('count', 7))
        page = request.GET.get('page')
        if int(category) == 0:
            portifolio = Portifolio.objects.filter(
                is_active=True, is_show_main=True).order_by('order')[:count]
        else:
            portifolio = Portifolio.objects.filter(
                is_active=True, is_show_main=True, category_id=category).order_by('order')[:count]
        data = {
            "success": True,
            "data": pagination_json(page, portifolio, PortifolioSerializer, count)
        }
        return Response(data)
    except Exception as err:
        return Response({
            "success": False,
            "error": f"{err}"
        })


@api_view(['GET'])
def aboutPageView(request):
    try:
        aboutUs = MainAboutUsTitle.objects.filter(is_active=True).last()
        aboutUsStatistics = MainAboutUsStatistic.objects.filter(is_active=True)[
            0:4]
        services = Service.objects.filter(is_active=True).order_by("order")
        team = Team.objects.filter(is_active=True).order_by('order')
        industrytitle = IndustryTitle.objects.filter(is_active=True).last()
        industry = Industry.objects.filter(is_active=True)[0:4]

        data = {
            "aboutUs": AboutUsTitleSerializer(aboutUs).data,
            "aboutUsStatistics": MainAboutUsStatisticSerializer(aboutUsStatistics, many=True).data,
            "services": ServiceSerializer(services, many=True).data,
            "team": TeamSerializer(team, many=True).data,
            "industryTitle": IndustryTitleSerializer(industrytitle).data,
            "industry": IndustrySerializer(industry, many=True).data,
        }

        return Response(data)
    except Exception as err:
        return Response({
            "success": False,
            "error": f"{err}"
        })


@api_view(['GET'])
def feadbackView(request):
    try:
        feadbackTitle = PartnerFeedbackTitle.objects.filter(
            is_active=True).last()
        feadback = PartnerFeedback.objects.filter(
            is_active=True).order_by('order')
        data = {
            "success": True,
            "data": {
                "feadbackTitle": PartnerFeedbackTitleSerializer(feadbackTitle).data,
                "feadBack": PartnerFeedbackSerializer(feadback, many=True).data
            }
        }
        return Response(data)
    except Exception as err:
        return Response({
            "success": False,
            "error": f"{err}"
        })


@api_view(['GET'])
def vacancyView(request):
    try:
        vacany = Vacancy.objects.filter(is_active=True).order_by('order')
        return Response(
            VacancySerializer(vacany, many=True).data
        )
    except Exception as err:
        return Response({
            "success": False,
            "error": f"{err}"
        })


@api_view(['GET'])
def serviceView(request):
    try:
        service = Service.objects.filter(is_active=True).order_by('order')
        return Response(
            ServiceForFormSerializer(service, many=True).data
        )
    except Exception as err:
        return Response({
            "success": False,
            "error": f"{err}"
        })


@api_view(['GET'])
def formContentView(request):
    try:
        type = request.GET.get('type', 'Project')
        content = FormContent.objects.filter(is_active=True, type=type).last()

        return Response(
            FormContentSerializer(content).data
        )
    except Exception as err:
        return Response({
            "success": False,
            "error": f"{err}"
        })


@api_view(['GET'])
def formContentView(request):
    try:
        type = request.GET.get('type', 'Project')
        content = FormContent.objects.filter(is_active=True, type=type).last()

        return Response(
            FormContentSerializer(content).data
        )
    except Exception as err:
        return Response({
            "success": False,
            "error": f"{err}"
        })


@api_view(['POST'])
def postClientMessageView(request):
    try:
        data = request.data
        ser = ClientMessageSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"success": True})
        else:
            return Response({"success": False, 'error': f"{ser.error_messages}"})
    except Exception as err:
        return Response({
            "success": False,
            "error": f"{err}"
        })


@api_view(['POST'])
def postResumeView(request):
    try:
        data = request.data
        ser = ResumeSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"success": True})
        else:
            return Response({"success": False, 'error': f"{ser.error_messages}"})
    except Exception as err:
        return Response({
            "success": False,
            "error": f"{err}"
        })
