from django.test import SimpleTestCase
from django.urls import reverse, resolve
from myapp.views import home

class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse("home")
        self.assertEqual(resolve(url).func, home)