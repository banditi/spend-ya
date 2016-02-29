import emoji
import telepot

try:
    from spend_ya_project.config import TELEGRAM_TOKEN_ID
except ImportError:
    import os
    TELEGRAM_TOKEN_ID = os.environ.get('TELEGRAM_TOKEN_ID')


class SpendYaBot(telepot.Bot):
    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            msg_text = msg.get('text')
            user_from = msg.get('from')
            username = user_from.get('username')
            if msg_text.startswith('/start'):
                self.sendMessage(chat_id, text=(emoji.emojize(
                    'Hello, {0}! Let\'s start working together!:grinning:'.format(username), use_aliases=True)))
            elif msg_text.startswith('/help'):
                self.sendMessage(chat_id, text='Trust me, I\'m an Engineer!')
            else:
                self.sendMessage(chat_id, text='Not quite my Tempo')

    def on_inline_query(self, msg):
        # for creating answers
        print('Inline MSG: ', msg)

    def on_chosen_inline_result(self, msg):
        # after user chose result from inline query
        print('Chosen Inline Result MSG: ', msg)

bot = SpendYaBot(TELEGRAM_TOKEN_ID)
bot.notifyOnMessage()
print('Bot started working...')
