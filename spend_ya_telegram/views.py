from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from spend_ya_telegram.spend_ya_bot import update_queue


@csrf_exempt
def telehook(request):
    update_queue.put(request.body)
    print request.body
