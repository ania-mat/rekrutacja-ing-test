import re
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function")
def context_args(context_args):
    return {
        **context_args,
        "locale": "pl-PL",
        "timezone_id": "Europe/Warsaw",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "viewport": {"width": 1920, "height": 1080},
    }

def test_ing_accept_analytical_cookies(page: Page):
    page.set_extra_http_headers({
        "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    page.goto("https://www.ing.pl/", wait_until="networkidle", timeout=60000)
    
    try:
        dostosuj_btn = page.get_by_role("button", name=re.compile(r"Dostosuj", re.IGNORECASE))
        expect(dostosuj_btn).to_be_visible(timeout=15000)
        dostosuj_btn.click()
        analityczne_header = page.get_by_role("heading", name=re.compile(r"Cookies analityczne", re.IGNORECASE))
        analityczne_header.click()
        accept_btn = page.get_by_role("button", name=re.compile(r"Zaakceptuj", re.IGNORECASE)).last
        accept_btn.click()
        page.wait_for_timeout(2000)
        expect(dostosuj_btn).not_to_be_visible()
        cookies = page.context.cookies()
        assert len(cookies) > 0, "Błąd: Przeglądarka nie zapisała żadnych ciasteczek."

    except Exception as e:
        print("TimeoutError czyli Anti-Bot na serwerze CI.")
        raise e
