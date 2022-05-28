from django.shortcuts import render, redirect
# 로그인 로그아웃, 회원인지 아닌지 확인해주는 모듈
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    # POST 요청이 들어오면 로그인 처리
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        # 데이터 베이스에 해당 username과 password가 있는 지 없는지 확인
        # 장고는 기본적으로 user라고 하는 객체가 존재
        user = auth.authenticate(request, username = userid, password = pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
    # GET 요청이 들어오면 login form을 담고있는 login.html을 띄워주는 역할
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')