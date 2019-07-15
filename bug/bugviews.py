from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from .models import Bug


# Create your views here.

# bug管理
def bug_manage(request):
    username = request.session.get('user', '')
    bug_list = Bug.objects.all()
    return render(request, "bug_manage.html", {"user": username, "bugs": bug_list})


# 搜索
@login_required
def bugsearch(request):
    username = request.session.get('user', '')
    search_bugname = request.GET.get('bugname', '')
    bug_list = Bug.objects.filter(bugname__icontains=search_bugname)
    return render(request, 'bug_manage.html', {"user": username, "bugs": bug_list})
