from django.urls import path, include
from . import views
from .api import LectureViewSet, LectureImageViewSet, StudentsAttendLecturesViewSet, StudentLectures

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('lecture', LectureViewSet)
router.register('lecture-image', LectureImageViewSet)
router.register('sal', StudentsAttendLecturesViewSet, base_name='sal')

router.register('cur-att', StudentLectures, base_name='cur-att')



urlpatterns = [
	path('api/', include(router.urls)),
]