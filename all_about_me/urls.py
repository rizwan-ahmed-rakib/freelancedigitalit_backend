from rest_framework.routers import DefaultRouter
from .views import (
    SetupPageViewSet, AboutMeViewSet, ContactWithMeViewSet,
    ServiceViewSet, ImageGalleryViewSet, MessageViewSet
)

router = DefaultRouter()
router.register(r'setup', SetupPageViewSet)
router.register(r'about', AboutMeViewSet)
router.register(r'contact', ContactWithMeViewSet)
router.register(r'service', ServiceViewSet)
router.register(r'gallery', ImageGalleryViewSet)
router.register(r'message', MessageViewSet)

urlpatterns = router.urls
