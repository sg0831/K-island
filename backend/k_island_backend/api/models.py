from django.db import models
from django.contrib.auth.models import User

class PlayList( models.Model ):
    user = models.ForeignKey( User, related_name='user' ,on_delete=models.CASCADE)
    name = models.CharField( max_length=50, null=False, blank=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True )
    created = models.DateTimeField( auto_now_add=True )
    count_music = models.IntegerField(default=0)
    played = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    def add_count_music(self):
        self.count_music += 1
    def add_played(self):
        self.played += 1
    def set_likes(self, count):
        self.likes = count



class LikeList(models.Model):
    playList = models.ForeignKey(PlayList, on_delete=models.CASCADE)
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)



class Music(models.Model):
    # 유저가 노래를 재생하는 순간 반드시 '최근 재생한 플레이리스트'에 들어가므로 null & blank 불가
    playList = models.ForeignKey(PlayList, null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, null=False, blank=False)
    thumbnail = models.ImageField(upload_to='images/', null=True, blank=True )
    # 유튜브 url 상의 비디오 ID
    v_id = models.CharField(max_length=50)
    played = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    def add_played(self):
        self.played += 1