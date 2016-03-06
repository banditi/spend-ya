import requests
import json

URL_TEMPLATE = 'https://api.botan.io/track?token={token}&uid={uid}&name={name}'
SHORTENER_URL = 'https://api.botan.io/s/'


class Botan():
    """
        Class Botan for tracking user actions.
        http://botan.io/
    """
    def __init__(self, token):
        """
            Constructor of Botan

            Args:
                token: A string with token for your bot. Ask @botaniobot
        """
        self.__token = token

    def track(self, uid, message, name='Message'):
        """
            Tracking action

            Args:
                uid: An integer with user ID
                message: A dictionary with user message
                name: A string with command name

            Returns:
                Response from server or False
        """
        url = URL_TEMPLATE.format(token=str(self.__token), uid=str(uid), name=name)
        headers = {'Content-type': 'application/json'}
        try:
            r = requests.post(url, data=json.dumps(message), headers=headers)
            return r.json()
        except requests.exceptions.Timeout:
            # set up for a retry, or continue in a retry loop
            return False
        except requests.exceptions.RequestException as e:
            # catastrophic error
            print(e)
            return False

    def short_url(self, url, uids):
        """
            Short URL for specified users of a bot

            Args:
                url: A string with URL for short
                uids: A list with user IDs

            Returns:
                Shortener URL or original URL
        """
        try:
            return requests.get(SHORTENER_URL, params={
                'token': self.__token,
                'url': url,
                'user_ids': ','.join(str(uid) for uid in uids),
            }).text
        except:
            return url
