from django.db import models

# Create your models here.

class SetupPage(models.Model):
    company_name = models.CharField(max_length=100)
    company_logo = models.ImageField(upload_to='company_logo', null=True, blank=True)
    location = models.TextField()

    def __str__(self):
        return self.company_name
    class Meta:
        verbose_name_plural = "Setup Page"




class AboutMe(models.Model):
    banner = models.ImageField(upload_to="aboutme/banner/", null=True, blank=True)
    hero_image = models.ImageField(upload_to="aboutme/hero_image/", null=True, blank=True)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=11)
    designation = models.CharField(max_length=100)
    Short_description = models.TextField()

    def __str__(self):
        return self.name+self.designation
    class Meta:
        verbose_name_plural = "About Me"

class ContactWithMe(models.Model):
    icon = models.ImageField(upload_to="contctWithMe/icon/", null=True, blank=True)
    media_name = models.CharField(max_length=100)
    hint = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.media_name+self.hint
    class Meta:
        verbose_name_plural = "Contact With Me"

class Service(models.Model):
    icon_or_image = models.ImageField(upload_to="service/icon_or_image/", null=True, blank=True)
    headline = models.CharField(max_length=100)
    sub_headline = models.CharField(max_length=200)
    link = models.URLField()
    def __str__(self):
        return self.headline

class ImageGallery(models.Model):
    image = models.ImageField(upload_to="gallery/", null=True, blank=True)
    class Meta:
        verbose_name_plural = "Image Gallery"

class Message (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    def __str__(self):
        return f"{self.name} - {self.email} - {self.subject} - {self.message}"