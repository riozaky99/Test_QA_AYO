import requests
from bs4 import BeautifulSoup
import re

BASE_HTML = "https://ayo.co.id/{page}"
HTML_PAGES = [
    "/",
    "/venues",
    "/main-bareng",
]

HTML_CHECKS = [
    ("a:contains('Sewa Lapangan')", None),
    ("a:contains('Main Bareng')", None),
    ("a:contains('Partner With Us')", None),
    ("a:contains('Blog')", None),
    ("a:contains('Get it on Google Play')", None),
    ("a:contains('Download on the App Store')", None),
    ("text=AYO Indonesia dalam Angka", None),
    ("text=PT Ayo Indonesia Maju", None),
]


class Counter:
    def __init__(self):
        self.page_errors = []

counter = Counter()


def fetch_page(path: str) -> BeautifulSoup:
    url = BASE_HTML.format(page=path.lstrip("/"))
    resp = requests.get(url, timeout=20)
    assert resp.status_code == 200, f"HTTP {resp.status_code} for {url}"
    assert "ayo" in resp.text.lower(), f"Unexpected body for {url}"
    return BeautifulSoup(resp.text, "html.parser"), url


def test_common_nav_links_exist():
    for path in HTML_PAGES:
        soup, url = fetch_page(path)
        expected_texts = [
            "Sewa Lapangan",
            "Main Bareng",
            "Partner With Us",
            "Blog",
            "Masuk",
            "Daftar",
        ]
        for text in expected_texts:
            found = bool(soup.find(string=re.compile(re.escape(text))))
            assert found, f"Expected text '{text}' not found on {url}"


def test_venue_page_listing():
    soup, url = fetch_page("/venues")
    assert soup.find("a", string=re.compile("Lihat Daftar Venue")) is not None or soup.find("a", href=re.compile("/venues")) is not None


def test_main_bareng_event_count_shown():
    soup, url = fetch_page("/main-bareng")
    body_text = soup.get_text(" ", strip=True).lower()
    assert "event mabar" in body_text
    assert "menampilkan" in body_text


def test_know_pricing_and_slots_source():
    trust_sources = [
        "ayo.app/venues",
        "App Store",
        "Play Store",
        "ayo.co.id",
    ]
    soup, url = fetch_page("/")
    html = soup.prettify()
    matched = any(s.lower() in html.lower() for s in trust_sources)
    assert matched, f"Expected AYO information sources not found on {url}"
