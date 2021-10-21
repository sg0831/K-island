from django.urls import path, include
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

# 목록 보여주기
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



router = DefaultRouter()
# 첫 번째 인자는 url의 prefix, 두 번째 인자는 ViewSet
router.register('user', UserViewSet)

urlpatterns =[
	path('', include(router.urls))
]
