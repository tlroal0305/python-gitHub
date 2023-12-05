from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from user.models import User

def singin(request):
   if request.method == "GET":
     # 키(title)의 값("할로")를 터미널창에 출력
     print(request.GET['title'])
     return render(request, 'page/singin.html')
      
   if request.method == "POST":
     username = request.POST['username']
     password = request.POST['password']
     
     # 로그인 로직 구현
     user = authenticate( username = username, password = password )
     if user: # 로그인 시,
       login(request, user)
       return redirect('board')
     else:
       messages.error(request, "입력 값을 확인해주세요");
       return redirect('singin')
    

def singup(request):
   if request.method == "GET":
     return render(request, 'page/singup.html')
