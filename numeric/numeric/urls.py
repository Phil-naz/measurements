from django.urls import path, include
from django.contrib import admin


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('measurements.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),

]