from urllib.request import urlopen

from unittest import TestCase


class HomepageTestCase(TestCase):
    """Test homepage for WAAI"""

    def test_render_homepage(self):
        """Test rendering of homepage of WAAI"""
        homepage_html = urlopen("http://localhost:5000").read().decode("utf-8")
        assert "<title>a<\title>"
        assert homepage_html.count("<li>") == 3
