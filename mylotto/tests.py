from django.test import TestCase

# Create your tests here.
from mylotto.models import GuessNumbers


class GuessNumbersTestCase(TestCase):
    def test_generateTestCase(self):
        g = GuessNumbers(name='monkey', text='1등 만세이!')
        g.generate()
        print(g.update_date)
        print(g.lottos)
        self.assertTrue(len(g.lottos) > 20)