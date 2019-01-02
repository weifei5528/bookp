from book.models.config import *


def sys_config(request):
    all_objects = Config.objects.all().values_list('name', 'value')
    # print(all_objects)
    sys_config = {}
    for key, v in all_objects:
        sys_config[key] = v
    # print(sys_config)
    return {'sys_config': sys_config}


def sys_suffix(request):
    return {'sys_suffix': ".html"}