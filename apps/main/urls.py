from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views.file import FileViewSet
from main.views.user import UserViewSet

router = DefaultRouter()
router.register('', UserViewSet, 'user')
router.register('file', FileViewSet, 'file')

urlpatterns = [
    path('', include(router.urls)),
]
