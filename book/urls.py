"""book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from book.views import index as view_index
from book.views import book as book_view
from book.views import login as login_view
from book.views import user as user_view
PRE = '.html'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_index.index),
    path('index'+PRE, view_index.index, name="index"),
    path('info/<int:id>'+PRE, book_view.info),
    path('login'+PRE, login_view.login, name='login'),
    # re_path(r'^login'+PRE+"(\?next=*)?", login_view.login, name='login'),
    path('account'+PRE, user_view.account),
]
