from django.test import TestCase


class SimpleTestCase(TestCase):
    def test_mult_ok(self):
        url = "/x/4/5/"
        expected = "4x5=20"

        resp = self.client.get(url)

        # self.assertEqual(resp.status_code, 200)
        # self.assertEqual(resp.body, expected)
        self.assertContains(resp, expected)

    def test_mult_bad(self):
        url = "/x/ki/5/"
        expected = "bad request"

        resp = self.client.get(url)

        self.assertContains(resp, expected, status_code=400)

    def test_mult_notfound(self):
        url = "/x/5/"

        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 404)