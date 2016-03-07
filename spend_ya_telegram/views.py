from Queue import Queue
import emoji
import telepot
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

try:
    from spend_ya_project.config import TELEGRAM_TOKEN_ID
except ImportError:
    import os
    TELEGRAM_TOKEN_ID = os.environ.get('TELEGRAM_TOKEN_ID')


update_queue = Queue()
bot = telepot.Bot(TELEGRAM_TOKEN_ID)


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        msg_text = msg.get('text')
        user_from = msg.get('from')
        username = user_from.get('username')
        if msg_text.startswith('/start'):
            bot.sendMessage(chat_id, text=(emoji.emojize(
                'Hello, {0}! Let\'s start working together!:grinning:'.format(username), use_aliases=True)))
        elif msg_text.startswith('/help'):
            bot.sendMessage(chat_id, text='Trust me, I\'m an Engineer!')
        else:
            bot.sendMessage(chat_id, text='Not quite my Tempo')


def on_inline_query(msg):
    # for creating answers
    print('Inline MSG: ', msg)


def on_chosen_inline_result(msg):
    # after user chose result from inline query
    print('Chosen Inline Result MSG: ', msg)


@csrf_exempt
def telehook(request):
    print 'telehook now is working'
    update_queue.put(request.body)
    print request.body
    return HttpResponse('Msg received')


def main():
    bot.setWebhook('https://ya-money-dev-pr-11.herokuapp.com/telehook')
    bot.notifyOnMessage({
        'normal': on_chat_message,
        'inline_query': on_inline_query,
        'chosen_inline_result': on_chosen_inline_result
    }, source=update_queue)
    print('Bot started working...')


if __name__ == 'spend_ya_telegram.views':
    main()
