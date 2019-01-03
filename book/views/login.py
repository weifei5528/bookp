from django.shortcuts import render
from book.dao.user import User as UserDao
import json
from django.http import HttpResponse
from book.util.common import Common


def login(request):
    username = 'weifei'
    password = '123456'
    user = UserDao()
    res = user.check_login(username, password)
    if not res:
        request.session['user'] = res

    if request.method == 'GET':
        return render(request, 'login/login.html')
    else:
        data = request.POST





