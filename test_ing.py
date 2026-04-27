import re
import pytest
from playwright.sync_api import Page, expect

def test_ing_accept_analytical_cookies(page: Page, context):
    page.emulate(locale="pl-PL", timezone_id="Europe/Warsaw")
    page.goto("https://www.ing.pl/")
    settings_btn = page.get_by_role("button", name=re.compile(r"Ustawienia", re.IGNORECASE))
    
    expect(settings_btn).to_be_visible(timeout=10000)
    settings_btn.click()
    
    page.locator("div.cookie-policy-switch").filter(
        has_text=re.compile(r"analityczne", re.IGNORECASE)
    ).click()
    
    page.get_by_role("button", name=re.compile(r"Zaakceptuj", re.IGNORECASE)).click()
    page.wait_for_timeout(1000)

    cookies = context.cookies()
    consent_cookie = any(
        "ING" in c['name'].upper() or "CONSENT" in c['name'].upper()
        for c in cookies
    )
    
    assert consent_cookie, "Błąd: Cookie zgody nie zostało zapisane!"
