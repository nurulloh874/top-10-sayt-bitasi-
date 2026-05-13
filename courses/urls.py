from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CourseViewSet, LessonViewSet, ProgressViewSet

router = DefaultRouter()
router.register('courses', CourseViewSet)
router.register('lessons', LessonViewSet)
router.register('progress', ProgressViewSet)

urlpatterns = [
    path('', include(router.urls)),
]