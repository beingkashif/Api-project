from django.urls import path,include
from enroll.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('form', views.StudentViewSet, basename = 'Student')


urlpatterns=[
    path('', include(router.urls))
]
