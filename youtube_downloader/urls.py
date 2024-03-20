from django.contrib import admin
from django.urls import path, include  # Import the include function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('downloader/', include('downloader.urls')),  # Include your app's URLs
]
