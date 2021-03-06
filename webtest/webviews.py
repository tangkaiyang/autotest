from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login


from .models import Webcasestep, Webcase

# Create your views here.

# Web用例管理
@login_required
def webcase_manage(request):
    webcase_list = Webcase.objects.all()
    username = request.session.get('user', '') # 读取浏览器登录session
    return render(request, "webcase_manage.html", {"user": username, "webcases": webcase_list})

# Web用例测试步骤
@login_required
def webcasestep_manage(request):
    username = request.session.get('user', '')
    webcasestep_list = Webcasestep.objects.all()
    return render(request, "webcasestep_manage.html", {"user": username, "webcasesteps": webcasestep_list})


# web测试报告
@login_required
def webtest_report(request):
    username = request.session.get('user', '')
    return render(request, "webtest_report.html")

# 搜索
@login_required
def websearch(request):
    username = request.session.get('user', '')
    search_webcasename = request.GET.get('webcasename', '')
    webcase_list = Webcase.objects.filter(webcasename__icontains=search_webcasename)
    return render(request, 'webcase_manage.html', {"user": username, "webcases": webcase_list})

# 搜索
@login_required
def webstepsearch(request):
    username = request.session.get('user', '')
    search_webcasename = request.GET.get('webcasename', '')
    webcasestep_list = Webcase.objects.filter(webcasename__icontains=search_webcasename)
    return render(request, 'webcasestep_manage.html', {"user": username, "webcasesteps": webcasestep_list})