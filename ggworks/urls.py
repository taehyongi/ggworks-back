"""ggworks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from ggworks.ggworks_api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'user_profiles', views.UserProfileViewSet)
router.register(r'token_info', views.TokenInfoViewSet)

urlpatterns = [
  path('admin/', admin.site.urls),
  # url(r'^channels/', include('ggworks.ggworks_channels.urls')),
  url(r'^api/', include(router.urls)),
  url(r'^api/login/', views.CustomObtainAuthToken.as_view()),
  url(r'^api/logout/', views.Logout.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)