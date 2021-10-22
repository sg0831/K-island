from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PlayList, LikeList, Music



class UserSerializer( serializers.ModelSerializer ):
	class Meta:
		model = User
		fields = [ 'id', 'username', 'password' ]
		extra_kwargs = {"password" : {"write_only" : True}}



class PlayListSerializer( serializers.ModelSerializer ):
	class Meta:
		model = PlayList
		fields = [ 'user', 'name', 'image', 'created', 'count_music', 'played', 'likes' ]



class LikeListSerializer( serializers.ModelSerializer ):
	class Meta:
		model = LikeList
		fields = [ 'playList', 'user' ]



class MusicSerializer( serializers.ModelSerializer ):
	class Meta:
		model = Music
		fields = [ 'playList', 'title', 'thumbnail', 'v_id', 'played' ]