from rest_framework import serializers
from .models import SetupPage, AboutMe, ContactWithMe, Service, ImageGallery, Message

class SetupPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SetupPage
        fields = '__all__'

class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = '__all__'

class ContactWithMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactWithMe
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ImageGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageGallery
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
