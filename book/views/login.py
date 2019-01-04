from django.shortcuts import render, redirect, reverse
from book.dao.user import User as UserDao

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
        user = UserDao()
        res = user.check_login(username, password)
        if res:
            request.session['id'] = res.id
            request.session['username'] = res.username
            request.session['email'] = res.email
            request.session['phone'] = res.phone
        return redirect(reverse('index'))





