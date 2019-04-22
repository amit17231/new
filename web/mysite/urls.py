from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('self.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)