import re
import pytest
from playwright.sync_api import Page, expect

def test_ing_accept_analytical_cookies(page: Page):
    page.goto("https://www.ing.pl/")
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
