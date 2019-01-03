import random, re, hashlib
from django.http import JsonResponse


class Common(object):

    # 数组中随机获取指定数量的值
    # @param list [] 数组
    @staticmethod
    def get_rand_slice(list, num=3):
        slice_list = random.sample(list,num)
        print(slice_list)
        return slice_list

    # 验证邮箱是否正确
    @staticmethod
    def check_email(email):
        str = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
        if re.match(str, email) is not None:
            return True
        else:
            return False

    # md5加密
    @staticmethod
    def md5_password(password, salt='vfdimlsd'):
        md = hashlib.md5()
        md.update((password+salt).encode())
        return md.hexdigest()

    """
    返回json
    """
    @staticmethod
    def success(msg, url):
        data = {'status': 1, 'info': msg, 'url': url}
        return JsonResponse(data)

