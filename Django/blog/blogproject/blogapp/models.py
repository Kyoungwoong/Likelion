from django.db import models

# Create your models here.
# 상속을 이용
class Blog(models.Model):
    # data type assign
    title = models.CharField(max_length=200) # 최대 길이 지정
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
    date = models.DateTimeField(auto_now_add=True) # 자동으로 지금 시간 추가
    
    # Title이름으로 블로그 제목 반영
    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # 어떤 게시물에 달려있는 댓글인지를 알 수 있는, 댓글이 달린 그 게시물이 쓰임.
    # Blog의 데이터를 foreinKey 
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment