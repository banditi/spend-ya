from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import spend_ya_bot
from spend_ya_project.settings import TELEGRAM_TOKEN_ID


@csrf_exempt
def telehook(request, telegram_token):
    if telegram_token == TELEGRAM_TOKEN_ID:
        spend_ya_bot.update_queue.put(request.body)
        print request.body
    return HttpResponse("Msg Received")
