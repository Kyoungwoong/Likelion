from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
# 게시물 모델
class Post(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    # upload = 

    def __str__(self):
        return self.title

# 댓글 모델
class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    # foreign key로 작성
    post = models.ForeignKey(Post, null =True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment

# 자유 게시판 모델
class FreePost(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

# 자유 게시판 댓글 모델
class FreeComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    # foreign key로 작성
    post = models.ForeignKey(FreePost, null =True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment