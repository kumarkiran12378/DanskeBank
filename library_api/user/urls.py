
from django.urls import path, include
from user.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('/', include(router.urls)),
]
