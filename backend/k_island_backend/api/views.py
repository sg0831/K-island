from django.http import HttpResponse
from .serializers import UserSerializer, PlayListSerializer, LikeListSerializer, MusicSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib import auth
from .models import PlayList, LikeList, Music
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import action
from rest_framework.response import Response



# 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	@action( detail=False, methods=['post'] )
	def sign_in( self, request ):
		user = self.queryset.get( username = request.POST['username'] )
		if not user == None:
			# check_password : 암호화된 비밀번호 확인
			#if check_password( request.POST['password'], user.password ):
			if user.password == request.POST['password']:
				auth.login(request,user)
				return HttpResponse( status=200 )
		return HttpResponse( status=400 )
	@action( detail=False )
	def sign_out( self, request ):
		auth.logout( request )
		return HttpResponse( status=200 )



class PlayListViewSet(viewsets.ModelViewSet):
	queryset = PlayList.objects.all()
	serializer_class = PlayListSerializer
	"""
	@action( detail=False )
	def top10( self, request ):
	"""





class LikeListViewSet(viewsets.ModelViewSet):
	queryset = LikeList.objects.all()
	serializer_class = LikeListSerializer



class MusicViewSet(viewsets.ModelViewSet):
	queryset = Music.objects.all()
	serializer_class = MusicSerializer