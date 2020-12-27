"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url ,include
from rest_framework.routers import DefaultRouter
from .views import HelloApiView , HelloViewSet ,UserProfileViewSet,LoginViewSet , UserProfileFeedViewSet


router = DefaultRouter()
router.register('hello-viewset' , HelloViewSet, basename='hello-viewset')
router.register('profile' , UserProfileViewSet)
router.register('login' , LoginViewSet, basename='login')
router.register('feed' , UserProfileFeedViewSet)

urlpatterns = [
    url(r'^viewall/', HelloApiView.as_view(), name='viewall'),
    url(r'', include(router.urls)),
    # url('', include('djoser.urls')),
    # url('', include('djoser.urls.authtoken')),
]
