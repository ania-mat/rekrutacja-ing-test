import re
import pytest
from playwright.sync_api import Page, expect

def test_ing_accept_analytical_cookies(page: Page, context):
    page.goto("https://www.ing.pl/")
    
    settings_btn = page.get_by_role("button", name=re.compile(r"Ustawienia|Settings|Manage", re.IGNORECASE))
    
    if settings_btn.is_visible(timeout=5000):
        settings_btn.click()
        page.locator("div.cookie-policy-switch").filter(
            has_text=re.compile(r"analityczne|analytical", re.IGNORECASE)
        ).click()
        page.get_by_role("button", name=re.compile(r"Zaakceptuj|Accept", re.IGNORECASE)).click()
        page.wait_for_timeout(1000)

    cookies = context.cookies()
    assert len(cookies) > 0, "Błąd: Przeglądarka nie zapisała żadnych ciasteczek."

    consent_cookie = any(
        "ING" in c['name'].upper() or "CONSENT" in c['name'].upper()
        for c in cookies
    )

    assert consent_cookie, "Błąd: Nie znaleziono ciasteczka potwierdzającego zgody."
