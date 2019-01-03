from django.shortcuts import redirect


def check_session(func):
    """
    查看session值用来判断用户是否已经登录
    :param request:
    :return:
    """
    def wrapper(request, *args, **kwargs):
        user = request.session.get('user', None)  # 获取session值
        print("-------")
        print(user)
        print("----------")
        if not user:  # 判断是否已经登录
            return redirect('/login.html')   # 如果没有登录返回登录页面
        return func(request, *args, **kwargs)  # 如果已经登录返回原函数请求页面
    return wrapper

