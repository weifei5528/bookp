# from __future__ import unicode_literals
from book.dao.category import Category as CategoryDao
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # 获取分类菜单
    category = CategoryDao()
    categories = category.get_menu()
    context = {}
    context['category_list'] = categories
    list = category.get_random_category_books()
    context['list'] = list
    return render(request, 'index/index.html', context)
