"""
URL configuration for photodashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# photodashboard/urls.py

from django.contrib import admin
from django.urls import path
from photoapp.views import home, search, upload_file  # Import the search view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home page
    path('search/', search, name='search'),
    path('upload/', upload_file, name='upload_file'), 
     # Search page
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

