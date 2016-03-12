from django.shortcuts import render
from django.http import HttpResponseRedirect
from future.moves.urllib.parse import urlencode
from yandex_money.api import Wallet

from .models import Wallet

try:
    from spend_ya_project.config import MONEY_CLIENT_ID, MONEY_REDIRECT_URI
except ImportError:
    import os

    MONEY_CLIENT_ID = os.environ.get('MONEY_CLIENT_ID')
    MONEY_REDIRECT_URI = os.environ.get('MONEY_REDIRECT_URI')


def index(request):
    scope = ['account-info', 'operation-history']
    auth_url = '{}&{}'.format(Wallet.build_obtain_token_url(MONEY_CLIENT_ID, MONEY_REDIRECT_URI, scope),
                              urlencode({
                                  "response_type": 'code'
                              }))
    return HttpResponseRedirect(redirect_to=auth_url)


def callback(request):
    is_success = False
    if not request.GET.get('error') and request.GET.get('code'):
        code = request.GET.get('code')
        is_success = True
    else:
        code = request.GET.get('error_description') or 'Error!'

    if is_success:
        access_token = Wallet.get_access_token(MONEY_CLIENT_ID, code, MONEY_REDIRECT_URI,
                                               client_secret=None)
        if 'access_token' in access_token:
            wallet = Wallet(access_token=access_token['access_token'])
            account_info = wallet.account_info()

            if 'account' in account_info:
                money = Wallet(account=account_info['account'],
                               access_token=access_token['access_token'])
                money.save()
                return render(request, 'money.html', {
                    'is_success': True
                })

    return render(request, 'money.html', {
        'is_success': False
    })
