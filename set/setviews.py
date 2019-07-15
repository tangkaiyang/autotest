from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Set


# Create your views here.


# 设置管理
def set_manage(request):
    username = request.session.get('user', '')
    set_list = Set.objects.all()
    return render(request, "set_manage.html", {"user": username, "sets": set_list})


# 用户管理
def set_user(request):
    user_list = User.objects.all()
    username = request.session.get('user', '')
    return render(request, "set_user.html", {"user": username, "users": user_list})


# 搜索
@login_required
def usersearch(request):
    username = request.session.get('user', '')
    search_username = request.GET.get('username', '')
    user_list = User.objects.filter(username__icontains=search_username)
    return render(request, 'set_user.html', {"user": username, "users": user_list})
