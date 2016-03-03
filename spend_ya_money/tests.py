from django.test import TestCase

from .models import YaMoney


class YaMoneyMethodTests(TestCase):

    def test_date(self):
        wallet = YaMoney(account=134, access_token='secret')
        self.assertEqual(wallet.created_at, wallet.updated_at)
