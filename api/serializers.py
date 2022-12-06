from rest_framework import serializers
from home.models import *


class MainTitleSerializerUz(serializers.ModelSerializer):
    class Meta:
        model = MainTitle
        fields = ['title_uz']


class MainTitleSerializerRu(serializers.ModelSerializer):
    class Meta:
        model = MainTitle
        fields = ['title_ru']


class MainTitleSerializerEn(serializers.ModelSerializer):
    class Meta:
        model = MainTitle
        fields = ['title_en']


class MainAboutUsTitleSerializerUz(serializers.ModelSerializer):
    class Meta:
        model = MainAboutUsTitle
        fields = ['title_uz', 'text_uz']


class MainAboutUsTitleSerializerRu(serializers.ModelSerializer):
    class Meta:
        model = MainAboutUsTitle
        fields = ['title_ru', 'text_ru']


class MainAboutUsTitleSerializerEn(serializers.ModelSerializer):
    class Meta:
        model = MainAboutUsTitle
        fields = ['title_en', 'text_en']


class AboutUsTitleSerializerUz(serializers.ModelSerializer):
    class Meta:
        model = MainAboutUsTitle
        fields = ['title_uz', 'text_uz', 'video']


class AboutUsTitleSerializerRu(serializers.ModelSerializer):
    class Meta:
        model = MainAboutUsTitle
        fields = ['title_ru', 'text_ru', 'video']


class AboutUsTitleSerializerEn(serializers.ModelSerializer):
    class Meta:
        model = MainAboutUsTitle
        fields = ['title_en', 'text_en', 'video']


class MainAboutUsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainAboutUsImage
        fields = ['title', 'image']


class MainAboutUsStatisticSerializerUz(serializers.ModelSerializer):
    class Meta:
        model = MainAboutUsStatistic
        fields = ['title_uz', 'subtitle_uz', 'icon']


class MainAboutUsStatisticSerializerRu(serializers.ModelSerializer):
    class Meta:
        model = MainAboutUsStatistic
        fields = ['title_ru', 'subtitle_ru', 'icon']


class MainAboutUsStatisticSerializerEn(serializers.ModelSerializer):
    class Meta:
        model = MainAboutUsStatistic
        fields = ['title_en', 'subtitle_en', 'icon']


class MainOurServiceTextSerializerUz(serializers.ModelSerializer):
    class Meta:
        model = MainOurServiceText
        fields = ['id', 'title_uz', 'text_uz']


class MainOurServiceTextSerializerRu(serializers.ModelSerializer):
    class Meta:
        model = MainOurServiceText
        fields = ['id', 'title_ru', 'text_ru']


class MainOurServiceTextSerializerEn(serializers.ModelSerializer):
    class Meta:
        model = MainOurServiceText
        fields = ['id', 'title_en', 'text_en']


class ServiceSerializerUz(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title_uz', 'text_uz', 'icon', 'icon_style']


class ServiceSerializerRu(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title_ru', 'text_ru', 'icon', 'icon_style']


class ServiceSerializerEn(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title_en', 'text_en', 'icon', 'icon_style']


class ServiceForFormSerializerUz(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title_uz']


class ServiceForFormSerializerRu(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title_ru']


class ServiceForFormSerializerEn(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title_en']


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['id', 'title', 'icon']


class MainTechnologyCardSerializerUz(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True)

    class Meta:
        model = MainTechnologyCard
        fields = ['id', 'title_uz', 'technologies']


class MainTechnologyCardSerializerRu(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True)

    class Meta:
        model = MainTechnologyCard
        fields = ['id', 'title_ru', 'technologies']


class MainTechnologyCardSerializerEn(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True)

    class Meta:
        model = MainTechnologyCard
        fields = ['id', 'title_en', 'technologies']


class PortifolioCategorySerializerUz(serializers.ModelSerializer):
    class Meta:
        model = PortifolioCategory
        fields = ['id', 'title_uz']


class PortifolioCategorySerializerEn(serializers.ModelSerializer):
    class Meta:
        model = PortifolioCategory
        fields = ['id', 'title_en']


class PortifolioCategorySerializerRu(serializers.ModelSerializer):
    class Meta:
        model = PortifolioCategory
        fields = ['id', 'title_ru']


class PortifolioImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortifolioImage
        fields = ['id', 'title', 'image']


class PortifolioSerializerUz(serializers.ModelSerializer):
    category = PortifolioCategorySerializerUz()
    images = PortifolioImageSerializer(many=True)

    class Meta:
        model = Portifolio
        fields = ['id', 'title_uz', 'images', 'description_uz',
                  'category', 'type', 'video', 'link']


class PortifolioSerializerRu(serializers.ModelSerializer):
    category = PortifolioCategorySerializerRu()
    images = PortifolioImageSerializer(many=True)

    class Meta:
        model = Portifolio
        fields = ['id', 'title_ru', 'images', 'description_ru',
                  'category', 'type', 'video', 'link']


class PortifolioSerializerEn(serializers.ModelSerializer):
    category = PortifolioCategorySerializerEn()
    images = PortifolioImageSerializer(many=True)

    class Meta:
        model = Portifolio
        fields = ['id', 'title_en', 'images', 'description_en',
                  'category', 'type', 'video', 'link']


class PartnerSerializerUz(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'name_uz', 'logo', 'website']


class PartnerSerializerRu(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'name_ru', 'logo', 'website']


class PartnerSerializerEn(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'name_en', 'logo', 'website']


class PartnerFeedbackSerializerUz(serializers.ModelSerializer):
    class Meta:
        model = PartnerFeedback
        fields = ['id', 'partner_name_uz', 'partner_bio_uz',
                  'partner_image', 'feedback_uz']


class PartnerFeedbackSerializerRu(serializers.ModelSerializer):
    class Meta:
        model = PartnerFeedback
        fields = ['id', 'partner_name_ru', 'partner_bio_ru',
                  'partner_image', 'feedback_ru']


class PartnerFeedbackSerializerEn(serializers.ModelSerializer):
    class Meta:
        model = PartnerFeedback
        fields = ['id', 'partner_name_en', 'partner_bio_en',
                  'partner_image', 'feedback_en']


class PartnerFeedbackTitleSerializerUz(serializers.ModelSerializer):
    class Meta:
        model = PartnerFeedbackTitle
        fields = ['title_uz', 'text_uz']


class PartnerFeedbackTitleSerializerRu(serializers.ModelSerializer):
    class Meta:
        model = PartnerFeedbackTitle
        fields = ['title_ru', 'text_ru']


class PartnerFeedbackTitleSerializerEn(serializers.ModelSerializer):
    class Meta:
        model = PartnerFeedbackTitle
        fields = ['title_en', 'text_en']


class ContactInfoSerializerUz(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['address_uz', 'facebook', 'instagram', 'telegram',
                  'tweeter', 'linkedin', 'youtube', 'phone1', 'phone2', 'email']


class ContactInfoSerializerRu(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['address_ru', 'facebook', 'instagram', 'telegram',
                  'tweeter', 'linkedin', 'youtube', 'phone1', 'phone2', 'email']


class ContactInfoSerializerEn(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['address_en', 'facebook', 'instagram', 'telegram',
                  'tweeter', 'linkedin', 'youtube', 'phone1', 'phone2', 'email']


class TeamSerializerUz(serializers.ModelSerializer):
    technalogies = TechnologySerializer(many=True)

    class Meta:
        model = Team
        fields = ['id', 'name_uz', 'title_uz',
                  'technalogies', 'image', 'order']


class TeamSerializerRu(serializers.ModelSerializer):
    technalogies = TechnologySerializer(many=True)

    class Meta:
        model = Team
        fields = ['id', 'name_ru', 'title_ru',
                  'technalogies', 'image', 'order']


class TeamSerializerEn(serializers.ModelSerializer):
    technalogies = TechnologySerializer(many=True)

    class Meta:
        model = Team
        fields = ['id', 'name_en', 'title_en',
                  'technalogies', 'image', 'order']


class IndustryTitleSerializerUz(serializers.ModelSerializer):
    class Meta:
        model = IndustryTitle
        fields = ['id', 'title_uz', 'text_uz']


class IndustryTitleSerializerRu(serializers.ModelSerializer):
    class Meta:
        model = IndustryTitle
        fields = ['id', 'title_ru', 'text_ru']


class IndustryTitleSerializerEn(serializers.ModelSerializer):
    class Meta:
        model = IndustryTitle
        fields = ['id', 'title_en', 'text_en']


class IndustrySerializerUz(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ['id', 'title_uz', 'text_uz', 'icon', 'icon_style']


class IndustrySerializerRu(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ['id', 'title_ru', 'text_ru', 'icon', 'icon_style']


class IndustrySerializerEn(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ['id', 'title_en', 'text_en', 'icon', 'icon_style']


class VacancySerializerUz(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['id', 'title_uz', 'text_uz', 'short_title_uz']


class VacancySerializerRu(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['id', 'title_ru', 'text_ru', 'short_title_ru']


class VacancySerializerEn(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['id', 'title_en', 'text_en', 'short_title_en']


class FormContentSerializerUz(serializers.ModelSerializer):
    class Meta:
        model = FormContent
        fields = ['id', 'title_uz', 'subtitle1_uz', 'text1_uz', 'subtitle2_uz',
                  'text2_uz', 'hide_second_part', 'type', 'is_active']


class FormContentSerializerRu(serializers.ModelSerializer):
    class Meta:
        model = FormContent
        fields = ['id', 'title_ru', 'subtitle1_ru', 'text1_ru', 'subtitle2_ru',
                  'text2_ru', 'hide_second_part', 'type', 'is_active']


class FormContentSerializerEn(serializers.ModelSerializer):
    class Meta:
        model = FormContent
        fields = ['id', 'title_en', 'subtitle1_en', 'text1_en', 'subtitle2_en',
                  'text2_en', 'hide_second_part', 'type', 'is_active']


class ClientMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientMessage
        fields = "__all__"


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = "__all__"
