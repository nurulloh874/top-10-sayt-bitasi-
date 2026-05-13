from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, LikeViewSet, FollowViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('likes', LikeViewSet)
router.register('follows', FollowViewSet)

urlpatterns = [
    path('', include(router.urls)),
]