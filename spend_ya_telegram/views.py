from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import spend_ya_bot

try:
    from spend_ya_project.config import TELEGRAM_TOKEN_ID
except ImportError:
    import os
    TELEGRAM_TOKEN_ID = os.environ.get('TELEGRAM_TOKEN_ID')


@csrf_exempt
def telehook(request, telegram_token):
    if telegram_token == TELEGRAM_TOKEN_ID:
        spend_ya_bot.update_queue.put(request.body)
        print request.body
    return HttpResponse("Msg Received")
