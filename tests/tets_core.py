import unittest

class LgtmTets(unittest.TestCase):
    def test_lgtm(self):
        from lgtm.core import lgtm
        self.assertIsNone(lgtm())
