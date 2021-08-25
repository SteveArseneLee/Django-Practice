from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .forms import LoginForm

def home(request):
    user_id = request.session.get('user')
    
    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)
        
    return HttpResponse('Home!')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    
    return redirect('/')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            # session
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})
    
    # if request.method == 'GET':
    #     return render(request, 'login.html')
    # elif request.method == 'POST':
    #     username = request.POST.get('username', None)
    #     password = request.POST.get('password', None)
        
    #     res_data = {}
    #     if not (username and password):
    #         res_data['error'] = '모든 값을 입력해야합니다.'
    #     else:
    #         # 다시 Fcuser라는 모델에서 정보를 가져옴
    #         fcuser = Fcuser.objects.get(username=username)
    #         if check_password(password, fcuser.password):
    #             # 비밀번호가 일치, 로그인 처리
    #             # 세션!
    #             request.session['user'] = fcuser.id
    #             # redirect로 다시 홈으로 돌아가기
    #             return redirect('/') # /을 쓰면 현재 쓰는 웹 사이트의 root로 감
    #         else:
    #             res_data['error'] = '비밀번호를 틀렸습니다.'
        
        # return render(request, 'login.html', res_data)
        

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        
        # Error 메세지를 담는 공간
        res_data={}
        
        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야합니다'
        elif password != re_password:
            # return HttpResponse('비밀번호가 다릅니다')
            res_data['error'] = '비밀번호가 다릅니다'
        else:       
            fcuser = Fcuser(
                username = username,
                useremail = useremail,
                password = make_password(password)
            )
            
            fcuser.save()
        
        return render(request, 'register.html', res_data)
        