import random


class Common(object):

    # s数组中随机获取指定数量的值
    @staticmethod
    def get_rand_slice(list, num=3):
        count = len(list)
        random.seed(count)
        slice_list = random.sample(list,num)
        return slice_list

