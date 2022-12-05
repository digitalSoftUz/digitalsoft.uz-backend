from django.db import models

# Create your models here.


class MainTitle(models.Model):
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class MainAboutUsTitle(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    video = models.FileField(upload_to='aboutus/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class MainAboutUsImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='about_image/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class MainAboutUsStatistic(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='about_image/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class MainOurServiceText(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.text[:55]


class Service(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    icon = models.TextField()
    icon_style = models.TextField(null=True, blank=True)
    order = models.IntegerField(default=99)
    is_show_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Technology(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='technology/')

    def __str__(self):
        return self.title


class MainTechnologyCard(models.Model):
    title = models.CharField(max_length=255)
    technologies = models.ManyToManyField(Technology)
    order = models.IntegerField(default=99)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class PortifolioCategory(models.Model):
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


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
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(PortifolioCategory, on_delete=models.CASCADE)
    type = models.SmallIntegerField(default=1, choices=TYPE)
    images = models.ManyToManyField(PortifolioImage)
    video = models.FileField(upload_to='portifolio/', null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    order = models.IntegerField(default=99)
    is_show_main = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Partner(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='partner/', null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class PartnerFeedbackTitle(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class PartnerFeedback(models.Model):
    partner_name = models.CharField(max_length=255)
    partner_bio = models.CharField(max_length=255)
    partner_image = models.ImageField(upload_to='feadback/')
    feedback = models.TextField()
    order = models.IntegerField(default=99)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.partner_name


class ClientMessage(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=50)
    text = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='message/', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} : {self.date}"


class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
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
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=200)
    technalogies = models.ManyToManyField(Technology)
    image = models.ImageField(upload_to="team/")
    order = models.IntegerField(default=99)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class IndustryTitle(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Industry(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=500)
    icon = models.ImageField(upload_to='service/')
    icon_style = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    short_title = models.CharField(max_length=50)
    order = models.IntegerField(default=99)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


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
    title = models.CharField(max_length=255)
    subtitle1 = models.CharField(max_length=255)
    text1 = models.TextField(null=True, blank=True)
    subtitle2 = models.CharField(max_length=255)
    text2 = models.TextField(null=True, blank=True)
    hide_second_part = models.BooleanField(default=False)
    type = models.CharField(max_length=50, choices=(
        ('Project', 'Project'), ('Resume', 'Resume')
    ))
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
