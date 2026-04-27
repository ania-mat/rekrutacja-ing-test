import re
import pytest
from playwright.sync_api import Page, expect


def test_ing_accept_analytical_cookies(page: Page, context):
    page.goto("https://www.ing.pl/")
    page.locator(".js-cookie-policy-main-settings-button").click()
    page.locator("div.cookie-policy-switch").filter(
        has_text=re.compile("analityczne", re.IGNORECASE)
    ).click()
    page.get_by_role("button", name=re.compile("Zaakceptuj", re.IGNORECASE)).click()
    page.wait_for_timeout(1000)

    cookies = context.cookies()
    assert len(cookies) > 0, "Błąd: Przeglądarka nie zapisała żadnych ciasteczek po akceptacji."

    consent_cookie = any(
        "ING" in c['name'].upper() or "CONSENT" in c['name'].upper()
        for c in cookies
    )

    assert consent_cookie, "Błąd: Nie znaleziono ciasteczka potwierdzającego zapisanie zgód usera."