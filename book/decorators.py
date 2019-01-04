from django.shortcuts import redirect, reverse
from django.http import HttpResponseRedirect

def check_session(func):
    """
    查看session值用来判断用户是否已经登录
    :param request:
    :return:
    """
    def wrapper(request, *args, **kwargs):
        id = request.session.get('id', None)  # 获取session值
        url = request.get_full_path()
        print(url)
        if not id:  # 判断是否已经登录
            return HttpResponseRedirect(reverse('login', kwargs={'next': url}))    # 如果没有登录返回登录页面
        return func(request, *args, **kwargs)  # 如果已经登录返回原函数请求页面
    return wrapper

