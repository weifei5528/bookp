from django.shortcuts import render, redirect, reverse
from book.dao.user import User as UserDao
from book.decorators import check_session
from django.core import serializers
from django.http import HttpResponse
from book.util.common import Common
from django.contrib.auth import authenticate, login, logout


def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    else:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        auth = authenticate(request, username=username, password=password)
        print(auth)
        """
                if res:
            request.session['id'] = res.id
            request.session['username'] = res.username
            request.session['email'] = res.email
            request.session['phone'] = res.phone
            print(request.session.get('id', None))
            return redirect(reverse('index'))
        else:
        """

        return HttpResponse("用户名密码错误")


# 退出登录
@check_session
def logout(request):
    del request.session['id']




