import emoji
import telepot
from Queue import Queue
from django.core.urlresolvers import reverse_lazy
from spend_ya_project.settings import TELEGRAM_TOKEN_ID, BASE_URI, DEBUG

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


def start_bot():
    bot.setWebhook(url='')
    if not DEBUG:
        webhookurl = 'https://{host}{path}'.format(
            host=BASE_URI,
            path=reverse_lazy('hook', kwargs={'telegram_token': TELEGRAM_TOKEN_ID}))
        print webhookurl
        bot.setWebhook(webhookurl)
    print('Bot started working...')


if not DEBUG:
    bot.notifyOnMessage({
        'normal': on_chat_message,
        'inline_query': on_inline_query,
        'chosen_inline_result': on_chosen_inline_result,
    }, source=update_queue)
else:
    bot.notifyOnMessage({
        'normal': on_chat_message,
        'inline_query': on_inline_query,
        'chosen_inline_result': on_chosen_inline_result,
    })
