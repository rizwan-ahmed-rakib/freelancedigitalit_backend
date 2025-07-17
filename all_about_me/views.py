from rest_framework import viewsets
from .models import SetupPage, AboutMe, ContactWithMe, Service, ImageGallery, Message
from .serializers import (
    SetupPageSerializer, AboutMeSerializer, ContactWithMeSerializer,
    ServiceSerializer, ImageGallerySerializer, MessageSerializer
)

class SetupPageViewSet(viewsets.ModelViewSet):
    queryset = SetupPage.objects.all()
    serializer_class = SetupPageSerializer

class AboutMeViewSet(viewsets.ModelViewSet):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer

class ContactWithMeViewSet(viewsets.ModelViewSet):
    queryset = ContactWithMe.objects.all()
    serializer_class = ContactWithMeSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ImageGalleryViewSet(viewsets.ModelViewSet):
    queryset = ImageGallery.objects.all()
    serializer_class = ImageGallerySerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
