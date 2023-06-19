from django.urls import path, include
from .views import PostViewSet, DirectoryViewSet
from rest_framework.routers import DefaultRouter

app_name = "posts"
router = DefaultRouter()
router.register('list', PostViewSet, basename='posts')
router.register('directory', DirectoryViewSet, basename='directory')

urlpatterns = [
    path("", include(router.urls)),
]
