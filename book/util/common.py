import random


class Common(object):

    # 数组中随机获取指定数量的值
    # @param list [] 数组
    @staticmethod
    def get_rand_slice(list, num=3):
        slice_list = random.sample(list,num)
        print(slice_list)
        return slice_list

