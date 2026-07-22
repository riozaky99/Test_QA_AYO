from playwright.sync_api import sync_playwright, Page

BASE_URL = "https://ayo.co.id"


def _visit(page: Page, path: str):
    page.goto(BASE_URL + path, wait_until="networkidle")


def test_book_venue_mobile_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) "
                "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
            ),
            viewport={"width": 375, "height": 812},
            is_mobile=True,
        )
        page = context.new_page()
        _visit(page, "/venues")
        # Step: filter sport to Padel
        page.locator("text=Pilih Cabang Olahraga").first.click()
        if page.locator("text=Padel").count() >= 1:
            page.locator("text=Padel").first.click()
        page.wait_for_timeout(1000)
        # Step: open first venue detail via card link
        page.locator("a[href*='/venues/']").first.click()
        page.wait_for_timeout(1000)
        assert page.locator("text=/Rp\\d+/").count() >= 1 or page.locator("text=Pilih Tanggal,text=Jadwal,text=Book").count() >= 1
        browser.close()


def test_create_game_time_mobile_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) "
                "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
            ),
            viewport={"width": 375, "height": 812},
            is_mobile=True,
        )
        page = context.new_page()
        _visit(page, "/main-bareng")
        # Step: open event detail for game-time-like flow verification
        if page.locator("a[href*='/main-bareng/']").count() >= 1:
            page.locator("a[href*='/main-bareng/']").first.click()
            page.wait_for_timeout(1000)
            assert page.locator("text=/Mabar|Event|Detail|Join/").count() >= 1
        else:
            assert page.locator("text=EVENT MAIN BARENG").count() >= 1
        browser.close()
