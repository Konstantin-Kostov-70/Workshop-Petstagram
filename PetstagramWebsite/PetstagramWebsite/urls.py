from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PetstagramWebsite.common.urls')),
    path('accounts/', include('PetstagramWebsite.accounts.urls')),
    path('pets/', include('PetstagramWebsite.pets.urls')),
    path('photos/', include('PetstagramWebsite.photos.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
