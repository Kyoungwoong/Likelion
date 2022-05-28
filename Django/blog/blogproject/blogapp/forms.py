from django import forms
from .models import Blog, Comment

# 장고 폼을 이용해서 폼을 자동으로 만드는 것은 클래스로 정의 가능
class BlogForm(forms.Form):
    # 내가 입력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget = forms.Textarea)

# model 폼을 이용해서 폼을 자동으로 만드는 것은 클래스로 정의 가능
class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        # fields = ['title', 'body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        