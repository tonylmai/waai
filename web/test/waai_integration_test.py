from urllib.request import urlopen

def test_render_homepage():
    homepage_html = urlopen("http://localhost:5000").read().decode("utf-8")
    assert "<title>a<\title>"
    assert homepage_html.count("<li>") == 3
