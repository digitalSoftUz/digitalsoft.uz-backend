from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(MainTitle)
class MainTitleAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']

@admin.register(MainAboutUsTitle)
class MainAboutUsTitle(admin.ModelAdmin):
    list_display = ['title','text', 'video', 'is_active']


@admin.register(MainAboutUsImage)
class MainAboutUsImageAdmin(admin.ModelAdmin):
    list_display = ['title','image', 'is_active']

@admin.register(MainAboutUsStatistic)
class MainAboutUsStatisticAdmin(admin.ModelAdmin):
    list_display = ['title','subtitle', 'icon', 'is_active']


@admin.register(MainOurServiceText)
class MainOurServiceTextAdmin(admin.ModelAdmin):
    list_display = ['title','text', 'is_active']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'text','icon', 'order', 'is_show_main', 'is_active']

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon']

@admin.register(MainTechnologyCard)
class MainTechnologyCardAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active']

@admin.register(PortifolioCategory)
class PortifolioCategoryAdmin(admin.ModelAdmin):
    list_display = ['title','is_active']

@admin.register(PortifolioImage)
class PortifolioImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']

@admin.register(Portifolio)
class PortifolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'category', 'type','video', 'link', 'order', 'is_show_main', 'is_active']

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name','logo','website','is_active']

@admin.register(PartnerFeedback)
class PartnerFeedbackAdmin(admin.ModelAdmin):
    list_display = ['partner_name', 'partner_bio', 'partner_image', 'feedback', 'order', 'is_active']

@admin.register(PartnerFeedbackTitle)
class PartnerFeedbackTitleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'is_active']

@admin.register(ClientMessage)
class ClientMessageAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'text', 'file', 'date']

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['address', 'facebook', 'instagram', 'telegram', 'tweeter', 'linkedin','youtube','phone1','phone2','email', 'is_active']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'image', 'order', 'is_active']

@admin.register(IndustryTitle)
class IndustryTitleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text']

@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'icon', 'icon_style', 'is_active']

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'short_title', 'is_active']

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'text', 'file', 'date']
