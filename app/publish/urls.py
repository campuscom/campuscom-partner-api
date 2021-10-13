from django.urls import path, include
from rest_framework import routers
from publish.views import PublishViewSet

router = routers.DefaultRouter()

router.register(r'publish', PublishViewSet, 'profile_enrollments')


urlpatterns = [
    path('', include(router.urls)),
]
