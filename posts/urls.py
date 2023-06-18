from django.urls import path, include
from .views import PostViewSet
from rest_framework.routers import DefaultRouter

app_name = "posts"
router = DefaultRouter()
router.register('list', PostViewSet, basename='posts')

urlpatterns = [
    path("", include(router.urls)),
]
