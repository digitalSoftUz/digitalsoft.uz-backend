from django.db import models

# Create your models here.


class MainTitle(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title_uz


class MainAboutUsTitle(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    text_uz = models.TextField()
    text_ru = models.TextField(null=True, blank=True)
    text_en = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to='aboutus/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title_uz


class MainAboutUsImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='about_image/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class MainAboutUsStatistic(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    subtitle_uz = models.CharField(max_length=255)
    subtitle_ru = models.CharField(max_length=255, null=True, blank=True)
    subtitle_en = models.CharField(max_length=255, null=True, blank=True)
    icon = models.ImageField(upload_to='about_image/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title_uz


class MainOurServiceText(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    text_uz = models.TextField()
    text_ru = models.TextField(null=True, blank=True)
    text_en = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.text_uz[:55]


class Service(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    text_uz = models.TextField()
    text_ru = models.TextField(null=True, blank=True)
    text_en = models.TextField(null=True, blank=True)
    icon = models.TextField()
    icon_style = models.TextField(null=True, blank=True)
    order = models.IntegerField(default=99)
    is_show_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title_uz


class Technology(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='technology/')

    def __str__(self):
        return self.title


class MainTechnologyCard(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    technologies = models.ManyToManyField(Technology)
    order = models.IntegerField(default=99)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title_uz


class PortifolioCategory(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title_uz


class PortifolioImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portifolio/')

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Portifolio(models.Model):
    TYPE = (
        (1, 'link'),
        (2, 'video'),
        (3, 'Slider'),
    )
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    description_uz = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    category = models.ForeignKey(PortifolioCategory, on_delete=models.CASCADE)
    type = models.SmallIntegerField(default=1, choices=TYPE)
    images = models.ManyToManyField(PortifolioImage)
    video = models.FileField(upload_to='portifolio/', null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    order = models.IntegerField(default=99)
    is_show_main = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title_uz


class Partner(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255, null=True, blank=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='partner/', null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name_uz


class PartnerFeedbackTitle(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    text_uz = models.TextField()
    text_ru = models.TextField(null=True, blank=True)
    text_en = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title_uz


class PartnerFeedback(models.Model):
    partner_name_uz = models.CharField(max_length=255)
    partner_name_ru = models.CharField(max_length=255, null=True, blank=True)
    partner_name_en = models.CharField(max_length=255, null=True, blank=True)
    partner_bio_uz = models.CharField(max_length=255)
    partner_bio_ru = models.CharField(max_length=255, null=True, blank=True)
    partner_bio_en = models.CharField(max_length=255, null=True, blank=True)
    partner_image = models.ImageField(upload_to='feadback/')
    feedback_uz = models.TextField()
    feedback_ru = models.TextField(null=True, blank=True)
    feedback_en = models.TextField(null=True, blank=True)
    order = models.IntegerField(default=99)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.partner_name_uz


class ClientMessage(models.Model):
    first_name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=50)
    text = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='message/', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} : {self.date}"


class ContactInfo(models.Model):
    address_uz = models.CharField(max_length=255)
    address_ru = models.CharField(max_length=255, null=True, blank=True)
    address_en = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255)
    tweeter = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    phone1 = models.CharField(max_length=50)
    phone2 = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


class Team(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255, null=True, blank=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    technalogies = models.ManyToManyField(Technology)
    image = models.ImageField(upload_to="team/")
    order = models.IntegerField(default=99)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name_uz


class IndustryTitle(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    text_uz = models.TextField()
    text_ru = models.TextField(null=True, blank=True)
    text_en = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title_uz


class Industry(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    text_uz = models.TextField()
    text_ru = models.TextField(null=True, blank=True)
    text_en = models.TextField(null=True, blank=True)
    icon = models.ImageField(upload_to='service/')
    icon_style = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title_uz


class Vacancy(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    text_uz = models.TextField()
    text_ru = models.TextField(null=True, blank=True)
    text_en = models.TextField(null=True, blank=True)
    short_title_uz = models.CharField(max_length=50)
    short_title_ru = models.CharField(max_length=50, null=True, blank=True)
    short_title_en = models.CharField(max_length=50, null=True, blank=True)
    order = models.IntegerField(default=99)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title_uz


class Resume(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=50)
    text = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='resume/', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} : {self.date}"


class FormContent(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    subtitle1_uz = models.CharField(max_length=255)
    subtitle1_ru = models.CharField(max_length=255, null=True, blank=True)
    subtitle1_en = models.CharField(max_length=255, null=True, blank=True)
    text1_uz = models.TextField()
    text1_ru = models.TextField(null=True, blank=True)
    text1_en = models.TextField(null=True, blank=True)
    subtitle2_uz = models.CharField(max_length=255)
    subtitle2_ru = models.CharField(max_length=255, null=True, blank=True)
    subtitle2_en = models.CharField(max_length=255, null=True, blank=True)
    text2_uz = models.TextField()
    text2_ru = models.TextField(null=True, blank=True)
    text2_en = models.TextField(null=True, blank=True)
    hide_second_part = models.BooleanField(default=False)
    type = models.CharField(max_length=50, choices=(
        ('Project', 'Project'), ('Resume', 'Resume')
    ))
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title_uz
 