from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from addsearch import views


router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls), name='movies'),
]
