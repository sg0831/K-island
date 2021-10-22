from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import UserViewSet, PlayListViewSet, LikeListViewSet, MusicViewSet
from rest_framework.routers import DefaultRouter

# User 목록 보여주기
user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
# detail 보여주기 + 수정 + 삭제
user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})


# PlayList 목록 보여주기
playList_list = PlayListViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
# PlayList detail 보여주기 + 수정 + 삭제
playList_detail = PlayListViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})


# LikeList 목록 보여주기
likeList_list = LikeListViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
# LikeList detail 보여주기 + 수정 + 삭제
likeList_detail = LikeListViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})


# Music 목록 보여주기
music_list = MusicViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
# Music detail 보여주기 + 수정 + 삭제
music_detail = MusicViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})


router = DefaultRouter()
# 첫 번째 인자는 url의 prefix, 두 번째 인자는 ViewSet
router.register('user', UserViewSet)
router.register('playList', PlayListViewSet)
router.register('likeList', LikeListViewSet)
router.register('music', MusicViewSet)

urlpatterns =[
	path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)