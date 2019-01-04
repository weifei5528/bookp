# 任意views中插入如下代码
from django.contrib.auth.backends import ModelBackend
from book.models.user import User as UserModel
from django.db.models import Q
from book.util.common import Common


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        print("测试进入")
        try:
            user = UserModel.objects.get(Q(username=username) | Q(email=username))  # 同理还可以加一个 |Q(iphone=username)

            print(user)
            if user.password == Common.md5_password(password):
                return user
        except Exception as e:
            print(e)
            return None

