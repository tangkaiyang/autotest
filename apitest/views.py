from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login


# Create your views here.

def test(request):
    return HttpResponse("hello test")


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request, 'login.html', {'error': 'username or password error.'})
    # else:
    #     context = {}
    #     return render(request, 'login.html', context)
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')