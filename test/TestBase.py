import unittest


class TestBase(unittest.TestCase):
    def test_ok(self):
        self.assertEqual('ok', 'ok')

    def test_fail(self):
        self.assertEqual('ok', 'ko')