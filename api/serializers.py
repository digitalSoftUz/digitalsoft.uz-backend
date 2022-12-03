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
        fields = ['title','text']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['title','text', 'icon', 'icon_style']

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['title', 'icon']

class MainTechnologyCardSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer()
    class Meta:
        model = MainTechnologyCard
        fields = ['title', 'technologies']



class PortifolioCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PortifolioCategory
        fields = ['title']

class PortifolioImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortifolioImage
        fields = ['title', 'image']

class PortifolioSerializer(serializers.ModelSerializer):
    category = PortifolioCategorySerializer()
    images = PortifolioImageSerializer()
    class Meta:
        model = Portifolio
        fields = ['title', 'images', 'description', 'category', 'type', 'video', 'link']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['name', 'logo', 'website']

class PartnerFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['partner_name', 'partner_bio', 'partner_image', 'feedback']

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['address', 'facebook', 'instagram', 'telegram', 'tweeter', 'linkedin','youtube','phone1','phone2','email']

class TeamSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer()
    class Meta:
        model = Partner
        fields = ['name', 'title', 'technalogies', 'image', 'order']

class IndustryTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['title', 'text']

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['title', 'text', 'icon', 'icon_style']

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['title', 'text', 'short_title']






