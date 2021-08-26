from django.shortcuts import render,redirect
from fcuser.models import Fcuser
from .models import Board
from .forms import BoardForm
# Create your views here.

def board_detail(request):
    return render(request, 'board_detail.html')

def board_write(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            # session에서 사용자 정보 가져오기
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)
            
            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()
            
            return redirect('/board/list/')
    else:
        form = BoardForm()
    return render(request, 'board_write.html', {'form':form})

def board_list(request):
    # -는 역순으로 정렬한다는 뜻
    boards = Board.objects.all().order_by('-id')
    return render(request, 'board_list.html', {'boards':boards})