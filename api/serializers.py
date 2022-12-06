from rest_framework import serializers
from home.models import *


class MainTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainTitle
        fields = ['title']


class MainAboutUsTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainAboutUsTitle
        fields = ['title', 'text']


class AboutUsTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainAboutUsTitle
        fields = ['title', 'text', 'video']


class MainAboutUsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainAboutUsImage
        fields = ['title', 'image']


class MainAboutUsStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainAboutUsStatistic
        fields = ['title', 'subtitle', 'icon']


class MainOurServiceTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainOurServiceText
        fields = ['id', 'title', 'text']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'text', 'icon', 'icon_style']


class ServiceForFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title']


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['id', 'title', 'icon']


class MainTechnologyCardSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True)

    class Meta:
        model = MainTechnologyCard
        fields = ['id', 'title', 'technologies']


class PortifolioCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PortifolioCategory
        fields = ['id', 'title']


class PortifolioImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortifolioImage
        fields = ['id', 'title', 'image']


class PortifolioSerializer(serializers.ModelSerializer):
    category = PortifolioCategorySerializer()
    images = PortifolioImageSerializer(many=True)

    class Meta:
        model = Portifolio
        fields = ['id', 'title', 'images', 'description',
                  'category', 'type', 'video', 'link']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'name', 'logo', 'website']


class PartnerFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerFeedback
        fields = ['id', 'partner_name', 'partner_bio',
                  'partner_image', 'feedback']


class PartnerFeedbackTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerFeedbackTitle
        fields = ['title', 'text']


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['address', 'facebook', 'instagram', 'telegram',
                  'tweeter', 'linkedin', 'youtube', 'phone1', 'phone2', 'email']


class TeamSerializer(serializers.ModelSerializer):
    technalogies = TechnologySerializer(many=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'title', 'technalogies', 'image', 'order']


class IndustryTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryTitle
        fields = ['id', 'title', 'text']


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ['id', 'title', 'text', 'icon', 'icon_style']


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['id', 'title', 'text', 'short_title']


class FormContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormContent
        fields = ['id', 'title', 'subtitle1', 'text1', 'subtitle2',
                  'text2', 'hide_second_part', 'type', 'is_active']


class ClientMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientMessage
        fields = "__all__"


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = "__all__"
