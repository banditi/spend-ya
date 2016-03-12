import json


class Config(object):
    def __init__(self, default='config.json'):
        """
        Constructor
        :param default: Configuration
        :return:
        """
        try:
            self._dictionary = json.load(open(default))
        except IOError or ValueError:
            self._dictionary = {}

    def get(self, key, default=''):
        """
        Get parameter from config.json
        :param key:
        :param default: Default value
        :return:
        """
        return self._dictionary.get(key, default)
