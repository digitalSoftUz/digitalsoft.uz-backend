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
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class MainAboutUsImage(models.Model):
    title = models.CharField(max_length=255)
    image=models.ImageField(upload_to='about_image/', null=True, blank=True)
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
    text = models.TextField()
    text = models.BooleanField(default=True)

    def __str__(self):
        return self.text[:55]

class Service(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    icon = models.ImageField(upload_to='service/')
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
    type = models.SmallIntegerField(default=1, choices= TYPE)
    images = models.ManyToManyField(PortifolioImage)
    video = models.FileField(upload_to='portifolio/', null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
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
    title = models.CharField(max_length = 255)
    text = models.TextField()
    
    def __str__(self):
        return self.title


class PartnerFeedback(models.Model):
    partner_name = models.CharField(max_length=255)
    partner_bio = models.CharField(max_length=255)
    partner_image = models.ImageField(upload_to='feadback/')
    feedback = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.partner_name



    


    
    
