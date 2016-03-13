from django.shortcuts import render
from django.http import HttpResponseRedirect
from future.moves.urllib.parse import urlencode
from spend_ya_project.settings import MONEY_CLIENT_ID, MONEY_REDIRECT_URI
from yandex_money.api import Wallet as YaWallet

from .models import Wallet


def index(request):
    scope = ['account-info', 'operation-history']
    auth_url = '{}&{}'.format(YaWallet.build_obtain_token_url(MONEY_CLIENT_ID, MONEY_REDIRECT_URI, scope),
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
        access_token = YaWallet.get_access_token(MONEY_CLIENT_ID, code, MONEY_REDIRECT_URI,
                                                 client_secret=None)
        if 'access_token' in access_token:
            wallet = YaWallet(access_token=access_token['access_token'])
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


def get_yamoney_history(uid, options):
    wallet = Wallet.objects.get(user__exact=uid)
    yawallet = YaWallet(access_token=wallet.access_token)
    return yawallet.operation_history(options=options)
