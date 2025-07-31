from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser

from .models import SetupPage, AboutMe, ContactWithMe, Service, ImageGallery, Message, VideoGallery
from .serializers import (
    SetupPageSerializer, AboutMeSerializer, ContactWithMeSerializer,
    ServiceSerializer, ImageGallerySerializer, MessageSerializer, VideoSerializer
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
    parser_classes = (MultiPartParser, FormParser)  # এটি না থাকলে image পাবেনা!


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ImageGalleryViewSet(viewsets.ModelViewSet):
    queryset = ImageGallery.objects.all()
    serializer_class = ImageGallerySerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = VideoGallery.objects.all().order_by('-created_at')
    serializer_class = VideoSerializer