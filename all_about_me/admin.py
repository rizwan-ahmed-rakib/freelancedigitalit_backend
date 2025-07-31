from multiprocessing.resource_tracker import register

from django.contrib import admin
from .models import SetupPage,AboutMe,ContactWithMe,Service,Message,ImageGallery,VideoGallery
# Register your models here.
admin.site.register(SetupPage)
admin.site.register(AboutMe)
admin.site.register(ContactWithMe)
admin.site.register(ImageGallery)
admin.site.register(Service)
admin.site.register(Message)
admin.site.register(VideoGallery)


