
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('payments/', include('payments.urls')),
    path('payments/', include('click.urls')),
]
