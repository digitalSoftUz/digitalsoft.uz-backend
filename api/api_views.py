from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .pagination import pagination_json


@api_view(['GET'])
def homePageApi(request, lng):
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

        if lng == 'ru':
            context = {
                "mainTitle": MainTitleSerializerRu(mainTitle).data,
                "mainAboutUs": MainAboutUsTitleSerializerRu(mainAboutUs).data,
                "mainAboutUsImages": MainAboutUsImageSerializer(mainAboutUsImages, many=True).data,
                "mainAboutUsStatistics": MainAboutUsStatisticSerializerRu(mainAboutUsStatistics, many=True).data,
                "mainOurServiceText": MainOurServiceTextSerializerRu(mainOurServiceText).data,
                "mainSeriveces": ServiceSerializerRu(mainSeriveces, many=True).data,
                "mainTechnologyCard": MainTechnologyCardSerializerRu(mainTechnologyCard, many=True).data,
                "partners": PartnerSerializerRu(partners, many=True).data,
                "partnerFeedbackTitle": PartnerFeedbackTitleSerializerRu(partnerFeedbackTitle).data,
                "partnerFeedback": PartnerFeedbackSerializerRu(partnerFeedback, many=True).data,
                "contactInfo": ContactInfoSerializerRu(contactInfo).data
            }
        elif lng == 'en':
            context = {
                "mainTitle": MainTitleSerializerEn(mainTitle).data,
                "mainAboutUs": MainAboutUsTitleSerializerEn(mainAboutUs).data,
                "mainAboutUsImages": MainAboutUsImageSerializer(mainAboutUsImages, many=True).data,
                "mainAboutUsStatistics": MainAboutUsStatisticSerializerEn(mainAboutUsStatistics, many=True).data,
                "mainOurServiceText": MainOurServiceTextSerializerEn(mainOurServiceText).data,
                "mainSeriveces": ServiceSerializerEn(mainSeriveces, many=True).data,
                "mainTechnologyCard": MainTechnologyCardSerializerEn(mainTechnologyCard, many=True).data,
                "partners": PartnerSerializerEn(partners, many=True).data,
                "partnerFeedbackTitle": PartnerFeedbackTitleSerializerEn(partnerFeedbackTitle).data,
                "partnerFeedback": PartnerFeedbackSerializerEn(partnerFeedback, many=True).data,
                "contactInfo": ContactInfoSerializerEn(contactInfo).data
            }
        else:
            context = {
                "mainTitle": MainTitleSerializerUz(mainTitle).data,
                "mainAboutUs": MainAboutUsTitleSerializerUz(mainAboutUs).data,
                "mainAboutUsImages": MainAboutUsImageSerializer(mainAboutUsImages, many=True).data,
                "mainAboutUsStatistics": MainAboutUsStatisticSerializerUz(mainAboutUsStatistics, many=True).data,
                "mainOurServiceText": MainOurServiceTextSerializerUz(mainOurServiceText).data,
                "mainSeriveces": ServiceSerializerUz(mainSeriveces, many=True).data,
                "mainTechnologyCard": MainTechnologyCardSerializerUz(mainTechnologyCard, many=True).data,
                "partners": PartnerSerializerUz(partners, many=True).data,
                "partnerFeedbackTitle": PartnerFeedbackTitleSerializerUz(partnerFeedbackTitle).data,
                "partnerFeedback": PartnerFeedbackSerializerUz(partnerFeedback, many=True).data,
                "contactInfo": ContactInfoSerializerUz(contactInfo).data
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
def portifolioCategoryView(request, lng):
    try:
        category = PortifolioCategory.objects.filter(is_active=True)
        if lng == 'ru':
            ser = PortifolioCategorySerializerRu(category, many=True)
        elif lng == 'en':
            ser = PortifolioCategorySerializerEn(category, many=True)
        else:
            ser = PortifolioCategorySerializerUz(category, many=True)
        data = {
            "success": True,
            "data": ser.data
        }
        return Response(data)
    except Exception as err:
        return Response({
            "success": False,
            "error": f"{err}"
        })


@api_view(['GET'])
def portifolioView(request, lng):
    try:
        category = request.GET.get('category', 0)
        count = int(request.GET.get('count', 7))
        is_show_main = request.GET.get('is_show_main')
        page = request.GET.get('page')
        if int(category) == 0:
            portifolio = Portifolio.objects.filter(
                is_active=True).order_by('order')
        else:
            portifolio = Portifolio.objects.filter(
                is_active=True, category_id=category).order_by('order')

        if is_show_main is not None:
            portifolio = portifolio.filter(is_show_main=True)

        if lng == 'ru':
            res = pagination_json(
                page, portifolio, PortifolioSerializerRu, count)
        elif lng == 'en':
            res = pagination_json(
                page, portifolio, PortifolioSerializerEn, count)
        else:
            res = pagination_json(
                page, portifolio, PortifolioSerializerUz, count)

        data = {
            "success": True,
            "data": res
        }
        return Response(data)
    except Exception as err:
        return Response({
            "success": False,
            "error": f"{err}"
        })


@api_view(['GET'])
def aboutPageView(request, lng):
    try:
        aboutUs = MainAboutUsTitle.objects.filter(is_active=True).last()
        aboutUsStatistics = MainAboutUsStatistic.objects.filter(is_active=True)[
            0:4]
        services = Service.objects.filter(is_active=True).order_by("order")
        team = TeamCategory.objects.filter(is_active=True).order_by('order')
        industrytitle = IndustryTitle.objects.filter(is_active=True).last()
        industry = Industry.objects.filter(is_active=True)[0:4]
        if lng == "ru":
            data = {
                "aboutUs": AboutUsTitleSerializerRu(aboutUs).data,
                "aboutUsStatistics": MainAboutUsStatisticSerializerRu(aboutUsStatistics, many=True).data,
                "services": ServiceSerializerRu(services, many=True).data,
                "team": TeamCategorySerializerRu(team, many=True).data,
                "industryTitle": IndustryTitleSerializerRu(industrytitle).data,
                "industry": IndustrySerializerRu(industry, many=True).data,
            }
        elif lng == "en":
            data = {
                "aboutUs": AboutUsTitleSerializerEn(aboutUs).data,
                "aboutUsStatistics": MainAboutUsStatisticSerializerEn(aboutUsStatistics, many=True).data,
                "services": ServiceSerializerEn(services, many=True).data,
                "team": TeamCategorySerializerEn(team, many=True).data,
                "industryTitle": IndustryTitleSerializerEn(industrytitle).data,
                "industry": IndustrySerializerEn(industry, many=True).data,
            }
        else:
            data = {
                "aboutUs": AboutUsTitleSerializerUz(aboutUs).data,
                "aboutUsStatistics": MainAboutUsStatisticSerializerUz(aboutUsStatistics, many=True).data,
                "services": ServiceSerializerUz(services, many=True).data,
                "team": TeamCategorySerializerUz(team, many=True).data,
                "industryTitle": IndustryTitleSerializerUz(industrytitle).data,
                "industry": IndustrySerializerUz(industry, many=True).data,
            }

        return Response(data)
    except Exception as err:
        return Response({
            "success": False,
            "error": f"{err}"
        })


@api_view(['GET'])
def feadbackView(request, lng):
    try:
        feadbackTitle = PartnerFeedbackTitle.objects.filter(
            is_active=True).last()
        feadback = PartnerFeedback.objects.filter(
            is_active=True).order_by('order')

        if lng == 'ru':
            ft_res = PartnerFeedbackTitleSerializerRu(feadbackTitle).data
            fb_res = PartnerFeedbackSerializerRu(feadback, many=True).data
        elif lng == 'en':
            ft_res = PartnerFeedbackTitleSerializerEn(feadbackTitle).data
            fb_res = PartnerFeedbackSerializerEn(feadback, many=True).data
        else:
            ft_res = PartnerFeedbackTitleSerializerUz(feadbackTitle).data
            fb_res = PartnerFeedbackSerializerUz(feadback, many=True).data
        data = {
            "success": True,
            "data": {
                "feadbackTitle": ft_res,
                "feadBack": fb_res
            }
        }
        return Response(data)
    except Exception as err:
        return Response({
            "success": False,
            "error": f"{err}"
        })


@api_view(['GET'])
def vacancyView(request, lng):
    try:
        vacany = Vacancy.objects.filter(is_active=True).order_by('order')
        if lng == 'ru':
            data = VacancySerializerRu(vacany, many=True).data
        elif lng == 'en':
            data = VacancySerializerEn(vacany, many=True).data
        else:
            data = VacancySerializerUz(vacany, many=True).data
        return Response(
            data
        )
    except Exception as err:
        return Response({
            "success": False,
            "error": f"{err}"
        })


@api_view(['GET'])
def serviceView(request, lng):
    try:
        service = Service.objects.filter(is_active=True).order_by('order')
        if lng == 'ru':
            data = ServiceForFormSerializerRu(service, many=True).data
        elif lng == 'en':
            data = ServiceForFormSerializerEn(service, many=True).data
        else:
            data = ServiceForFormSerializerUz(service, many=True).data
        return Response(
            data
        )
    except Exception as err:
        return Response({
            "success": False,
            "error": f"{err}"
        })


@api_view(['GET'])
def formContentView(request, lng):
    try:
        type = request.GET.get('type', 'Project')
        content = FormContent.objects.filter(is_active=True, type=type).last()
        if lng == 'ru':
            data = FormContentSerializerRu(content).data
        elif lng == 'en':
            data = FormContentSerializerEn(content).data
        else:
            data = FormContentSerializerUz(content).data
        return Response(
            data
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
