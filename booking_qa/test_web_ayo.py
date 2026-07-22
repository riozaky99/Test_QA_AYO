from playwright.sync_api import sync_playwright, Page, Browser

BASE_URL = "https://ayo.co.id"

def _visit(page: Page, path: str):
    page.goto(BASE_URL + path, wait_until="networkidle")

def test_homepage_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/126.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 900},
        )
        page = context.new_page()
        _visit(page, "/")
        assert page.title() == "AYO : Super Sport Community App"
        main_heading = page.locator("text=Super Sport Community App").first
        assert main_heading.is_visible()
        browser.close()

def test_main_bareng_page_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/126.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 900},
        )
        page = context.new_page()
        _visit(page, "/main-bareng")
        assert page.locator("text=EVENT MAIN BARENG").first.is_visible()
        assert page.locator("button:has-text('Cari mabar'), button:has-text('Filter')").count() >= 1
        assert page.locator("a[href*='/main-bareng/']").count() >= 1
        browser.close()

def test_venues_page_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/126.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 900},
        )
        page = context.new_page()
        _visit(page, "/venues")
        assert page.locator("text=BOOKING LAPANGAN ONLINE TERBAIK").first.is_visible()
        assert page.locator("text=Menampilkan").count() >= 1
        assert page.locator("text=/\\d+ venue tersedia/").count() >= 1
        assert page.locator("a[href*='/venues/']").count() >= 1
        browser.close()

def test_venues_search_filters_and_pagination():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/126.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 900},
        )
        page = context.new_page()
        _visit(page, "/venues")
        page.locator("text=Pilih Cabang Olahraga").first.click()
        page.locator("text=Padel").first.click()
        page.wait_for_timeout(1000)
        assert page.locator("text=Menampilkan").count() >= 1
        # pagination page 2
        page.locator("a[href*='/venues?page=']").first.click()
        page.wait_for_timeout(1000)
        assert "page=2" in page.url or page.locator("text=2").count() >= 1
        browser.close()

def test_venues_faq_and_cta():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/126.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 900},
        )
        page = context.new_page()
        _visit(page, "/venues")
        page.locator("text=FAQ").first.click()
        page.wait_for_timeout(500)
        assert page.locator("text=FAQ").count() >= 1
        page.locator("text=Daftarkan Venue").first.click()
        page.wait_for_timeout(500)
        assert page.locator("text=Daftarkan Venue").count() >= 1
        browser.close()
