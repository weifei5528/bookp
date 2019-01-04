from book.dao.common import Common
from book.util.common import Common as CommonUtil
from book.models.user import User as UserModel


class User(Common):
    """
    查询用户帐号密码是否正确
    :username 帐号
    :password 密码
    :return  正确返回查询的数据object 错误返回False
    """
    def check_login(self, username, password):
        try:
            if CommonUtil.check_email(username):
                user = UserModel.objects.get(email=username, status=1)
            else:
                user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            print("1111")
            return False
        except UserModel.MultipleObjectsReturned:
            print("22222")
            return False

        if user.password != CommonUtil.md5_password(password):
            print("3333")
            return False
        return user

