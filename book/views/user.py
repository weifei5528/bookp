from django.shortcuts import render
from book.decorators import check_session


@check_session
def account(request):
    return render(request, 'user/account.html')
