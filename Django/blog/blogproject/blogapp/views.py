from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentForm
# Create your views here.

def home(request):
    # 블로그 글들을 모조리 띄우는 코드
    # posts = Blog.objects.all()
    posts = Blog.objects.filter().order_by('date')
    return render(request, 'index.html', {'posts': posts})

# 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')

# blog 글을 저장해주는 함수
def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        # model객체.save()를 통해 모델 객체를 데이터베이스에 저장할 수 있다.
        post.save()
        
    return redirect('home')

# django from을 이용해서 입력값을 받는 함수 
# 장고는 하나의 url에서 GET요청과 POST요청을 둘다 받게 할 수 있음
# GET (= 입력값을 받을 수 있는 html 파일 가져오기) 
# POST  (= 입력한 내용을 데이터베이스에 저장. form에서 입력한 내용을 처리)
# 요청 둘다 처리 가능
def formcreate(request):
    # 입력 내용을 DB에 저장할 내용
    if(request.method == "POST"):
        form = BlogForm(request.POST)
        # form 데이터가 유효한지 검사
        if(form.is_valid()):
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')

    # 입력을 받을 수 있는 html 가져오기
    else:
        form = BlogForm()
    return render(request, 'form_create.html', {'form': form}) # third 인자는 from_create_html의 파라미터로 넘겨주는 인자, 단 딕셔너리 자료형으로

def modelcreate(request):
    # 입력 내용을 DB에 저장할 내용
    if(request.method == "POST") or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        # form 데이터가 유효한지 검사
        if(form.is_valid()):
            # Model 기반 폼은 자체가 save 메소드를 가지고 있음.
            form.save()
            return redirect('home')

    # 입력을 받을 수 있는 html 가져오기
    else:
        form = BlogModelForm()
    return render(request, 'form_create.html', {'form': form})

def detail(request, blog_id):
    # blog_id 번째 블로그 글을 database로 부터 가지고 와서 
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    # detail.html로 띄워주는 코드

    comment_form  = CommentForm()
    return render(request, 'detail.html', {'blog_detail': blog_detail, 'comment_form': comment_form})


def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)
    if(filled_form.is_valid()):
        finished_form = filled_form.save(commit=False)    
        finished_form.post = get_object_or_404(Blog, pk = blog_id)
        finished_form.save()
    
    return redirect('detail', blog_id)