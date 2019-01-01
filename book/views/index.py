from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from django.core import serializers
from book.dao.category import Category as CategoryDao
from django.shortcuts import render_to_response, render
from book.dao.book import Book as BookDao


def index(request):
    # res = Books.objects.filter(name="1111")
    category = CategoryDao()
    list = category.get_rand_categories(3)
    # for cat_id in list:
    categories = category.get_menu();

    # return HttpResponse(serializers.serialize('json', request))
    context = {}
    context['category_list'] = categories
    return render(request, 'layout.html', context)
    # return HttpResponse(request.config)
