"""
URL configuration for backend project.

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
import os
from django.conf import settings
from django.urls import path, include
from connectgmail import views
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # הוספת הנתיב ל-View של Home
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/google/', views.google_auth, name='google-auth'),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),

    path('', include('signup_app.urls')),  # חיבור האפליקציה הראשית
    path('instagram/', include('instagram.urls')),  
    path('gallery/', include('gallery.urls')),  # הוספת נתיבי הגלריה
    path('facebook/', include('connectfacebook.urls')),

]

# תמיכה בקבצי מדיה במצב פיתוח
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


   
    